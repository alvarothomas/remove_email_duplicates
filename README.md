# PROBLEM:

"Write a function that removes all duplicates from an unsorted list of email addresses, while leaving the remaining list in the original order.
Prove that this function can handle 100,000 email addresses containing 50% randomly placed duplicates, in under 1 second on a typical laptop"

# SOLUTION:

This project includes two scripts written in Python:

## generate_emails.py
This script generates a text file with as many email addresses as
the number passed in as argument. The file contains 50% randomly
placed duplicates except if only one email is desired.

## remove_email_duplicates.py
Script that removes all duplicates from an unsorted list of email addresses, while leaving the remaining list in the original order
The email addresses are first read from a file and converted to the list which is treated to generate a new file with the email
addresses without duplicates

"generate_emails" is used to create the file of 100,000 email addresses containing 50% randomly placed duplicates and the solution
to the problem is coded in "remove_email_duplicates". The later relies on OrderedDict which returns an instance of a dict subclass that has
methods specialized for rearranging dictionary order. This is used to cover ordered dictionaries even with versions of Python older than 3.6,
where dictionaries are already sorted. Please refer to https://docs.python.org/3/library/collections.html#collections.OrderedDict for further
reference.

There are two scripts to test the above mentioned functionality using the pytest framework:

## test_generate_emails.py
This set of tests covers the main functions of generate_emails.py.
### test_generate_emails_list
### test_generate_emails_file

## test_rem_dup_emails.py
This set of tests covers the main functions of remove_email_duplicates.py.
### test_remove_dup_list
### test_generate_emails_file

# USAGE

1. To generate a file containing 100000 emails please type the following in the terminal:

python generate_emails.py 100000

2. To generate the file with all duplicates removed please type:

remove_email_duplicates.py email_addresses.txt

(Given that the previoulsy generated file is called "email_addresses.txt")

3. `pytest` can be installed in a virtualenv by typing pip install pytest

4. To run the tests `pytest` will run all tests found in the sub-folders (starting with filename prefixed with `test_`).

# BENCHMARKING

'time' module is used to set a timer with start and stop and measure the execution time.

- If set right before the function that sorts the list, this is successfully executed under one second:

python remove_email_duplicates.py email_addresses.txt
Starting timer
Finishing timer
0.062402

- If set before reading the file, this might need slightly more than one second:

python remove_email_duplicates.py email_addresses.txt
Starting timer
Finishing timer
0.10821700000000001
