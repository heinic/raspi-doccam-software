#!/usr/bin/env python
# coding=UTF-8

# Raspberry Pi document camera
# Copyright (C) 2017  Nico Heitmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os, sys
from doccam.comm import sendCmd
from doccam.cgihelper import readGetQuery

# POST input
query = readGetQuery()

if not query['setting']: sys.exit()
sparts = query['setting'].split('_')
if not len(sparts) == 2: sys.exit()

if not 'value' in query: query['value'] = ''

# IPC
response = sendCmd((sparts[0], sparts[1], query['value']))

# Response
print('Content-type: text/plain\n')
sys.stdout.write(response)
