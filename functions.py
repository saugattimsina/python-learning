
# function

# basic function call
# function which doesnot accepts parameters and doesnot return values
def basic_function():
    print("hello world")

# function that accepts parameters and doesnot return value
def function_with_parameter(test_number,members):
    # print(test_number)
    my_cut = test_number/members
    print(my_cut)

# print(test_number)

# accepts parametes and returns data
def add_all_the_money(numbers):
    # print(numbers)
    all_money_sumed = 1
    for i in numbers:
        all_money_sumed += i
    # print(all_number_multiplied) 
    return all_money_sumed  




# main function (self invoking function)
if __name__ == "__main__":
    basic_function()
    all_nums = add_all_the_money([300,500,696,7000])
    function_with_parameter(all_nums,4)

