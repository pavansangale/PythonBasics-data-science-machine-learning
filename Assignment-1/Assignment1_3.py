##########################################################################################
#  Problem Statement No. 3 :    
# Write a program which contains one function as Add() which accepts two numbers from user 
# return addition of that two numbers.
#------------------------------------------------------------------------------------------
# Input : 11 5      Output : 16
#########################################################################################


def Add(Number1, Number2):
    Answer = Number1 + Number2
    return Answer

def main():
    print("Enter Number : ")
    Value1 = int(input())
    Value2 = int(input())
    Result = Add(Value1,Value2)
    print(Result)
    
if __name__ == "__main__":
    main()
