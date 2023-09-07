##########################################################################################
#  Problem Statement No. 06 :    
#  Write a program which accept one number and print below pattern
#  Input  : 5
#  Output :  * * * * *
#            * * * *
#            * * * 
#            * * 
#            *
#########################################################################################

def main():
    print("Enter Number : ")
    Number = int(input())

    for i in range(Number,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()
        

if __name__ == "__main__":
    main()