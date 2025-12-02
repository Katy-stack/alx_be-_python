# main.py

import sys
# Import the function from the other file
from robust_division_calculator import safe_divide

def main():
    # Check for correct number of arguments (script name + 2 numbers = 3)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are read as strings from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the robust function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()