##########################################################################################
#  Problem Statement No. 09 :    
#  Write a program which accept one number from user and return the number of digits in that number
#  Input  : 5187934
#  Output :  7 
#########################################################################################

def CheckCount(No):
    Count = 0
    while No != 0:
        No = No // 10
        Count = Count + 1
        #print(Count)

    return Count




def main():
    print("Enter Number : ")
    Number = int(input())
    Result = CheckCount(Number)
    print(Result)

if __name__ == "__main__":
    main()