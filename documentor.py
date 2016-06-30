#!/usr/bin/env python

# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


import copy
import json

from collections import OrderedDict

import almost_base64


def get_type(obj):
    if isinstance(obj, (dict, OrderedDict)):
        if 'type' in obj:
            return get_type(obj['type'])
        elif 'key' in obj:
            return get_type(obj['key'])
    elif isinstance(obj, basestring):
        return obj
    return 'unknown'


def get_ref_table(obj):
    if isinstance(obj, dict) and 'key' in obj and \
       isinstance(obj['key'], dict) and 'refTable' in obj['key']:
        return obj['key']['refTable']
    return 'unknown'


def get_ref_type(obj):
    if isinstance(obj, dict):
        if 'refType' in obj:
            return obj['refType']
        ref_type = 'strong'
        for key, value in obj.iteritems():
            temp = get_ref_type(value)
            if temp != 'strong':
                ref_type = temp
        return ref_type
    return 'strong'


def get_value(obj):
    if isinstance(obj, dict) and 'value' in obj:
        return obj['value']
    if isinstance(obj, dict) and 'valueType' in obj:
        return obj['valueType']
    return None


def get_value_type(obj):
    if isinstance(obj, dict) and ('value' in obj or 'valueType' in obj):
        return get_type(get_value(obj))
    return None


class EmptyStringArray(object):
    def __getitem__(self, key):
        return ''


class DocSection:
    def __init__(self, title='', obj=None, link=None):
        self.title = title
        if obj is not None and isinstance(obj, dict) and 'doc' in obj:
            self.text = obj['doc']
        else:
            self.text = []
        if obj is not None and isinstance(obj, dict) and 'type' in obj:
            self.sec_type = obj['type']
        else:
            self.sec_type = None
        self.subsections = []
        self.link = link

    def add(self, subsection):
        self.subsections.append(subsection)

    def _indstr(self, ind):
        if len(ind) == 0:
            return ''
        index = ''
        for n in ind:
            index += str(n) + '.'
        if len(ind) > 1:
            return index[:-1] + ' '
        return index + ' '

    def to_file(self, fd, level=1, ind=[], post=EmptyStringArray()):
        title = ('#' * level + ' ' + self._indstr(ind) + self.title +
                 post[level] + '\n\n')
        fd.write(title)
        if self.link is not None:
            fd.write('![%s_table_img](%s)\n\n' % (self.title, self.link))
        if self.sec_type is not None:
            ktype = get_type(self.sec_type)
            vtype = get_value_type(self.sec_type)
            ref_str = ''
            if vtype is not None:
                sec_type = ktype + '->' + vtype
            else:
                sec_type = ktype
            for_str = ' **refTable**: [%s](%s.html) **refType**: _%s_\n\n'
            if ktype == 'uuid':
                ref_table = get_ref_table(self.sec_type)
                ref_type = get_ref_type(self.sec_type)
                ref_str += for_str % (ref_table, ref_table.lower(), ref_type)
            if vtype == 'uuid':
                value_type = get_value(self.sec_type)
                ref_table = value_type['refTable']
                ref_type = get_ref_type(value_type)
                ref_str += for_str % (ref_table, ref_table.lower(), ref_type)
            fd.write('**Type**: _%s_%s\n\n' % (sec_type, ref_str))
        for line in self.text:
            fd.write(line + '\n')
        if len(self.text) > 0:
            fd.write('\n')
        ind.append(1)
        for section in self.subsections:
            section.to_file(fd, level + 1, ind, post)
            ind[-1] += 1
        del ind[-1]

    def fix_links(self):
        def clean(text):
            textl = text.lower()
            textl = textl.replace('_', '-')
            textl = textl.replace(' ', '-')
            return textl
        ref_mark = ']('
        new_text = []
        for line in self.text:
            index = line.find(ref_mark)
            while index != -1:
                # Split line.
                end = line.find(')', index+len(ref_mark))
                pre_link = line[:index+len(ref_mark)]
                link = line[index+len(ref_mark):end]
                post_link = line[end:]
                # Check if the link points to a table, a column or a key,
                # and create the corresponding link.
                parts = link.split('.')
                new_link = ''
                if len(parts) > 0:
                    new_link = parts[0].lower() + '.html'
                if len(parts) == 2:
                    new_link = new_link + '#' + clean(parts[1])
                if len(parts) == 3:
                    new_link = new_link + '#' + clean(parts[1]) + \
                               '-' + clean(parts[2])
                # Reassembly the line with the new link
                line = pre_link + new_link + post_link
                index = line.find(ref_mark, index + len(ref_mark))
            new_text.append(line)
        self.text = new_text
        # Recursively fix all links in text.
        for section in self.subsections:
            section.fix_links()

    def printme(self, level=1, ind=[]):
        post = {
            1: '',
            2: ' table',
            3: ' column',
            4: ' key'
        }
        title = ('#' * level + ' ' + self._indstr(ind) + self.title +
                 post[level] + '\n')
        print title
        for line in self.text:
            print line
        print '\n'
        ind.append(1)
        for section in self.subsections:
            section.printme(level + 1, ind)
            ind[-1] += 1
        del ind[-1]


class DocGroup:
    def __init__(self, title='', obj=None):
        self.section = DocSection(title, obj)
        self.subgroups = OrderedDict()

    def add_section(self, section):
        self.section.add(section)

    def add_group(self, path):
        groups = path.split('/')
        groups = groups[2:]
        current_group = self
        for group in groups:
            if group not in current_group.subgroups:
                current_group.subgroups[group] = DocGroup(group)
            current_group = current_group.subgroups[path]

    def get_group(self, path, schema):
        groups = path.split('/')
        current_path = '/' + groups[1]
        groups = groups[2:]
        current_group = self
        for group in groups:
            current_path += '/' + group
            if group not in current_group.subgroups:
                groups = schema['groups']
                current_group.subgroups[group] = \
                    DocGroup(group, groups.get(current_path))
            current_group = current_group.subgroups[group]
        return current_group

    def add_to_group(self, path, section, schema):
        group = self.get_group(path, schema)
        group.add_section(section)

    def to_doc_section(self):
        doc = copy.deepcopy(self.section)
        for group in self.subgroups.itervalues():
            doc.add(group.to_doc_section())
        return doc

    def from_table(self, table_name, table, schema, diag=None):
        if diag is not None:
            table_diag = diag.focus_on(table_name)
            link = table_diag.get_link()
            self.section = DocSection(table_name, table, link)
        else:
            self.section = DocSection(table_name, table)
        docgroup = self
        columns = table['columns']
        for column_name, column in columns.iteritems():
            section = DocSection(column_name, column)
            if 'group' in column:
                group = column['group']
                if isinstance(group, (str, unicode)):
                    docgroup.add_to_group(group, section, schema)
                else:
                    for g in group:
                        docgroup.add_to_group(g, section, schema)
            else:
                # Column does not belong to any group
                docgroup.add_to_group('/' + table_name + '/Ungrouped',
                                      section, schema)
            col_type = column['type']
            if 'valueMap' in col_type:
                for key_name, key in col_type['valueMap'].iteritems():
                    section = DocSection(column_name + ' : ' +
                                         key_name, key)
                    if 'group' in key:
                        docgroup.add_to_group(key['group'], section, schema)
                    else:
                        docgroup.add_to_group('/' + table_name + '/Ungrouped',
                                              section, schema)

    def from_schema(self, schema, path=[]):
        groups = schema['groups']
        if len(path) == 0:
            path.append(self.section.title)
        curr_path = '/' + '/'.join(path)
        print curr_path
        if curr_path in groups:
            self.section.text = groups[curr_path]['doc']
        for group_name, group in self.subgroups.iteritems():
            path.append(group_name)
            group.from_schema(schema, path)
            del path[-1]


def save_tables(doc):
    docs_dir = 'docs/'
    index_file = open(docs_dir + 'index.rst', 'w')
    index_file.write('OpenSwitch Schema Documentation\n')
    index_file.write('===============================\n\n')
    index_file.write('Tables:\n\n')
    index_file.write('.. toctree::\n')
    index_file.write('   :maxdepth: 1\n\n')
    for section in doc.subsections:
        name = section.title.lower()
        index_file.write('   ' + name + '\n')
        file_name = docs_dir + name + '.md'
        with open(file_name, 'w') as fd:
            section.to_file(fd)
    index_file.close()


def build_doc(schema):
    doc = DocSection('OpenSwitch Schema', schema)
    tables = schema['tables']
    for table_name, table in tables.iteritems():
        table_doc = DocSection(table_name, table)
        columns = table['columns']
        for column_name, column in columns.iteritems():
            col_doc = DocSection(column_name, column)
            if 'valueMap' in column['type']:
                for key_name, key in column['type']['valueMap'].iteritems():
                    key_doc = DocSection(key_name, key)
                    col_doc.add(key_doc)
            table_doc.add(col_doc)
        doc.add(table_doc)
    return doc


def build_grouped_doc(schema, diag=None):
    doc = DocSection('OpenSwitch Schema', schema)
    tables = schema['tables']
    for table_name, table in tables.iteritems():
        group = DocGroup()
        group.from_table(table_name, table, schema, diag)
        doc.add(group.to_doc_section())
    return doc


class TableDiagram:
    def __init__(self, name='', table=None):
        self.name = name

    def __str__(self):
        return 'class %s\n' % self.name

    def __eq__(self, other):
        if isinstance(other, (str, unicode)):
            return self.name == other
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Diagram:
    def __init__(self, schema=None):
        self.name = ''
        self.root_tables = set()
        self.tables = set()
        self.links = set()  # Tuples of table names
        self.weak_links = set()  # Tuples of table names
        if schema is not None:
            self.from_schema(schema)

    def add_table(self, table):
        self.tables.add(table)

    def add_root_table(self, table):
        self.root_tables.add(table)

    def add_link(self, table_a, table_b, link_type='strong'):
        self.links.add((table_a, table_b, link_type))

    def from_schema(self, schema):
        '''Builds a diagram from a schema.'''
        tables = schema['tables']
        for table_name, table in tables.iteritems():
            table_diag = TableDiagram(table_name)
            if table.get('isRoot', False):
                self.add_root_table(table_diag)
            else:
                self.add_table(table_diag)
            columns = table['columns']
            for column in columns.itervalues():
                if isinstance(column['type'], dict) and \
                   isinstance(column['type']['key'], dict) and \
                   'refTable' in column['type']['key']:
                    ref_table = column['type']['key']['refTable']
                    if 'refType' in column['type']['key'] and \
                       column['type']['key']['refType'] == 'weak':
                        self.add_link(table_name, ref_table, 'weak')
                    else:
                        self.add_link(table_name, ref_table)

    def from_table(self, table_name, table):
        '''Builds a diagram from a table.'''
        table_diag = TableDiagram(table_name)
        self.add_table(table_diag)
        columns = table['columns']
        for column in columns.itervalues():
            if isinstance(column['type'], dict) and \
               isinstance(column['type']['key'], dict) and \
               'refTable' in column['type']['key']:
                other_table_name = column['type']['key']['refTable']
                self.add_table(TableDiagram(other_table_name))
                self.add_link(table_name, other_table_name)

    def focus_on(self, table_name):
        '''Return a Diagram that focus on the given table.

        All tables and links not related to the focused table are deleted from
        the returned diagram.
        '''
        diag = Diagram()
        diag.name = table_name
        valid_tables = set()
        valid_tables.add(table_name)
        # Copy relevant links
        for ta, tb, link_type in self.links:
            if ta == table_name or tb == table_name:
                valid_tables.add(ta)
                valid_tables.add(tb)
                diag.add_link(ta, tb, link_type)
        # Copy relevant root tables
        for table in self.root_tables:
            if table.name in valid_tables:
                diag.root_tables.add(table)
        # Copy relevant tables
        for table in self.tables:
            if table.name in valid_tables:
                diag.tables.add(table)
        return diag

    def _group_tables(self, tables, name, n):
        '''Groups tables togueter using invisible links

        tables - set of tables
        name - a table's name to ignore
        n - elements per group
        '''
        t = tables.copy()
        ret = ''
        while len(t) >= n:
            g = []
            for i in range(n):
                table = t.pop()
                if table == name:
                    table = t.pop()
                g.append(table)
            for i in range(n):
                if i < n-1:
                    ret += '%s -[hidden]- %s\n' % (g[i].name, g[i+1].name)
                else:
                    ret += '%s -[hidden]- %s\n' % (g[i].name, g[0].name)
        return ret

    def __str__(self):
        ret = '@startuml\n'
        if len(self.root_tables) > 0:
            ret += 'package "Root Tables" {\n'
            for table in self.root_tables:
                ret += str(table)
            ret += '}\n'
        if len(self.tables) > 0:
            ret += 'together {\n'
            for table in self.tables:
                ret += str(table)
            ret += '}\n'
        for ta, tb, link_type in self.links:
            link = ' -%s-> '
            pos, no_pos = 'd', 'u'
            if tb == self.name:
                ta, tb = tb, ta
                pos, no_pos = no_pos, pos
                link = ' <-%s- '
            if tb in self.root_tables:
                pos, no_pos = no_pos, pos
            if link_type == 'weak':
                link = link.replace('-', '.')
            ret += ta + (link % pos) + tb + '\n'
        # Group tables when there are too many
        if len(self.root_tables) >= 8:
            ret += self._group_tables(self.root_tables, self.name, 3)
        if len(self.tables) >= 8:
            ret += self._group_tables(self.tables, self.name, 3)
        ret += 'hide circle\n'
        ret += 'hide members\n'
        ret += 'skinparam monochrome true\n'
        ret += 'legend right\n'
        ret += 'continuos line - <b>strong</b> reference\n'
        ret += 'dotted line - <i>weak</i> reference\n'
        ret += 'endlegend\n'
        ret += '@enduml\n'
        return ret

    def get_link(self):
        '''Return an URL to this diagram.'''
        enc = almost_base64.deflate_and_encode(str(self))
        return 'http://www.plantuml.com/plantuml/img/' + enc


def save_table_imgs(schema):
    img_dir = 'docs/img/'
    main_diag = Diagram(schema)
    for table_name, table in schema['tables'].iteritems():
        diag = main_diag.center_on(table_name)
        filename = img_dir + table_name.lower() + '.txt'
        with open(filename, 'w') as fp:
            fp.write(str(diag))


def main():
    with open('unified.extschema.json', 'r') as fp:
        schema = json.load(fp, object_pairs_hook=OrderedDict)
    diag = Diagram(schema)
    doc = build_grouped_doc(schema, diag)
    doc.fix_links()
    save_tables(doc)

    # diag = Diagram(schema)
    # cdiag = diag.focus_on('System')
    # print cdiag
    # img = almost_base64.deflate_and_encode(str(cdiag))
    # print 'http://www.plantuml.com/plantuml/img/' + img


if __name__ == '__main__':
    main()
