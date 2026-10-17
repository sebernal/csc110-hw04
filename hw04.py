# ------------------------------------------------------
#        Name: (Sophia Bernal)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This function recieves a string from the user and checks if it contains dog, Dog, or the secret word"""
#collecting input from user
    user_in = input("Give me a sentence: ")
#Force starting a while loop
    while True:
#Checking first condition, if input includes dog or Dog 
        if "dog" in user_in or "Dog" in user_in:
            print("You used the word \"dog\" or the word \"Dog\"!")
#If user input satisfies this condition end loop
            break
#If first condition not met check for second condition 
        elif secret_word in user_in:
            print("You used the secret word!")
#If secret word condition met end loop
            break
#If neither conditions are met continue the loop
        else:
            print("Try again")
            user_in = input("Give me a sentence: ")

# Task 2
def check_greater():
    """ recieves two inputs and determines which number is greater """
#Get two numbers from user
    a = input("Give me a first integer: ")
    b = input("Give me a second integer: ")
#Use a while loop to continue getting input until numbers are not equal
    while a==b:
        print("Try again")
        a = input("Give me a first integer: ")
        b = input("Give me a second integer: ")
#Check if the first value is greater
    if a>b:
        print("First is Greater")
#Check if the second value is greater
    elif b>a:
        print("Second is Greater")


# Task 3
def get_special_numbers():
    """ prints the numbers in specified range that meet all conditions"""
#Use a for loop that checks each number between 1 and 41
    for num in range(1,41):
#Check that the number is odd
        if num%2==1:
#Check that the numer is a multiple of 3
            if num%3==0:
#Check that the number is not a multiple of 5
                if num%5!=0:
                    print(num)


# Task 4.a
def my_for_loop():
    """takes string from user and determines whether each variable is a vowel or consonant"""
#Get input from user
    user_str = input("Give me a string: ")
#find length of the string
    length = len(user_str)
#Check that the string length is between 2 and 5 and that there is no space
    if not 2<=length<=5 or " " in user_str:
        print("bad word")
        return
    else:
#use enumerate to assign an index to each element in the string
        for i,ch in enumerate(user_str):
            letter = ch
#check if the letter is a vowel
            if letter in "aeiou" or letter in "AEIOU":  
                print(f"letter {letter} is a vowel")
#If the letter is not a vowel print that it is a consonant 
            else:
                 print(f"letter {letter} is a consonant")

        
              

# Task 4.b
def my_while_loop():
    """ User input determines whether the loop is continued or exited and what is printed """
#Start the loop
    while True :
#get input from user
        option_picked = input("Choose one option: a, b, or c: ")
#check if user picked a
        if option_picked == 'a':
            continue
#check if user picked b
        if option_picked == 'b':
            print("Goodbye")
            return
#check if user picked c
        if option_picked == 'c':
            exit()
#If user did not pick a, b, or c, print try again and restart the loop
        else:
            print("try again") 
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
