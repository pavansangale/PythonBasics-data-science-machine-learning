##########################################################################################
#  Problem Statement No. 2 :    
#  Write a program which contains one function named as ChkNum() which accept one parameter as number. 
#  If number is even then it should display "Even Number"  otherwise display "Odd Number
#------------------------------------------------------------------------------------------
# Input : 11      Output : Odd Number 
# Input : 8       Output : Even Number 
#########################################################################################


def ChkNum(Number):
    if(Number % 2 == 0):
        print("Enven Number")
    else:
        print("Odd Number")

def main():
    print("Enter Number : ")
    Value = int(input())
    ChkNum(Value)
    
if __name__ == "__main__":
    main()
