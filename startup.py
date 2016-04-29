# -*- coding: utf-8 -*-


class Company(object):
    def __init__(self, name="unknown"):
        self._name = name

    def name(self):
        return self._name
