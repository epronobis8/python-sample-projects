#creating our addition function

def addition(a, b):
    return a + b

# All code is contained inside the main function
def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter you 2nd number:\n'))

    #Calling our function
    result = addition(num1, num2)
    print('The results is', result)

#still need to call main after the functions are declared
main()
