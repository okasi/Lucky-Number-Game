import procedural_lucky_number_game
import oop_lucky_number_game

def main():
    print("Choose which version of the Lucky Number Game you'd like to play:")
    print("1. Procedural version")
    print("2. Object Oriented version")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        procedural_lucky_number_game.play_game()
    elif choice == '2':
        game = oop_lucky_number_game.LuckyNumberGame()
        game.start_game()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
