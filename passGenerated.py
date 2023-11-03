import random
import string

def generate_password(length=30):

    # define the character pool for the password
    GP = string.ascii_letters + string.digits + string.punctuation

    # make sure the password contains at least one letter, one digit, and one special character
    password = []
    password.append(random.choice(string.ascii_letters))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    # fill the rest of the password with random characters from the pool
    for i in range(length - 3):
        password.append(random.choice(GP))

    # shuffle the characters in the password to ensure randomness
    random.shuffle(password)

    # convert the list of characters into a string and return it
    return ''.join(password)


# testing usage
password = generate_password(30)
print("Generated password: ", password)
