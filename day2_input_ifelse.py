name = input("write your name")
salary = int(input("write your salary in Euro"))
if salary >= 2000:
    print("Great!")
else:
    print("Keep Building")


name = input("Write your name: ")
salary = int(input("Write your salary in Euro: "))

if salary > 2000:
    print(f"Great, {name}! You are above the Munich average entry salary.")
else:
    print(f"Keep building your skills, {name} — your salary will grow!")