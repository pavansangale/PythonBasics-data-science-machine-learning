##########################################################################################
#  Problem Statement No. 7 :    
#  Write a program which contains one function that accept one number from user and returns 
# true if nubmer is divisible by 5 otherwise retur fale
#------------------------------------------------------------------------------------------
 #    Input : 8     Output : False
 #    Input : 25    Output : True
#########################################################################################

def ChKDivByFive(Number):
    remainder = Number % 10

    if(remainder == 0 | remainder == 5 ):
        return True
    else:
        return False

def main():
    print("Enter Number : ")
    Value = int(input())

    Result = ChKDivByFive(Value)
    print(Result)

if __name__ == "__main__":
    main()
