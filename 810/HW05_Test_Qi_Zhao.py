"""
this is a program contains Test Class for HW05

Written by Qi Zhao 
"""

import unittest as ut 
import HW05_Qi_Zhao as HW05

class TestString(ut.TestCase):
    """ Test cases class with extended test cases. """
    def test_reverse(self):
        # Test my reverse function
        self.assertEqual(HW05.reverse("abcd123"), "321dcba")
        self.assertEqual(HW05.reverse(""), "")
        self.assertFalse(HW05.reverse("123,,.") == "123,,.")
    
    def test_rev_enumerate(self):
        """ test the reverse enumerate function """
        result_1 = [
            (6, '3'), (5, '2'), 
            (4, '1'), (3, 'd'), 
            (2, 'c'), (1, 'b'), 
            (0, 'a')]
        self.assertEqual(list(HW05.rev_enumerate("abcd123")), result_1)
        self.assertEqual(list(HW05.rev_enumerate("")), [])
        self.assertFalse(list(HW05.rev_enumerate("abcd123")) == list(enumerate("abcd123")))
    
    def test_find_second(self):
        """ test the find next function """
        string_1 = "abbabbab"
        self.assertEqual(HW05.find_second("abba", string_1), 3)
        self.assertEqual(HW05.find_second("22", "a22ab2b22cc"), 7)
        self.assertFalse(HW05.find_second("", string_1) == 0)

    def test_get_lines(self):
        """ test get lines generator"""
        path = "c:\\Users\\snian\\Desktop\\a1\\Stevens-Python-Course\\810\\hw05_test.txt"
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        self.assertEqual(list(HW05.get_lines(path)),expect)
        self.assertFalse(list(HW05.get_lines(path)) == expect.append("<asda>"))
        with self.assertRaises(FileNotFoundError):
            list(HW05.get_lines(""))


if __name__ == '__main__':
    ut.main(exit=False, verbosity=2)