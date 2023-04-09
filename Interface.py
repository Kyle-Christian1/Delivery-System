# Kyle Christian 000959459

import Main

# This program's time complexity is O(n^2)

def main():

    # Time Complexity: O(n)
    while True:
        print("Select an option using the number keys:")
        print("[1] View all packages...")
        print("[2] Look up time...")
        print("[3] Exit...")
        response = input("> ")
        if response == str(1):
            Main.main('00:00:00', '1')
        elif response == str(2):
            print("\n**Enter time in hh:mm::ss format using 24 hour time. ex. 1pm = 13:00:00")
            # Time Complexity: O(1)
            user_time = input("Enter time: ")
            Main.main(user_time, '2')
            print()
        elif response == str(3):
            exit()
        else:
            print("Please submit a valid response.")

main()