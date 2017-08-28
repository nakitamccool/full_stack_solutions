#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fractions import gcd

class Fraction:
    """
    Fraction class
    """

    def __init__(self, numerator, denominator):
        """Initialize a `Fraction` object with `num` and `den`"""
        g = gcd(numerator, denominator)
        self.num = numerator // g
        self.den = denominator // g

    def __repr__(self):
        """Return the actual fraction as the string representation"""
        # Get the quotient and remainder using divmod
        quotient, remainder = divmod(self.num, self.den)
        # If the quotient is 0, then it means that the fraction
        # is smaller than a whole number, i.e. 3/4, 1/2, 4/6
        if quotient == 0:
            return '%s/%s' % (self.num, self.den)
        # Else if the remainder is equal to 0 then it means that we're
        # dealing with a whole number, i.e. 4/4, 2/2, 6/6
        elif remainder == 0:
            return '%s' % quotient
        # Otherwise, we're dealing with a vulgar fraction, i.e, 6/4,
        # 3/2, 17/6
        else:
            return '%s %s/%s' % (quotient, remainder, self.den)

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

    def __eq__(self, other):
        """Check if `self` is equal to `other`"""
        return self.__repr__() == Fraction(other.num, other.den).__repr__()
    
    def __ne__(self, other):
        """Check if `self` is not equal to `other`"""
        return self.__repr__() != Fraction(other.num, other.den).__repr__()

    def __gt__(self, other):
        """Check if `self` is greater than `other`"""
        return self.num > other.num and self.den < other.den

    def __lt__(self, other):
        """Check if `self` is less than `other`"""
        return self.num < other.num and self.den < other.den

