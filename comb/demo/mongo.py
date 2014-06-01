# -*- coding: utf-8 -*-


import comb.slot
import comb.mq.mongo as MongoHelper
from pymongo import MongoClient


class Slot(comb.slot.Slot):
    def __init__(self, combd):
        super(self.__class__, self).__init__(combd)
        self.threads_num = 4
        self.sleep = 1
        self.sleep_max = 60
        self.db = MongoClient('localhost', 27017)['db_mq']


    def __enter__(self):
        data = MongoHelper.token(self.db['mq1'])
        if not data:
            return False
        return data['_id']

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = MongoHelper.release(self.db['mq1'])


    def slot(self, result):
        print "call slot,current id is:", result
        pass









