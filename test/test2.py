#!/usr/bin/env python
# coding:utf-8
# coded by jigloo

import os
import imgsz

for root, dirs, names in os.walk('.'):
    for name in names:
        filename = os.path.join(root, name)
        try:
            mime, x, y= imgsz.size(filename)
            print '%s %dx%d:' % (mime, x, y), filename
        except ValueError, e:
            print 'ERROR:', filename, e