##########################################################################################
#  Problem Statement No. 03 :    
#  Write a program which accept one number from user and return its factorial
#  Input  : 5
#  Output : 120
#########################################################################################

def main():
    fact = 1
    print("Enter Number : ")
    Number = int(input())

    if Number < 0:
        print("Negative Number !")
    elif Number == 0:
        print("Factorial : 1")
    else:
        for i in range(1,Number+1):
            fact = fact * i
    print("Factorial : ",fact)

if __name__ == "__main__":
    main()