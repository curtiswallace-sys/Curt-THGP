name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your grade in the class?")
print(f"Your grade is {fav1}")

number = int(fav1)
if number >= 90:
    print("A")
elif number >= 80:
    print("B")
elif number >= 70:
    print("C")
elif number >= 60:
    print("D")      
else:
    print("F")
