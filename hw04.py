# ------------------------------------------------------
#        Name: (Sophia Bernal)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Add your docstring """
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
    """ Add your docstring """
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
    """ Add your docstring """
    for num in range(1,41):
        if num%2==1:
            if num%3==0:
                if num%5!=0:
                    print(num)


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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
