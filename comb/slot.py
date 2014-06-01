# -*- coding: utf-8 -*-

class Slot(object):
    def __init__(self,combd):
        self.threads_num = 2
        self.sleep = 2
        self.sleep_max = 60
        self._debug=combd.debug

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value

