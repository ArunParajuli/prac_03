"""

Questions

1. When will a ValueError occur?

   ans: A ValueError arises when the user inputs a value that is unconvertable to an integer, such as a string or a floating-point number.


2. When will a ZeroDivisionError occur?

 ans: A ZeroDivisionError arises when the user inputs 0 because division by zero is prohibited.


3. Could you change the code to avoid the possibility of a ZeroDivisionError?

 ans: Certainly, we can include a condition to verify whether the user input is 0, and then request the user to input a non-zero value.


4. If you could figure out the answer to question 3, then make this change now.

"""



finished = False

result = 0

while not finished:

    try:

        number = int(input("Enter a valid non-zero integer: "))

        if number == 0:

            print("Please enter a non-zero integer.")

        else:

            result = 10 / number

            finished = True

    except ValueError:

        print("Please enter a valid integer.")


print("Valid result is:", result)
