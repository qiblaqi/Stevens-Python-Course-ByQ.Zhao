"""
this is a program use Class to handle two Fractions plus, minus, mutiply, divide and
check-out if they equals to each other

123131321
Written by Qi Zhao
"""

class Fraction:
    """ Fraction class hold numerator and dorminator with method to do + - * / == with each other """
    def __init__(self,numerator, denominator):
        """ This initiates the """
        if denominator == 0:
            raise ValueError("denominator cant be '0' !")
        self.numerator = numerator
        self.denominator = denominator
    
    def plus(self,other):
        #
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.denominator + other.numerator * self.denominator
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction
    
    def minus(self,other):
        #
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.denominator - other.numerator * self.denominator
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def times(self,other):
        #
        newFractionDeno = self.denominator * other.denominator
        newFractionNumer = self.numerator * other.numerator 
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def divide(self,other):
        #to reverse the fraction and multiply
        newFractionDeno = self.denominator * other.numerator
        newFractionNumer = self.numerator * other.denominator 
        newFraction = Fraction(newFractionNumer,newFractionDeno)
        return newFraction

    def equal(self,other):
        #
        newFractionNumer = self.numerator * other.denominator - other.numerator * self.denominator
        if newFractionNumer == 0:
            return True
        else:
            return False
    
    def __str__(self):
        #
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
        finalF = f1.plus(f2)
    elif code == '-':
        finalF = f1.divide(f2)
    elif code == '*':
        finalF = f1.times(f2)
    elif code == '/':
        finalF = f1.divide(f2)
    elif code == '==':
        f1.equal(f2)
    print(f"{f1} {code} {f2} = {finalF}")
   
    #testing part    
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")

if __name__ == '__main__':
    main()    


    