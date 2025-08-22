def make_card(name, age, message = "Have a good day"):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return f"Hello {name.title()} ({age} years old)\n{message}!\n"
