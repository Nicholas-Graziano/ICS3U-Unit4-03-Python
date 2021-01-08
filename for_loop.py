#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if a number is negative or positive

def main():
    # input
    print("\n", end="")
    positive_integer_as_string = input("Enter a positive integer here:")

# process and output
    try:
        print("\n", end="")
        positive_integer = int(positive_integer_as_string)
        for positive_integer in range(0, positive_integer):
            square = positive_integer**2
            print(positive_integer, "square is", square)

    except Exception:
        print("This is not a positive_integer")


if __name__ == "__main__":
    main()
