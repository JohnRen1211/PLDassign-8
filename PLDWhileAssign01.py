# The application of lesson to the lottery program
# Mechanics: The program will generate random number 3 from 0 to 100 then show it
# The program will ask to run until the 3 values are the same to show Winner for the user


#Making command to continue
print("To run the lottery press ""Y"" or ""N"" to exit the program")  

response = input("Response: ")
if response == ("Y"):
    print("Continue to the survey")
elif response == ("N"):
    print("Okay,then rest")
    raise SystemExit
elif response != "Y" or "N":
    print("Put Valid Value")
    raise SystemExit

# Program for while loop back
while True:
