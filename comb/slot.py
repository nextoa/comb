# -*- coding: utf-8 -*-

class Slot(object):
    def __init__(self,combd):
        self.threads_num = 2
        self.sleep = 2
        self.sleep_max = 60
        self.debug=combd.debug
        self.initialize()


    def initialize(self):
        """Hook for subclass initialization.

        This block is execute before thread initial

        Example::

            class UserSlot(Slot):
                def initialize(self,*args,**kwargs):
                    self.attr = kwargs.get('attr',None)

                def slot(self, result):
                    ...

        """
        pass

    def __enter__(self):
        print "You should overwrite __enter__ method by subclass"
        return False


    def __exit__(self, exc_type, exc_val, exc_tb):
        print "You should overwrite __exit__ method by subclass"
        pass


    def slot(self):
        pass


