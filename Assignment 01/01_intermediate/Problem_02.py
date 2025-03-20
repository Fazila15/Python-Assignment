from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return Fore.RED + "Index is out of range"
    return Fore.GREEN + str(lst[index])

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return Fore.RED + "Index is out of range"
    lst[index] = new_value
    return Fore.CYAN + str(lst)

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        return Fore.RED + "Invalid range"
    return Fore.YELLOW + str(lst[start:end])

def game():
    my_list = [5, "apple", 12, "banana", 20]

    print(Fore.MAGENTA + "Welcome to the Index Game!")
    print(Fore.CYAN + "Here's the list:", my_list)

    while True:
        print(Fore.MAGENTA + "\nChoose an operation:")
        print(Fore.CYAN + "1. Access an element")
        print(Fore.CYAN + "2. Modify an element")
        print(Fore.CYAN + "3. Slice the list")
        print(Fore.CYAN + "4. Exit the game")

        choice = input(Fore.YELLOW + "Enter the number of the operation: ")

        if choice == "1":
            index = int(input(Fore.YELLOW + "Enter an index to access: "))
            print(Fore.GREEN + "Element:", access_element(my_list, index))

        elif choice == "2":
            index = int(input(Fore.YELLOW + "Enter an index to modify: "))
            new_value = input(Fore.YELLOW + "Enter the new value: ")
            print(Fore.GREEN + "Updated list:", modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input(Fore.YELLOW + "Enter the start index: "))
            end = int(input(Fore.YELLOW + "Enter the end index: "))
            print(Fore.GREEN + "Sliced list:", slice_list(my_list, start, end))

        elif choice == "4":
            print(Fore.MAGENTA + "Exiting the game. Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice, please try again.")

# Run the game
game()
