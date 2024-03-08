# A simple program that greets the user, and asks if the user is good

user_name = input("Please enter your name: ")
print(f"Hello {user_name}!")
user_input = input("Are you all good today? Y/N: ")
if user_input.upper() == "Y":
  print("I'm glad to hear that!")
elif user_input.upper() == "N":
  print("Sorry to hear that, hope it gets better.")
else:
  print("What did you say?")
