#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Fraction:
    """
    Fraction class
    """

    def __init__(self, numerator, denominator):
        """Initialize a `Fraction` object with `num` and `den`"""
        self.num = numerator
        self.den = denominator

    def __repr__(self):
        """Return the actual fraction as the string representation"""
        return '%s/%s' % (self.num, self.den)

    def __add__(self, other):
        """
        Add the two fractions (`self` and `other`)
        together and return a new `Fraction`
        """
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        """
        Subtract `self` from `other` and return a new `Fraction`
        """
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        """Multiply `self` by `other` and return a new `Fraction`"""
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Divide `self` by `other` using true division and return a new `Fraction`"""
        return Fraction(self.num / other.den, self.den / other.num)

    def __floordiv__(self, other):
        """Divide `self` by `other` using floor division and return a new `Fraction`"""
        return Fraction(self.num // other.den, self.den // other.num)

