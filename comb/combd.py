# -*- coding: utf-8 -*-

import os, sys,signal
from threading import Thread
from time import sleep



def signal_handle(signum, frame):
    print "\nUser interrupt.\n"
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handle)



def worker(iterator):
    time = iterator.sleep
    # iterator.beforePoll()

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
        self.threads_num = kwargs.get('threads_num', 10)
        self.sleep_max = kwargs.get('sleep_max', 60)
        self.sleep = kwargs.get('sleep', 2)


        if slot:
            iterator = slot(self)

            threads_num = iterator.threads_num
            i = 0
            while i < threads_num:
                t = Thread(target=worker, args=[iterator])
                t.daemon = True
                t.start()
                i += 1

            while True:
                sleep(1)


class Touch(object):
    pass
