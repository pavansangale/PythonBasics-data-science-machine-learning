##########################################################################################
#  Problem Statement No. 05 :    
#  Write a program which accept one number from user and check whether number is prime or not
#  Input  : 5
#  Output : It is prime number
#########################################################################################


def CheckPrime(No):
    Flag = False
    for i in range(2,No,1):
        if No % i == 0:
            Flag = True
            break
    if Flag == False:
        print("Number is prime")
    else: 
        print("Number is not prime")
        


def main():
    print("Enter Number : ")
    Number = int(input())
    if Number == 1:
        print("Number is not prime")
    elif Number > 1:
        CheckPrime(Number)

if __name__ == "__main__":
    main()
