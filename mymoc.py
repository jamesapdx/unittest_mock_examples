#!/usr/bin/python

import time
import string
from random import random


def string_function(s):
    s = string.lower(s)# = mock.Mock(return_value="i am upper")
    s += " case"
    # print(s) --> "i am upper"
    # note, we don't have to mock every function
    s = string.replace(s, "upper", "lower")
    return s

def fun_main(obj):
    fun_called(obj, "bb")

def fun_called(obj, b):
    pass

def random_function():
    x = random()
    return x


def basic_return(val):
    return val + 3


class Adapter:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def is_up(self):
        return "up"

class Host:
    def __init__(self):
        self.adapter = Adapter("a","b")

    def is_adapter_up1(self):
        x = self.adapter.is_up()
        return x

    def is_adapter_up1(self):
        x = self.adapter.is_up()
        return x

    def is_adapter_up2(self):
        b = Adapter("a","b")
        x = b.is_up()
        return x

if __name__ == "__name__":
    mys("main")
