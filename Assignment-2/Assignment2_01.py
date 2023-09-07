##########################################################################################
#  Problem Statement No. 01 :    
#  Create one module named as Arithmetic which contains 4 function as Add() for addition, 
#  sub() for subtraction, Mult() for multiplication and Div() for division. All functions 
#  accept two parameters as number and perform the operatin. Write one python program which 
#  call all the functions from Arithmetic module by accepting the parameter from user.
#########################################################################################

import Arithmetic

def main():
    print("Enter Two Numbers : ")
    No1 = int(input())
    No2 = int(input())

    print("=========================")
    Result = Arithmetic.Add(No1,No2)
    print("Addition        : ", Result)

    Result = Arithmetic.Sub(No1,No2)
    print("Subtraction     : ",Result)

    Result = Arithmetic.Mult(No1,No2)
    print("Multiplication  : ",Result)

    Result = Arithmetic.Div(No1,No2)
    print("Division        : ",Result)
    print("=========================")


if __name__ == "__main__":
    main()