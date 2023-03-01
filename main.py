def get_input():
    userInput = input("\nEnter morse code: ")

    match userInput:
        case ".-":
            print('A')
get_input()