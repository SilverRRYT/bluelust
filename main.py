import os

# Variables
hp = 5

# Functions
def clear():
    os.system("clear") # Clear for UNIX systems

# Main game function
def main():
    print("You wake up in a forest")
    print("There is a cave in front of you and a path to your left.")

    while True:
        place = input("Which way do you want to go? (f: Forawrd, l: Left)  ")

        if place == "f":
            print("You walk into the cave and see a ladder.")

if __name__ == "__main__":
    main()
