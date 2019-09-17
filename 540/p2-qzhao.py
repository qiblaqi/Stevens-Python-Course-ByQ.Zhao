"""
This is a program intend to convert numeric scores into grades.
The program can identify valid and legal inputs (scores range in 0 to 100) and remind users to input valid inputs.

Written by Qi Zhao
"""

def validScores(yourMsg):
    #get the valid input scores 
    try:
        scores = float(yourMsg)
    except ValueError:
        print(f"{yourMsg} is not a valid number, please input a number ranged in 0 to 100! ")
        return False
    if scores >= 0.0 and scores <= 100.0:
        return True
    else:
        print(f"{yourMsg} is not a legal scores number, please input a number ranged in 0 to 100! ")
        return False


def getGrades(yourScores):
    #convert the numeric scores into the grades

    if yourScores <= 100.0 and yourScores >= 93.0:
        return "A"
    elif yourScores < 93.0 and yourScores >= 90.0:
        return "A-"
    elif yourScores < 90.0 and yourScores >= 87.0:
        return "B+"
    elif yourScores < 87.0 and yourScores >= 83.0:
        return "B"
    elif yourScores < 83.0 and yourScores >= 80.0:
        return "B-"
    elif yourScores < 80.0 and yourScores >= 70.0:
        return "C"
    elif yourScores < 70.0 and yourScores >= 0.0:
        return "F"


def testSuite(testInputs):
    #create a testing case.
    print("----------TEST INFORMATION----------")
    for testItem in testInputs:
        if validScores(testItem):
            print(f"Your score is {testItem}, the grade is '{getGrades(float(testItem))}' ")
    print("-------------TEST END! -------------")



def main():
    #get the usr inputs and tell them the acutal grade or warning info 
    testInputs = [100, 93, 92.99, 90, 89.9, 87, 83, 80, 75, 69, 'eighty', -1, 101]
    usrInput = input("Please input your scores: ")
    if validScores(usrInput):
        print(f"Your score is {usrInput}, the grade is '{getGrades(float(usrInput))}' ")
    print(" ")
    testSuite(testInputs)



if __name__ == '__main__':
    main()