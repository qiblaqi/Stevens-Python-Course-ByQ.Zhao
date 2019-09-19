"""
this is a program use Class to handle two Fractions plus, minus, mutiply, divide and
check-out if they equals to each other

upgraded with unittest module to build a test suite

Written by Qi Zhao
"""

import unittest as ut

class FractionTest(ut.TestCase):
    """ Test class of fraction which includes testing '+-*/ == >= <= != > <' """
    def test_init(self):
        #test deno cant be 0
        with self.assertRaises(ValueError):
            Fraction(1,0)
    
    def test_add(self):
        #test plus function 
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(2,5)
        self.assertEqual(testUnit_1+testUnit_2,Fraction(11,15))

    def test_sub(self):
        #test minus function 
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(2,5)
        self.assertEqual(testUnit_1-testUnit_2,Fraction(-1,15))
    
    def test_mul(self):
        #test multiply function 
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(2,5)
        self.assertEqual(testUnit_1*testUnit_2,Fraction(2,15))
    
    def test_truediv(self):
        #test divide function and vailid new fraction's denominator cant be 0
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(2,5)
        testUnit_3 = Fraction(0,4)
        self.assertEqual(testUnit_1/testUnit_2,Fraction(5,6))
        with self.assertRaises(ValueError):
            testUnit_1 / testUnit_3
    
    def test_eq(self):
        #test the equal function for negative or postive fraction
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(2,6)
        testUnit_3 = Fraction(-1,-3)
        self.assertTrue(testUnit_1==testUnit_2)
        self.assertTrue(testUnit_1==testUnit_3)
        #special test
        self.assertTrue(Fraction(-1,3),Fraction(1,-3))
    
    def test_ne(self):
        #test the not equal function 
        testUnit_1 = Fraction(1,3)
        testUnit_2 = Fraction(3,6)
        self.assertTrue(testUnit_1!=testUnit_2)
    
    def test_lt(self):
        #give two fractions check if self < other
        self.assertTrue(Fraction(-1,3)<Fraction(2,4))
        self.assertFalse(Fraction(1,-4)<Fraction(1,5))
    
    def test_gt(self):
        #check the greater than function
        self.assertTrue(Fraction(1,2)>Fraction(1,3))

    def test_ge(self):
        #check the greater than or equal to function, two steps 1.test '>'  2. test '='
        self.assertTrue(Fraction(1,2)>=Fraction(1,3))
        self.assertTrue(Fraction(1,2)>=Fraction(2,4))
    
    def test_le(self):
        #check the less than or equal to, like test_ge
        self.assertTrue(Fraction(1,3)<=Fraction(1,2))
        self.assertTrue(Fraction(1,3)<=Fraction(2,6))


class Fraction:
    """ Fraction class hold numerator and dorminator with method to do + - * / == with each other """
    def __init__(self,numerator, denominator):
        # This initiates the fraction's numerator and denominator
        if denominator == 0:
            raise ValueError("denominator cant be '0' !")
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self,other):
        #plus two fraction and return a new fraction 
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.denominator + other.numerator * self.denominator
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction
    
    def __sub__(self,other):
        #two fraction minus with each other
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.denominator - other.numerator * self.denominator
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def __mul__(self,other):
        #multiply two fractions with one denominator 
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.numerator 
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def __truediv__(self,other):
        #to reverse the fraction and multiply
        newFractionDeno = self.denominator * other.numerator
        newFractionNumer = self.numerator * other.denominator 
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def __eq__(self,other):
        # check two fractions have the same value or not
        newFractionNumer = self.numerator * other.denominator - other.numerator * self.denominator
        if newFractionNumer == 0:
            return True
        else:
            return False
    
    def __ne__(self,other):
        #check two fractions are not the same by using __eq__ function
        return not(self==other)

    def __lt__(self,other):
        #check self fraction is less than other fraction or not with
        return (self.numerator*other.denominator-self.denominator*other.numerator)<0 
        
    def __gt__(self,other):
        #check self fraction is greater than other fraction
        return (self.numerator*other.denominator-self.denominator*other.numerator)>0
    
    def __ge__(self,other):
        #check self >= other with using __lt__ function
        return not(self<other)
    
    def __le__(self,other):
        #check self <= other with using __gt__ function
        return not(self>other)

    def __str__(self):
        #output the fraction in a mathmetics way like '1/2' for f12
        return f"{self.numerator}/{self.denominator}"

def getNumber(yourInputMsg):
    # check user's input and make sure it can be converted into an integer
    bufferNumber = input(yourInputMsg)
    try:
        number = int(bufferNumber)
    except ValueError:
        print(f"{bufferNumber} is not a number, please type a number! ")
        number = getNumber(yourInputMsg)
    return number

def getCode(yourInputMsg):
    #check user's code is legal or not and make sure to get legal code command
    bufferCode = input(yourInputMsg)
    if bufferCode in ['+','-','*','/','==']:
        return bufferCode
    else:
        print(f"'{bufferCode}' is not a legal code command, please type again! ")
        return getCode(yourInputMsg)

def main():
    #the main function is to let the user to input their parameters and 
    f1Numer = getNumber("Fraction 1 numerator: ")
    f1Deno = getNumber("Fraction 1 denominator: ")
    f1 = Fraction(f1Numer,f1Deno)
    code = getCode("Operation (+, -, *, /, ==): ")
    f2Numer = getNumber("Fraction 2 numerator: ")
    f2Deno = getNumber("Fraction 2 denominator: ")
    f2 = Fraction(f2Numer,f2Deno)
    
    if code == '+':
        finalF = f1 + f2
    elif code == '-':
        finalF = f1 - f2
    elif code == '*':
        finalF = f1 * f2
    elif code == '/':
        finalF = f1 / f2   
    elif code == '==':
        finalF = f1 == f2
    print(f"{f1} {code} {f2} = {finalF}")

if __name__ == '__main__':
    #main()
    ut.main(exit=False, verbosity=2)    

"""
    #testing part    
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")
"""
    