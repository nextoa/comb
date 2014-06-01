# -*- coding: utf-8 -*-



def token(collection):
    return collection.find_and_modify({'token': {'$exists': False}}, {'$set': {'token': True}})


def release(collection):
    return collection.update({'token': True}, {'$set': {'token': False}}, multi=True)

def garbage(collection):
    collection.remove({'token': False}, multi=True)