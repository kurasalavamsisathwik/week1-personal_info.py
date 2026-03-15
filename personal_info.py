# My name is Vamsi
# This is my first basic program developed as of my first week task
# My information
name = "Vamsi"
age = 18
hobby = "surfing net"
# welocome message 
print("=" * 40)
print("WELCOME TO THE PROGRAM")
print("=" * 40)
# printing my personal information
print("My name is",str(name))
print("My age is",str(age))
print("My hobby is",str(hobby))

# Taking inputs from the user
Name = input("Enter your name: ")
print("Hello", Name)

# Ask for favorite food
food = input("What is your favorite food? ")
# used while to ensure no empty input
while food.strip() == "":
    print("Please enter your favorite food.")
    food = input("What is your favorite food? ")

# Ask for favorite color
color = input("What is your favorite color? ")
# used while loop to ensure no empty input
while color.strip() == "":
    print("Please enter your favorite color.")
    color = input("What is your favorite color? ")

print("Your favorite food is:", food)
print("Your favorite color is:", color)
print("those are the best picks")
# to display info using f strings and seperators
print("Apple","orange","mango",sep=",")
car = B M W
print(f "my favorite car is{car}")
# to display age in months
age = int(input("enter your age :"))
age_in_months = age * 12
print("your age in months is ",age_in_months)
# good bye message
print("=" * 40)
print("THANKS FOR REVIEWING THE PROGRAM")
print("=" * 40)



