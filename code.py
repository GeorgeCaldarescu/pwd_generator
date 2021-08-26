import string
import random

# create the variable that contains the characters used for the password

alphabet = list(string.ascii_letters)
numbers = list(string.digits)
specials = list("!@#$%^&*()")  # create the list with the special characters. pay attention because sometimes some characters are not allowed
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# create the function

def generate():
    # define the lenght by input
    length = int(input("Lenght of the password:" ))

    # define how many characters of each class you want
    alpha_count = int(input("How many letter you want: "))
    numbers_count = int(input("HOw many numbers you want: "))
    specials_count = int(input("How many specials characters you want: "))

    characters_count = alpha_count + numbers_count + specials_count

    if characters_count > length:
        print("The total of characters is bigger than the lenght you choose for the password")
        return


    # start to create the password
    password = []

    # take ramdom characters for letters, numbers and special charachters
    for i in range(alpha_count):
        password.append(random.choice(alphabet))

    for i in range(numbers_count):
        password.append(random.choice(numbers))
    
    for i in range(specials_count):
        password.append(random.choice(specials))

    # create a if statement to pick some random characters if the password lenght is less the lenght choosed at the beginning to make it the same
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))
    
    # shuffle the characters
    random.shuffle(password)

    # convert the list to string
    print("".join(password))

generate()