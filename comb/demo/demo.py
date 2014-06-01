# -*- coding: utf-8 -*-

import comb.slot


class Slot(comb.slot.Slot):
    def __init__(self, combd):
        super(self.__class__, self).__init__(combd)
        self.threads_num = 4
        self.sleep = 1
        self.sleep_max = 60
        self.todo_list = range(1, 1000)
        print self.todo_list


    def __enter__(self):
        if not self.todo_list:
            print "todo list is empty,sleep now"
            return False
        else:
            next = self.todo_list.pop()
            return next


    def __exit__(self, exc_type, exc_val, exc_tb):
        print "this is used for transaction operation,ignore"


    def slot(self, result):
        print "call slot,current number is:", result
        pass









