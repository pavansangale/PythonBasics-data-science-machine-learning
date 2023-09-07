##########################################################################################
#  Problem Statement No. 08 :    
#  Write a program which accept one number and print below pattern
#  Input  : 5
#  Output :  1 
#            1 2 
#            1 2 3 
#            1 2 3 4 
#            1 2 3 4 5 
#########################################################################################

def main():
    print("Enter Number : ")
    Number = int(input())

    for i in range(Number+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

if __name__ == "__main__":
    main()