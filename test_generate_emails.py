"""
This set of tests covers the main functions of generate_emails.py
using the pytest framework.

TEST SCENARIOS

test_generate_emails_list
test_generate_emails_file

"""

import pytest
import os.path
from os import path

from src import generate_emails

# NOTE: test data could be handled in an external configuration file


def test_generate_emails_list():
    """
    Tests that cover the creation of a list which size is the same
    of an input number, containing duplicates

    Test cases:

        test_generate_emails_list_TC1:
            List size same as input number

        test_generate_emails_list_TC2:
            List contains duplicated emails
    """
    dup_list = []

    dup_list = generate_emails.generate_emails_list(100000, dup_list)

    assert len(dup_list) == 100000, "List size same as input number"

    assert len(dup_list) != len(set(dup_list)), "List contains duplicates"


def test_generate_emails_file():
    """
    Tests that cover the creation of a file where the emails
    are stored

    Test cases:

        test_generate_emails_file_TC1:
            File "./test_file_duplicates.txt" is created
    """
    dup_list = []

    dup_list = generate_emails.generate_emails_list(100000, dup_list)
    dup_file = "./test_file_duplicates.txt"

    generate_emails.generate_emails_file(dup_list, dup_file)

    assert path.exists("./test_file_duplicates.txt"), "File created"
    assert os.stat(dup_file).st_size != 0, "File is not empty"
