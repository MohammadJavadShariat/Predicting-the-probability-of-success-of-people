# Getting_Up_Early
# If a letter or a number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Getting_Up_Early1= input("Give your early morning a score from 0 to 100 🤤:")
     if Getting_Up_Early1.isdigit() == True :
         Getting_Up_Early = int(Getting_Up_Early1)
         if Getting_Up_Early in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")

# Interest
#If a letter or a number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Interest1 = input("Give your interest a score from 0 to 100 🤩:")
     if Interest1.isdigit() == True :
         Interest = int(Interest1)
         if Interest in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Diligence
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Diligence1 = input("Give your hard work a score from 0 to 100 🤯:")
     if Diligence1.isdigit() == True :
         Diligence = int(Diligence1)
         if Diligence in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Interest_in_Learning
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Interest_in_Learning1 = input("Rate your interest in learning from 0 to 100 😍:")
     if Interest_in_Learning1.isdigit() == True :
         Interest_in_Learning = int(Interest_in_Learning1)
         if Interest_in_Learning in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Study
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Study1 = input("Give your study a score from 0 to 100 📚:")
     if Study1.isdigit() == True :
         Study = int(Study1)
         if Study in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Sport
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Sport1 = input("Give your sport a score from 0 to 100 ⚽🏓:")
     if Sport1.isdigit() == True :
         Sport = int(Sport1)
         if Sport in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Coffee_food
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Coffee_food1 = input("Give your coffee and healthy food a score from 0 to 100 ☕🍗:")
     if Coffee_food1.isdigit() == True :
         Coffee_food = int(Coffee_food1)
         if Coffee_food in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
# Sleep
#If a letter or number other than 0 to 100 is entered, the question will be asked again.
while (True) :
     Sleep1 = input("Give a score from 0 to 100 to the adequacy of your sleep 😴:")
     if Sleep1.isdigit() == True :
         Sleep = int(Sleep1)
         if Sleep in range(0 , 101) :
             break
         else:
             print("Please enter a number between 0 and 100.")
     else:
         print("Please enter a number between 0 and 100.")
         
def Success(Getting_Up_Early=0, Interest=0, Diligence=0, Interest_in_Learning=0, Study=0, Sport=0, Coffee_food=0, Sleep=0): 
    """
    With the help of this function, you can estimate the percentage of your career or academic success.
    For this, it is enough to put a number between 0 and 100 for each function parameter, which indicates the percentage of doing that job or having that feature.
    Obviously, if you don't pass a number for the function parameters, the default number zero will be substituted for each one.
    """

    x = round((Getting_Up_Early + 2*Interest + 3*Diligence + 4*Interest_in_Learning + 2*Study + 2*Sport + 4*Coffee_food + 2*Sleep)/20 , 2)   
    return x

all_Success = Success(Getting_Up_Early, Interest, Diligence, Interest_in_Learning, Study, Sport, Coffee_food, Sleep)

if all_Success >= 80 :
    print("\nCongratulations!🥳")
elif all_Success >= 50 and all_Success < 80 :
    print("\nGood, but try harder.😊")
elif all_Success >= 30 and all_Success < 50 : 
    print("\nWork harder to have a better future. 😉")
elif all_Success >= 0 and all_Success < 30 : 
    print("\nWow! You are in a critical situation! 😱 If you want to have a good future, you have to work harder.")

print(f"Based on your data and our statistics-based prediction, you will succeed %{all_Success} in the future.")
print("Of course, this percentage is not necessarily correct because some characteristics such as your mood, poverty, destiny, God's will, etc. can affect your success percentage.😊")
    








