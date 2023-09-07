##########################################################################################
#  Problem Statement No. 10 :    
#  Write a program which accept one number from user and return the additon of the digits of the number
#  Input  : 5187934
#  Output : 37 
#########################################################################################

def SumOfDigits(No):
    Count = 0
    Sum = 0
    while No > 0:
        lastDigit = No % 10   
        Sum = Sum + lastDigit      
        No = No // 10

    return Sum




def main():
    print("Enter Number : ")
    Number = int(input())
    Result = SumOfDigits(Number)
    print(Result)

if __name__ == "__main__":
    main()