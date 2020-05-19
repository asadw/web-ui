from passlib.hash import pbkdf2_sha256
import sys
import getopt

P_FILE = "passwords.txt"

def encrypt(user_input):
    """
        write encrypted password to file
    """
    encrypted_pass = pbkdf2_sha256.hash(user_input)
    with open(P_FILE, "w") as f:
        f.write(encrypted_pass)


if __name__ == "__main__":
    user_input = sys.argv[1]
    encrypt(user_input)
