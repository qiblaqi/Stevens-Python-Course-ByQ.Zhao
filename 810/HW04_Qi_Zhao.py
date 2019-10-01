"""
this is a program contains function takes a string as an argument and returns the number of vowels
last_occurrence, which return the index (offset from 0) of the last occurrence of the target item 
and Simplfy the Fraction class
Written by Qi Zhao 
"""


def count_vowels(seq):
    #count the vowels in the input sequnce
    lowSeq = seq.lower()
    countVow = 0
    for i in lowSeq:
        if i in ['a','e','i','o','u']:
            countVow += 1
    return countVow

def last_occurrence(target,sequnce):
    #using for loop to check out every item in the sequence and return the offset 
    offsetSeq = []
    offset = 0
    for item in sequnce:
        if item == target:
            offsetSeq.append(offset)
        offset += 1 
    if offsetSeq.__le__ != 0:
        return max(offsetSeq)
    else:
        return None
def my_enumerate(seq):
    #use generator to create my enumerate function 
    cnt = 0
    for i in seq:
        yield cnt,i
        cnt += 1


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
        if self.denominator*other.denominator>0:
            return (self.numerator*other.denominator-self.denominator*other.numerator)<0
        elif self.denominator*other.denominator<0:
            return (self.numerator*other.denominator-self.denominator*other.numerator)>0
         
        
    def __gt__(self,other):
        #check self fraction is greater than other fraction
        if self.denominator*other.denominator>0:
            return (self.numerator*other.denominator-self.denominator*other.numerator)>0
        elif self.denominator*other.denominator<0:
            return (self.numerator*other.denominator-self.denominator*other.numerator)<0
    
    def __ge__(self,other):
        #check self >= other with using __lt__ function
        return not(self<other)
    
    def __le__(self,other):
        #check self <= other with using __gt__ function
        return not(self>other)

    def __str__(self):
        #output the fraction in a mathmetics way like '1/2' for f12
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        #find the GCF of the fraction and return the new simplified fraction 
        start = min(abs(self.numerator),abs(self.denominator))
        for gcf in range(start,1,-1):
            if self.numerator % gcf == 0 and self.denominator % gcf == 0:
                return Fraction(self.numerator/gcf,self.denominator/gcf)
        return self