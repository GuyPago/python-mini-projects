import math
math.sqrt(2)

x = 0

while True:
    user_input = input("enter any key to print(enter 'q' to quit):\n",)
    if user_input == "q":
        print("ending program...bye!\n\n\n")
        break
    else:
        print("user input was",user_input)
        print("the value of",user_input,"in ASCII is",str(ord(user_input)),"\n\n\n")
