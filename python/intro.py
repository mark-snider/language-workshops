#########################################################
# A quick intro to basic CS concepts and terminology
# using Python
#########################################################

# variables
customer1 = "John Smith"
customer2 = "Beth Jones"

# an array/list data structure
customers = [customer1, customer2]

# using built-in Python print function
print(customer1)

# using built-in Python String functions
print(customer2.lower())

print(customer1.split(" ")[0] + " " + customer2.split(" ")[1])


# creating a custom function
def printGreeting(fullname):
    print("Hello %s! What are you looking for?\n" % (fullname))


# invoking a custom function
printGreeting("Henry Smalls")

# looping
for customer in customers:
    printGreeting(customer)


# using conditionals and casting int to string
def printValue(value):
    # cast an int to a string
    strValue = str(value)

    # conditional a.k.a if...then, else if...then, else
    if value < 5:
        print("Low: " + strValue)
    elif value >= 5 and value < 10:
        print("Medium: " + strValue)
    else:
        print("High " + strValue)


for x in range(15):
    printValue(x)
