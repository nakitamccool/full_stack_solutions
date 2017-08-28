#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Bird:
    """
    Bird Class
    """

    def __init__(self, kind, call):
        """
        Set the bird kind and it's call
        """
        self._kind = kind
        self._call = call

    def do_call(self):
        """
        Print out the bird kind and the call
        """
        print("A %s goes %s" % (self._kind, self._call))

owl = Bird('Owl', 'Twit Twoo!'

print(owl._kind)
