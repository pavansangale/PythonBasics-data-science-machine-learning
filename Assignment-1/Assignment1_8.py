##########################################################################################
#  Problem Statement No. 8 :    
#  Write a program which accepts number from user and print that number of "*" on screen
#------------------------------------------------------------------------------------------
 #    Input : 5     Output : * * * * * 
#########################################################################################



def main():
    print("Enter Number : ")
    Value = int(input())

    for i in range(0,Value,1):
        print("*",end=" ")

if __name__ == "__main__":
    main()
