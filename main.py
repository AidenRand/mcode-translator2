def get_input():
    print('----------------------------')
    print('   MORSE CODE TRANSLATOR')
    print('----------------------------')
    print('     Enter (q) to quit')
    while True:
        userInput = input("\nEnter morse code: ")
        match userInput:
            case '.-':
                print('A')
            case '-...':
                print('B')
            case '-.-.':
                print('C')
            case '-..':
                print('D')
            case '.':
                print('E')
            case '..-.':
                print('F')
            case '--.':
                print('G')
            case '....':
                print('H')
            case '..':
                print('I')
            case '.---':
                print('J')
            case '-.-':
                print('K')
            case '.-...':
                print('L')
            case '--':
                print('M')
            case '-.':
                print('N')
            case '---':
                print('O')
            case '.--.':
                print('P')
            case '--.-':
                print('Q')
            case '.-.':
                print('R')
            case '...':
                print('S')
            case '-':
                print('T')
            case '..-':
                print('U')
            case '...-':
                print('V')
            case '.--':
                print('W')
            case '-..-':
                print('X')
            case '-.--':
                print('Y')
            case '--..':
                print('Z')
            case '.----':
                print('1')
            case '..---':
                print('2')
            case '...--':
                print('3')
            case '....-':
                print('4')
            case '.....':
                print('5')
            case '-....':
                print('6')
            case '--...':
                print('7')
            case '---..':
                print('8')
            case '----.':
                print('9')
            case '-----':
                print('0')
            case 'q':
                break
        
get_input()