##########################################################################################
#  Problem Statement No. 6 :    
#  Write a program which accept number from user and check whether that number is positive 
#  or negative or Zero
#------------------------------------------------------------------------------------------
 #    Input : 11     Output : Positive Number
 #    Input : -8     Output : Negative Number
 #    Input :  0     Output : Zero
#########################################################################################


def main():
    print("Enter Number : ")
    Number = int(input())

    if(Number > 0):
        print("Positive Number")
    elif(Number < 0):
        print("Negative Number")
    else:
        print("Zero")

if __name__ == "__main__":
    main()
