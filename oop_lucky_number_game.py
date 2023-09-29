# Required libraries
import random
import datetime

# Define a class for the Lucky Number Game
class LuckyNumberGame:
    
    # Constructor
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.age = 0
        self.tries_count = 0
        self.lucky_list, self.lucky_number = [], 0

    # Method to take user input for name and ensure it's valid
    def input_name(self):
        while True:
            name = input("Enter your full name (first name and last name): ")
            if name.replace(" ", "").isalpha() and name.count(" ") == 1:
                self.name = name
                return

    # Method to input and validate the birthdate
    def input_birthdate(self):
        while True:
            birthdate = input("Enter your birthdate in format yyyymmdd: ")
            if len(birthdate) == 8 and birthdate.isdigit():
                year, month, day = int(birthdate[:4]), int(birthdate[4:6]), int(birthdate[6:])
                if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                    self.birthdate = birthdate
                    return
                else:
                    print("Invalid date!")
            else:
                print("Invalid input!")

    # Method to calculate age from birthdate
    def calculate_age(self):
        current_year = datetime.datetime.now().year
        self.age = current_year - int(self.birthdate[:4])

    # Method to generate the list of random numbers and the special lucky number
    def generate_lucky_list(self):
        self.lucky_list = random.sample(range(101), 9)
        available_numbers = set(range(101)) - set(self.lucky_list)
        self.lucky_number = random.choice(list(available_numbers))
        self.lucky_list.append(self.lucky_number)


    # Main game method
    def play(self):
        self.tries_count += 1
        print("Lucky list:", self.lucky_list)
        input_num = int(input("Pick the lucky number from the list: "))

        # Check if guess is correct
        if input_num == self.lucky_number:
            print(f"Congratulations, game is over! You got the lucky number on try#{self.tries_count}.")
            play_again = input("Do you want to play again? (y for Yes, n for No): ")
            if play_again.lower() == 'y':
                self.generate_lucky_list()
                self.tries_count = 0
                return True
            else:
                return False
        else:
            # Define the range for the shorter list
            min_val, max_val = self.lucky_number - 10, self.lucky_number + 10
            shorter_lucky_list = [num for num in self.lucky_list if min_val <= num <= max_val]

            # Check if the guessed number is in the shorter list
            if input_num not in shorter_lucky_list:
                print(f"Wrong guess! This is try#{self.tries_count}. The number {input_num} is not in the shorter list.")
            else:
                print(f"Wrong guess! This is try#{self.tries_count}. The number {input_num} is close to the lucky number.")
                
            # Remove guessed number if present in the main list
            if input_num in self.lucky_list:
                self.lucky_list.remove(input_num)

            # End game if the lucky list becomes too short
            if len(self.lucky_list) <= 2:
                print("Game over!")
                return False

            return True


    # Main execution method for the class
    def start_game(self):
        self.input_name()
        while True:
            self.input_birthdate()
            self.calculate_age()
            if self.age >= 18:
                break
            else:
                print("You're underage! Please re-enter your birthdate.")
        self.generate_lucky_list()
        while self.play():
            pass

# Main execution, only when the script is run directly (not imported as a module)
if __name__ == "__main__":
    game = LuckyNumberGame()
    game.start_game()
