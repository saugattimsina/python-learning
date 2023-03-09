# function is the block of code which does some specific taask 
# predefined function
'''
example:
print() #used to print the output
input() # used to read the data
'''

# user defined function
'''
previously :
name = input("enter your name")
print(name)
last_name = input("enter your last_name")
print(last_name)

using function the abobe code can be done repetidely and properly 
example :
def ask_name():
    name = input("enter your name")
    print(name)

as many time you called the function name will be asked and output will be your input
you can call ask_name() to use the function above


example :
parameters: 
if any variable is inside the paranthesis or small bracket that are parameters
parameters are seperated by commas
example 
def check_parameters(name,roll_number):
    print(name)
    print(roll_number)

      where name and roll_number are the parameter 
parameters are the information that has to be passed to use the function 
to call the  we will do check_parameter(2,3)


functions can aslo take any number of parameters as per the need
def check_parameters(n1,n2,n3,n4,..,nn):
    sum_of_numbers = n1+n2+n3+n4+...+nn


function can return the data to the place where the function is called
    example
    def check_parameters(n1,n2,n3,n4,..,nn):
        sum_of_numbers = n1+n2+n3+n4+...+nn
        return sum_of_numbers
    
    to recive the sum of numbers
    sum_of_numbers = check_parameters(1,2,3,4,...,n)
    print(sum_of_numbers) here the sum of numbers are recived
'''