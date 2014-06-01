#!/usr/bin/python

import os, sys, signal
import comb.combd
import importlib


def useage():
    print "Useage", os.path.basename(sys.argv[0]), ''' [--root packages-root] [touch] slot-package.slot-module

    slot-package.slot-module        same as python package.module

    Global:
    --root                          find package.module in root path,it will search COMBPATH first

    '''


if '-h' in sys.argv or '--help' in sys.argv:
    useage()
    sys.exit(0)

_debug = False
if '--debug' in sys.argv:
    _debug = True


user_path = []

if '--root' in sys.argv:
    user_path.append()


module_name = sys.argv[-1]


if sys.argv.__len__() < 2 or module_name[:1] == '-':
    print "illegal option,use -h to get help."
    sys.exit(0)



# @todo set python path
# print os.getenv('SLOTPATH')
# sys.exit(1)


current_module = importlib.import_module(module_name)


if __name__ == '__main__':
    comb.combd.Start(current_module.Slot, **{'debug': _debug})










