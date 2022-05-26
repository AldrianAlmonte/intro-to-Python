# this is a comment
name = "Aldrian"
last_name = "Almonte"
age = 101
weight = 230
happy = True  # False
something = []

print("Hello World!")
print(age+1)
print(name)
print(name*3)
# print(name+1)
print(name+last_name)
print(name+" " + last_name)
print(f"{name} {last_name}")


def say_hello():
    print("Hi!!")


say_hello()

if (age < 100):
    print("Don't worry you're still young")

elif(age == 100):
    print("congrats on the century")
else:
    print("youre getting old")
