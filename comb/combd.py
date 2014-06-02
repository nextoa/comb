# -*- coding: utf-8 -*-

import os, sys
from threading import Thread
from time import sleep


def worker(iterator):
    time = iterator.sleep
    while True:
        with iterator as result:
            if result is not False:
                iterator.slot(result)
                time = iterator.sleep
            else:
                time += iterator.sleep
                if time > iterator.sleep_max:
                    time = iterator.sleep
                #@todo add Logger
                sleep(time)


class Start(object):
    def __init__(self, slot, *args, **kwargs):

        self.debug = kwargs.get('debug', False)

        if slot:
            iterator = slot(self)

            threads_num = iterator.threads_num
            i = 0
            while i < threads_num:
                t = Thread(target=worker, args=[iterator])
                t.daemon = True
                t.start()
                i += 1


class Touch(object):
    pass
