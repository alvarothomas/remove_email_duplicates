"""
This script generates a text file with as many email addresses as
the number passed in as argument. The file contains 50% randomly
placed duplicates except if only one email is desired.
"""

import sys
import os
import random

emails_file = "./email_addresses.txt"   # text file to store email addresses
emails_list = []                        # list of email addresses
num_emails = int                        # number or email addresses
# NOTE: data should be stored and in an external configuration file


def get_num_emails(input_number):
    """
    Reads how many email addresses are going to be generated as an argument

     Parameters
    ----------
    input_number
        number of email addresses to be read
    """
    # Ask the user for a number of email addresses to generate
    # NOTE: more input number checking could be added

    if not type(int(sys.argv[1])) is int:
        raise TypeError("Only integers are allowed")
    elif (int(sys.argv[1]) < 1):
        raise Exception("Sorry, no numbers below one")
    else:
        try:
            input_number = int(sys.argv[1])
            return input_number
        except ValueError:
            print("The input was not a valid integer")


def generate_emails_list(num, dest_list):
    """
    Generates a list with as many fake email addresses as given by 'num'

    Parameters
    ----------
    num
        Number of desired email addresses to be generated as an input
    dest_list
        The destination list where the addresses will be stored as an output
    """
    dest_list = []
    # Generates a list with half the amount of given email addresses
    # NOTE: only one email provider is considered and user's names start
    # with "user_0". If only 1 email is desired, then one random
    # email address is created

    if num == 1:
        new_email = "user_" + str(random.randint(0, 9)) + "@provider.com"
        dest_list.append(new_email)
    else:
        for i in range(num // 2):
            new_email = "user_" + str(i) + "@provider.com"
            dest_list.append(new_email)

        # Extends the email addresses list with a copy of the same list, and
        # shuffles the list reorganizing its order
        dest_list.extend(dest_list)
        random.shuffle(dest_list)

    return dest_list


def generate_emails_file(source_list, dest_file):
    """
    Creates a file and writes each email from a list

    Parameters
    ----------
    source_list
        The list to the source email addresses be transferred
    dest_file
        The path to the email addresses file as output
    """
    # Create the file, read from the list and add each email to a new line
    # NOTE: further file protection could be added
    with open(dest_file, 'w') as writer:
        try:
            for email in source_list:
                writer.write(email + "\n")
        except AssertionError as error:
            print(error)
    writer.close


if __name__ == "__main__":

    # Get number of fake emails to be created
    num_emails = get_num_emails(num_emails)

    # Generate list with email addresses
    emails_list = generate_emails_list(num_emails, emails_list)

    # Generate file with email addresses
    generate_emails_file(emails_list, emails_file)

    if num_emails == 1:
        print("A file containing one"
              " email address has "
              "been successfully generated.\n")
    else:
        print("A file containing " + str(num_emails) +
              " email addresses has "
              "been successfully generated.\n")
