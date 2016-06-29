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


import zlib


def _encode6bit(b):
    '''Code adapted from http://plantuml.com/codejavascript2.html'''
    if b < 10:
        return chr(48 + b)
    b -= 10
    if b < 26:
        return chr(65 + b)
    b -= 26
    if b < 26:
        return chr(97 + b)
    b -= 26
    if b == 0:
        return '-'
    if b == 1:
        return '_'
    return '?'


def _append3bytes(bb1, bb2, bb3):
    '''Code adapted from http://plantuml.com/codejavascript2.html'''
    b1 = ord(bb1[0])
    b2 = ord(bb2[0])
    b3 = ord(bb3[0])
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return '%c%c%c%c' % (_encode6bit(c1 & 0x3F), _encode6bit(c2 & 0x3F),
                         _encode6bit(c3 & 0x3F), _encode6bit(c4 & 0x3F))


def encode(data):
    '''Reencode data to ASCII using a transformation close to base64.

    Code adapted from http://plantuml.com/codejavascript2.html
    '''
    r = ''
    for i in range(0, len(data)-1, 3):
        if i+2 == len(data):
            r += _append3bytes(data[i], data[i+1], chr(0))
        elif i+1 == len(data):
            r += _append3bytes(data[i], chr(0), chr(0))
        else:
            r += _append3bytes(data[i], data[i+1], data[i+2])
    return r

def deflate(data):
    zobj = zlib.compressobj(0, zlib.DEFLATED,-zlib.MAX_WBITS,
                            zlib.DEF_MEM_LEVEL, 0)
    zdata = zobj.compress(data)
    zdata += zobj.flush()
    return zdata

def deflate_and_encode(string_val):
    ''' Compress a string to use with PlantUML image generation servers.

    Code adapted from http://plantuml.com/codejavascript2.html
    '''
    # Compress with zlib
    compressed_string = deflate(string_val)
    # Encode with almost base64
    return encode(compressed_string)
