##########################################################################################
#  Problem Statement No. 07 :    
#  Write a program which accept one number and print below pattern
#  Input  : 5
#  Output :  1 2 3 4 5 
#            1 2 3 4 5 
#            1 2 3 4 5 
#            1 2 3 4 5 
#            1 2 3 4 5 
#########################################################################################

def main():
    print("Enter Number : ")
    Number = int(input())

    for i in range(Number):
        for j in range(Number):
            print(j+1,end=" ")
        print()

if __name__ == "__main__":
    main()