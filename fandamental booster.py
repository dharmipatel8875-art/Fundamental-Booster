print("Welcome to the Interactive Personal Data collector!")

name = input("please enter your name: ")
age = int(input("please enter your age: "))
height = float(input("please enter your height in meeters: "))
favourite_number = int(input("please enter your favouritenumber "))


print("Thank you! Here is the information we collected: ")

print("Name:", name, ("Type:", type(name),"Memory Address:",id(name)))
print("Age:", age, ("Type:", type(age),"Memory Address:",id(age)))
print("Height:", height, ("Type:", type(height),"Memory Address:",id(height)))
print("Favourite Number:", favourite_number, ("Type:", type(favourite_number),"Memory Address:",id(favourite_number)))


current_year = 2026
birth_year = current_year - int(age)
print("Your birth year is approximatately: ", birth_year, "(based on your age of", age,")")
print("Thank you for using the personal Data collector, Goodbye")


