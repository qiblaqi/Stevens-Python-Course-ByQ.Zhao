"""
This is a program intend to

Written by Marta
"""
import unittest as ut 

class ThreeNumber:
    """ """
    def __init__(self,numb0,numb1,numb2):
        #initialize the class and give the three values
        self.numb0 = int(numb0)
        self.numb1 = int(numb1)
        self.numb2 = int(numb2)
            


    
    def maxOfThree(self):
        #compare two of the values and then compare the last number with bigger number
        if (self.numb0 < self.numb1):
            maxTwo = self.numb1
        else:
            maxTwo = self.numb0
        if (self.numb2 > maxTwo):
            return self.numb2
        else:
            return maxTwo

def testSuite():
    print("Testing: ")
    for i,j,k in [[1,2,3],[3,2,1],[2,1,3],[1,1,3],['a','b','c']]:
         try:
             usr3 = ThreeNumber(i,j,k)
             print(f"The maximum of {i} {j} {k} is {usr3.maxOfThree()}")
         except ValueError:
             print(f"'{i}' '{j}' '{k}' is not vailid number, please input numbers ")
    print("Test End! ")




def getNumber(Msg):
    #make sure to get the 
    temp = input(Msg)
    try:
        number = int(temp)
    except ValueError:
        print(f"'{temp}' is not a number,please input a number! ")
        number = getNumber(Msg)
    return number

def main():
    #get the users input and 
    usrNumb0 = getNumber("Enter first value: ")
    usrNumb1 = getNumber("Enter second value: ")
    usrNumb2 = getNumber("Enter third value: ")
    usr3 = ThreeNumber(usrNumb0,usrNumb1,usrNumb2)
    print(f"The maximum of {usrNumb0} {usrNumb1} {usrNumb2} is {usr3.maxOfThree()}")

if __name__ == '__main__':
    testSuite()
    main()
    
    