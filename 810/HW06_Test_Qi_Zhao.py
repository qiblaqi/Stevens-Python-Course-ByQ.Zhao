"""
this is a program contains Test Class for HW06

Written by Qi Zhao 
"""

import unittest as ut 
import HW06_Qi_Zhao as HW06

class TestString(ut.TestCase):
    """ Test cases class with extended test cases. """
    def test_insertion_sort(self):
        # Test my insertion sort function
        self.assertEqual(HW06.insertion_sort([3,2,1,0]), [0, 1, 2, 3])
        self.assertEqual(HW06.insertion_sort([]), [])
        self.assertFalse(HW06.insertion_sort([2, 2, 2, 10, 4]) == [2, 2, 2, 10, 4])
    
    def test_list_copy(self):
        # test my list compy function
        self.assertEqual(HW06.list_copy([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(HW06.list_copy([]), [])
        self.assertFalse(HW06.list_copy([1, 2, 3, 4]) == [1])
    
    def test_list_intersect(self):
        # test my list intersect fucntion
        self.assertEqual(HW06.list_intersect([3,2,1,0], [0, 1]), [1, 0])
        self.assertEqual(HW06.list_intersect([], []), [])
        self.assertFalse(HW06.list_intersect([2, 2, 2, 10, 4], []) == [2, 2, 2, 10, 4])

    def test_list_difference(self):
        #test my list difference function
        self.assertEqual(HW06.list_difference([3,2,1,0], [2, 0, 1]), [3])
        self.assertEqual(HW06.list_difference([], []), [])
        self.assertFalse(HW06.list_difference([2, 2, 2, 10, 4], []) != [2, 2, 2, 10, 4])

    def test_remove_vowels(self):
        # test my remove vowels function
        self.assertEqual(HW06.remove_vowels("ehEllo world!eA"), "hll wrld!")
        self.assertEqual(HW06.remove_vowels(""), "")
        self.assertFalse(HW06.remove_vowels("hello world!") == "hello world!")

    def test_check_pwd(self):
        # test my pwd checker function
        self.assertTrue(HW06.check_pwd("Password1"))
        self.assertFalse(HW06.check_pwd("Password"))
        self.assertFalse(HW06.check_pwd("password1"))
        self.assertFalse(HW06.check_pwd("PASSWORD1"))
        self.assertFalse(HW06.check_pwd("!@*&(*)"))
        self.assertFalse(HW06.check_pwd(""))


if __name__ == '__main__':
    ut.main(exit=False, verbosity=2)


