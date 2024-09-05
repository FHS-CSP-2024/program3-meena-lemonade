# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers



## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your Name? ")
#print(name)
#print(Name)
#CASING AND SPELLING IN VARIABLES IS IMPORTANT!!


# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
name = "Violin" #this is a string
number = -100 #this is a number
Numberr = "100" #this is a string

print (number/2)
#casting example
print (int(Numberr)/2)

myfloat = 3.567
print (int(myfloat/2))


# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
num1=75
num2=68
num3=1492
avg = (str((num1+num2+num3)/3))

print ("Average = " + avg)
print ("Average = " + (avg))
print ("Average = ", avg)
print (f"Average = {avg}")

beds = 5
bath = 3.75
address = "9876 Cool Ln"
city = "Folsom"
zip = 95630
sale = 1,000,000

print (f"House for sale at {address} in {city}, {zip}.")
print (f"There are {beds} beds and {bath} bathrooms.")
print (f"House costs ${sale}.")

# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \
print ("I have a file located at: C:\\andthen\\therestofit")