def personDetails():
    name = input("Enter your name: ").upper()
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    country = input("Enter your country: ").capitalize()

    return f"Hello {name}\nYou are {age} years old.\nYour height is {height:.2f} feet.\nYou are from {country}.\nYour nickname is {name[0:2]}{name[-2:]}."


print(personDetails())