##########################################################################################
#  Problem Statement No. 02 :    
#  Write a program which accept one number and display below pattern.
#  Input  : 5
#  Output : * * * * * 
#           * * * * * 
#           * * * * * 
#           * * * * * 
#           * * * * * 
#########################################################################################



def main():
    print("Enter Number : ")
    Number = int(input())

    for i in range(Number):
        for i in range(Number):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    main()