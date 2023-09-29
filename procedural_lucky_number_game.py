# Required libraries
import random
import datetime

# Function to take user input for name and ensure it's valid
def input_name():
    while True:
        name = input("Enter your full name (first name and last name): ")
        if name.replace(" ", "").isalpha() and name.count(" ") == 1:
            return name

# Function to input and validate the birthdate
def input_birthdate():
    while True:
        birthdate = input("Enter your birthdate in format yyyymmdd: ")
        if len(birthdate) == 8 and birthdate.isdigit():
            year, month, day = int(birthdate[:4]), int(birthdate[4:6]), int(birthdate[6:])
            if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                return birthdate
            else:
                print("Invalid date!")
        else:
            print("Invalid input!")

# Calculate age from birthdate
def calculate_age(birthdate):
    current_year = datetime.datetime.now().year
    return current_year - int(birthdate[:4])

# Generate the list of random numbers and the special lucky number
def generate_lucky_list():
    lucky_list = random.sample(range(101), 9)
    lucky_number = random.randint(0, 100)
    lucky_list.append(lucky_number)
    return lucky_list, lucky_number

# Main game function
def play_game():
    tries_count = 0
    lucky_list, lucky_number = generate_lucky_list()
    while True:
        tries_count += 1
        print("Lucky list:", lucky_list)
        input_num = int(input("Pick the lucky number from the list: "))

        # Check if guess is correct
        if input_num == lucky_number:
            print(f"Congratulations, game is over! You got the lucky number on try#{tries_count}.")
            play_again = input("Do you want to play again? (y for Yes, n for No): ")
            if play_again.lower() == 'y':
                lucky_list, lucky_number = generate_lucky_list()
                tries_count = 0
            else:
                break
        else:
            # Define the range for the shorter list
            min_val, max_val = lucky_number - 10, lucky_number + 10
            shorter_lucky_list = [num for num in lucky_list if min_val <= num <= max_val]

            # Check if the guessed number is in the shorter list
            if input_num not in shorter_lucky_list:
                print(f"Wrong guess! This is try#{tries_count}. The number {input_num} is not in the shorter list.")
            else:
                print(f"Wrong guess! This is try#{tries_count}. The number {input_num} is close to the lucky number.")
            
            # Remove guessed number if present in the main list
            if input_num in lucky_list:
                lucky_list.remove(input_num)

            # End game if the lucky list becomes too short
            if len(lucky_list) <= 2:
                print("Game over!")
                break

# Main execution, only when the script is run directly (not imported as a module)
if __name__ == "__main__":
    name = input_name()
    while True:
        birthdate = input_birthdate()
        age = calculate_age(birthdate)
        if age >= 18:
            break
        else:
            print("You're underage! Please re-enter your birthdate.")
    play_game()
