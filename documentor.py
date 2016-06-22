#!/usr/bin/env python

import copy
import json
import re

from collections import OrderedDict


class EmptyStringArray(object):
    def __getitem__(self, key):
        return ''


class DocSection:
    def __init__(self, title='', obj=None):
        self.title = title
        if obj and isinstance(obj, dict) and 'doc' in obj:
            self.text = obj['doc']
        else:
            self.text = []
        self.subsections = []

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
                    new_link = new_link + '#' + clean(parts[1]) + '-column'
                if len(parts) == 3:
                    new_link = new_link + '#' + clean(parts[1]) + \
                               '-' + clean(parts[2]) + '-key'
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


def add_to_groups(groups, group):
    paths = group.split('/')
    # Discart first two paths
    paths = paths[2:]
    cur_group = groups
    for path in paths:
        if path not in cur_group:
            cur_group[path] = OrderedDict()
        cur_group = cur_group[path]


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
                current_group.subgroups[group] = DocGroup(group + ' group')
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
                    DocGroup(group + ' group', groups.get(current_path))
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

    def from_table(self, table_name, table, schema):
        self.section = DocSection(table_name, table)
        docgroup = self
        columns = table['columns']
        for column_name, column in columns.iteritems():
            if 'doc' in column:
                section = DocSection(column_name + ' column', column)
                if 'group' in column:
                    group = column['group']
                    if isinstance(group, (str, unicode)):
                        docgroup.add_to_group(group, section, schema)
                    else:
                        for g in group:
                            docgroup.add_to_group(g, section, schema)
            col_type = column['type']
            if 'valueMap' in col_type:
                for key_name, key in col_type['valueMap'].iteritems():
                    if 'group' in key:
                        section = DocSection(column_name + ' : ' + key_name + ' key', key)
                        docgroup.add_to_group(key['group'], section, schema)

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



# class DocGroup:
#     def __init__(self, title='', obj=None, schema=None):
#         self.subgroups = OrderedDict()
#         self.subsections = []
#         self.doc = DocSection(title, obj)
#         self.schema = schema
#
#     def _add_to_subgroups(self, group, title, obj):
#         paths = group.split('/')
#         paths = paths[2:]
#         cur_group = self
#         for path in paths:
#             if path not in cur_group.subgroups:
#                 cur_group.subgroups[path] = DocGroup(title=path + ' group')
#             cur_group = cur_group.subgroups[path]
#         cur_group.subsections.append(DocSection(title, obj))
#
#     def add(self, title, obj):
#         if isinstance(obj, dict) and 'group' in obj:
#             if isinstance(obj['group'], list):
#                 for group in obj['group']:
#                     self._add_to_subgroups(group, title, obj)
#             else:
#                 self._add_to_subgroups(obj['group'], title, obj)
#
#     def to_doc_section(self):
#         doc = DocSection()
#         doc.title =  self.doc.title
#         doc.text =  self.doc.text
#         for section in self.subsections:
#             doc.add(section)
#         for group in self.subgroups.values():
#             doc.add(group.to_doc_section())
#         return doc
#
#     def from_table(self, table):
#         columns = table['columns']
#         for column_name, column in columns.iteritems():
#             self.add(column_name, column)

def save_tables(doc):
    docs_dir = 'docs/'
    index_file = open(docs_dir + 'index.rst', 'w')
    index_file.write('OpenSwitch Schema Documentation\n')
    index_file.write('===============================\n\n')
    index_file.write('Tables:\n\n')
    index_file.write('.. toctree::\n')
    index_file.write('   :maxdepth: 1\n\n')
    post = {
        1: ' table',
        2: ' column',
        3: ' key'
    }
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


def build_grouped_doc(schema):
    doc = DocSection('OpenSwitch Schema', schema)
    tables = schema['tables']
    for table_name, table in tables.iteritems():
        group = DocGroup()
        group.from_table(table_name, table, schema)
        doc.add(group.to_doc_section())
    return doc


def print_groups(groups, space=0):
    pre = ' ' * space * 2 + unichr(746)
    for group in groups:
        print pre + group
        print_groups(groups[group], space + 1)


def get_groups(table):
    columns = table['columns']
    groups = OrderedDict()
    for column_name, column in columns.iteritems():
        col_type = column['type']
        if isintance(col_type, dict) and 'valueMap' in col_type:
            grouped_keys = OrderedDict()
            for key_name, key in col_type['valueMap']:
                if 'group' in key:
                    if key['group'] not in grouped_key:
                        grouped_cols[key['group']] = []
                    grouped_cols[key['group']].append(key)

        else:
            if 'group' in column:
                if isinstance(column['group'], list):
                    for group in column['group']:
                        add_to_groups(groups, group)
                else:
                    add_to_groups(groups, column['group'])
    return groups





def main():
    with open('unified.extschema.json', 'r') as fp:
    #with open('myschema.json', 'r') as fp:
        schema = json.load(fp, object_pairs_hook=OrderedDict)
    doc = build_grouped_doc(schema)
    #doc.printme()
    doc.fix_links()
    save_tables(doc)

    # table = schema['tables']['Interface']
    # group = DocGroup()
    # group.from_table('Interface table', table, schema)
    # doc = group.to_doc_section()
    # doc.fix_links()
    # with open('interface.md','w') as fp:
    #     doc.to_file(fp)

    # groups = get_groups(table)
    # print groups
    # print_groups(groups)

    # mydoc = DocSection(title='My Doc')
    # groups = {}
    # groups['1'] = mydoc
    # topdoc = DocSection(title='Top Section')
    # topdoc.add(mydoc)
    # topdoc.printme()
    # groups['1'].title = 'Change Title'
    # topdoc.printme()



if __name__ == '__main__':
    main()


# class DocKey:
#     def __init__(self, key_name='', key=None):
#         self.name = key_name
#         if key:
#             self.doc = key['doc']
#         else:
#             self.doc = []
#
#
# class DocGroups():
#     def __init__(self, group_name, schema):
#         self.name = group_name
#         self.doc = []
#         self.groups = OrderedDict()
#         groups = schema['groups']
#         if groups:
#             if group_name in groups:
#                 self.doc = groups[group_name]['doc']
#
#
#     def add(self, name, obj):
#         if isinstance(name, (str, unicode)):
#             self.groups[name] = obj
#         elif isinstance(name, list):
#             for n in name:
#                 self.add
#         if 'group' in obj:
#             self.groups[obj[group]] = obj
#
#
# class DocColumn(DocKey):
#     def __init__(self, column_name='', column=None):
#         DocKey.__init__(self, column_name, column)
#         self.key_groups = DocGroups()
#
#     def add_key(self, key_name, key):
#         doc_key = DocKey(key_name, key)
#         if 'group' in key:
#             self.key_groups.add(key['group'], doc_key)
#         else:
#             self.key_groups
