"""
This set of tests covers the main functions of remove_email_duplicates.py
using the pytest framework.

TEST SCENARIOS

test_remove_dup_list
test_generate_emails_file

"""

import pytest
import os.path
from os import path

from src import remove_email_duplicates

# NOTE: test data could be handled in an external configuration file


def test_remove_dup_list():
    """
    Tests that cover removing duplicates from a list
    of an input number, containing duplicates

    Test cases:

        test_remove_dup_list_TC1:
            Result list is correct

        test_remove_dup_list_TC2:
            Result list does not contain duplicates
    """
    dup_list = ['4', '3', '3', '2', '1', '2']

    no_dup_list = []

    no_dup_list = remove_email_duplicates.remove_dup_list(
        dup_list, no_dup_list)

    assert no_dup_list == ['4', '3', '2', '1'], "Result list is correct"

    assert len(no_dup_list) == len(
        set(no_dup_list)), "List does not contain dups"


def test_generate_emails_file():
    """
    Tests that cover the creation of a file where the emails
    are stored without duplicates and with the original order

    Test cases:

        test_generate_emails_file_TC1:
            File "./test_file_no_dups.txt" is created
        test_generate_emails_file_TC2:
            File "./test_file_no_dups.txt" is not empty
    """
    no_dup_list = ['4', '3', '2', '1']
    no_dup_file = "./test_file_no_dups.txt"

    remove_email_duplicates.generate_emails_file(no_dup_list, no_dup_file)

    assert path.exists("./test_file_no_dups.txt"), "File created"
    assert os.stat(no_dup_file).st_size != 0, "File is not empty"
