# The application of lesson to guessing program
# Mechanics: The program will generate random number from 0 to 100 then the user will guess
# If the given value of the user is less than the generated value print less than
# If the given value of the user is greater than the generate value print greater than
# If the given value of the user is the same with the hidden value print guessed correctly


# Making command to continue
print("To run the guessing program press ""Y"" to continue or ""N"" to exit the program")  

response = input("Response: ")
if response == ("Y"):
    print("Continue to the program")
elif response == ("N"):
    print("Okay,then rest")
    raise SystemExit
elif response != "Y" or "N":
    print("Put Valid Value")
    raise SystemExit

# Coding while loop for loop back
while True:

 import random
# Program for random number
 hidden_val = random.randint(0,100)
# print hidden_val turn is a comment to hide the generated value to show it just remove the # in the line and put the # back to hide it

#  print(hidden_val)  




