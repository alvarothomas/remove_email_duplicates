"""
This script removes all duplicates from an unsorted list of email
addresses, while leaving the remaining list in the original order.
The email addresses are first read from a file and converted to
the a list which is treated to generate a new file with the email
addresses without duplicates
"""

import sys
import os
import time
# OrderedDict returns an instance of a dict subclass that has
# methods specialized for rearranging dictionary order.
# This is used to cover ordered dictionaries even with versions
# of Python older than 3.6
from collections import OrderedDict


# file without duplicated email addresses
emails_file_no_dups = "./emails_no_dups.txt"
# list of email addresses with duplicates
emails_list_dups = []
# list of email addresses without duplicates
emails_list_no_dups = []


def get_emails_list(emails_list_read):
    """
    Reads email addresses from a file given as an argument
    and stores them in a list

     Parameters
    ----------
    emails_list_read
        The destination list where email addresses will be stored
    emails_file_name
        Name of the text file where email addresses are stored
    """

    # Ask the user for a file that contains the email addresses
    # NOTE: further security checks could be added

    emails_list_read = []
    if not type(sys.argv[1]) is str:
        raise TypeError("Please give a valid filename")
    else:
        try:
            emails_file_name = sys.argv[1]
            with open(emails_file_name) as reader:
                emails_list_read = reader.read().split("\n")
                # emails_list_read = reader.readlines().splitlines()
        except AssertionError as error:
            print(error)
    return emails_list_read


def remove_dup_list(source_list, dest_list):
    """
    removes all duplicates from an unsorted list of email
    addresses, while leaving the remaining list in the original order

    Parameters
    ----------
    source_list
        An unsorted list of email addresses with duplicates
    dest_list
        The destination list where the addresses will be stored
        without duplicates
    """
    dest_list = []

    dest_list = list(OrderedDict.fromkeys(source_list))

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

    start = time.clock()
    print("Starting timer")

    # Read email addresses from the file given as an argument
    emails_list_dups = get_emails_list(emails_list_dups)

    # Remove duplicates from the list
    emails_list_no_dups = remove_dup_list(
        emails_list_dups, emails_list_no_dups)

    # Generate file with email addresses
    generate_emails_file(emails_list_no_dups, emails_file_no_dups)

    end = time.clock()
    print("Finishing timer")
    print(end - start)
