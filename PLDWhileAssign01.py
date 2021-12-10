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

# Program for 3 random numbers input Wonderful Program Wonderful Program
 import random
 def lottery_pick():
     for numbers  in enumerate(range(3)):
        ran_num1 = random.randint(0,9)
        ran_num2 = random.randint(0,9)
        ran_num3 = random.randint(0,9)
        return ran_num1, ran_num2, ran_num3

 def display(ran_num1, ran_num2, ran_num3):
    print(f"The lottery number combination are: {ran_num1}, {ran_num2}, {ran_num3}")
 ran_num1, ran_num2, ran_num3 =lottery_pick()
 display(ran_num1, ran_num2, ran_num3)


 if (ran_num1 == ran_num2 and ran_num1 == ran_num3):
    print ("Congratulation Winner")
    print("The program successfully processed")
    raise SystemExit
 elif (ran_num1 != ran_num2 and ran_num3):
    print("Opps Loss Try again for more chance of winning lottery")

 restart=input("Restart the program enter Y to reset or N to exit: ")
 