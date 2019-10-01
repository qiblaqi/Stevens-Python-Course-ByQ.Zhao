"""
this is a program contains Test Class for HW04

Written by Qi Zhao 
"""


import unittest as ut 
import HW04_Qi_Zhao as HW04

class TestFraction(ut.TestCase):
    #Test cases class with extended test cases.
    def test_simplify(self):
        self.assertEqual(HW04.Fraction(9, 27).simplify(),HW04.Fraction(1,3))
        self.assertEqual(HW04.Fraction(9, -27).simplify(),HW04.Fraction(-1,3))
        self.assertEqual(HW04.Fraction(1, -4).simplify(),HW04.Fraction(-1,4))
        self.assertFalse(HW04.Fraction(2, -4).simplify()==HW04.Fraction(-1,4))

class TestIteration(ut.TestCase):
    #Test cases for all the other functions

    def test_count_vowels(self):
        #test for the count vowels function
        self.assertEqual(HW04.count_vowels("Happy Day!"),2)
        self.assertEqual(HW04.count_vowels("HAppy Deust!"),3)
        self.assertEqual(HW04.count_vowels("H ppy D st!"),0)
        self.assertFalse(HW04.count_vowels("H ppy D s3et!")==0)

    def test_last_occurance(self):
        #test for the last occurance function for all sequence
        self.assertEqual(HW04.last_occurrence(42,[10,20,23,42,42]),4)
        self.assertEqual(HW04.last_occurrence('apple',['10',20,'23','42','apple']),4)
        self.assertEqual(HW04.last_occurrence('p','apple'),2)
        self.assertEqual(HW04.last_occurrence('p',[]),None)
    def test_my_enumerate(self):
        #test for the generator
        strA = "hello world!"
        strB = "hello "
        self.assertTrue(list(HW04.my_enumerate(strA))==list(enumerate(strA)))
        self.assertFalse(list(HW04.my_enumerate(strA))==list(enumerate(strB)))
        


if __name__ == '__main__':
    ut.main(exit=False,verbosity=2)
