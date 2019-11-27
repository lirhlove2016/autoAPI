#!/usr/scripts/env python
# -*- coding: utf-8 -*-
import os

PROJECTPATH = "E:/myworkspace"

SRCDIR = os.path.join(PROJECTPATH, 'pyapi')
DATADIR = os.path.join(SRCDIR, 'datadir')
REPORTDIR = os.path.join(SRCDIR, 'report')


if __name__ == "__main__":
    print(SRCDIR)
    print(DATADIR)
    print(REPORTDIR)
