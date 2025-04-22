"""
Jai Outland
Github: 
personal_diary.py
"""

# Basic diary program


def main():
    # User enters date of diary entry
    date = input("What is the date? (Example: 04.21.2025): ")

    # User inputs time of diary entry
    time = input("What is the time? (Example: 11:30 PM): ")

    # User is prompted to start diary entry
    entry = input("Write your diary entry below:\n")

    # Open file
    file = open("diary.txt", "a")

    # Enter date and time
    file.write("Date: " + date + "  Time: " + time + "\n")

    # Write diary entry
    file.write(entry + "\n")

    file.write("\n")

    # Close file to save entry
    file.close()

    # User is prompted with entry saved message
    print("Your diary entry was saved!")


# Call main function
main()
