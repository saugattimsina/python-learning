
# when someone calls this function they will use ask_name() to call this 
# request name and returns name
def ask_name():
    name = input("enter your name")
    return name
# when someone calls this function they will use ask_location() to call this 
# request location and returns location
def ask_location():
    location = input("enter your location")
    return location

#this function recives name and location from ask_name() and ask_location()  and 
# called using concat_and_return(name returned from ask_name() and location from ask_location() )
# concats both information with other texts and return to function call concat_and_return()

def concat_and_return(name,location):
    output_string = f'\n\ngreetings everyone,\n \ti am {name} \n \tand i am from {location}'
    return output_string
def main():
    name = ask_name() # calls ask_name() function and recives name inputed by user in variable name
    location = ask_location() # calls ask_location() function and recives location inputed by user in variable location
    my_informations = concat_and_return(name,location) # sends both name and location to concat_and_return() finction
    print(my_informations) # print my information returnrd from concat_and_return function

if __name__ == "__main__":
    main()