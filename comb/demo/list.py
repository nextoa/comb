# -*- coding: utf-8 -*-

import comb.slot


class Slot(comb.slot.Slot):
    def initialize(self):
       self.threads_num = 4
       self.sleep = 1
       self.sleep_max = 60

       if self.debug:               #debug flag
           self.todo_list = range(1000, 2000)
       else:
           self.todo_list = range(1, 1000)

       print self.todo_list


    def __enter__(self):
        if not self.todo_list:
            print "todo list is empty,sleep now,this must be return False when no data found."
            return False
        else:
            next = self.todo_list.pop()
            return next


    def __exit__(self, exc_type, exc_val, exc_tb):
        print "load after self.slot() call"


    def slot(self, result):
        print "call slot,current number is:", result
        pass









