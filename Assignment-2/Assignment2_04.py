##########################################################################################
#  Problem Statement No. 04 :    
#  Write a program which accept one number from user and return addition of its factors
#  Input  : 12
#  Output : 16
#########################################################################################

def AdditionOfFactors(No):
    Sum = 0
    for i in range(1,No,1):
        if No % i == 0:
            Sum = Sum + i
            print(i)
            
            
    return Sum

def main():
    print("Enter Number : ")
    Number = int(input())
    Result = AdditionOfFactors(Number)
    print(Result)

if __name__ == "__main__":
    main()
