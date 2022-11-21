import secrets
import string
import clipboard as cb
import argparse

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation
all_chars = lower_chars + upper_chars + special_chars + digits

parser = argparse.ArgumentParser(
    prog="PROG",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
        Generate a secure random password with the following minimum requirement:
            * 1 lowercase character
            * 1 uppercase character
            * 1 special character
            * 1 digit
            * does not begin with a digit or special character"
            * must at least 6 characters in length
        '''
)
parser.add_argument("-l", "--length", type=int, default=8,
                    help="length of password to be generated. If not provided, default is 8.")
args = parser.parse_args()
password_length = args.length


def generate_password():
    while True:
        if password_length < 6:
            print("Password length is too short")
            exit()

        first_char = secrets.choice(string.ascii_letters)
        rest_of_chars = ""

        for _ in range(password_length - 1):
            rest_of_chars += "".join(secrets.choice(all_chars))

        password = first_char + rest_of_chars

        if (any(char in special_chars for char in password) and any(char in lower_chars for char in password) and any(char in upper_chars for char in password) and any(digit in digits for digit in password)):
            break

    print(f"🔑 {password}")
    cb.copy(password)
    print("📋 Password copied to your clipboard!")


def main():
    generate_password()


if __name__ == '__main__':
    main()
