#!/usr/bin/env python
# coding:utf-8

import os
import imgsz
import cStringIO

for root, dirs, names in os.walk('.'):
    for name in names:
        filename = os.path.join(root, name)
        data = file(filename, 'rb').read(1024)
        try:
            mime, x, y= imgsz.fromstring(data)
            print '%s %dx%d:' % (mime, x, y), filename
        except ValueError, e:
            print 'ERROR:', filename, e