words = ["Bicycle","Dio","Holyness","Epicness","Chorba","Shest","Koremche","Auschwitz","Kopach","BratMi","Posleden"]

try:
    choose = int(input("Please enter a random number to get(0-9): "))
except:
    print("Error, please make sure you entered a number between 0-9!")
    quit()

chosen_word = words[choose]

print("The length of your word is: ", len(chosen_word))
print("Guess the characters!")

guesses = ''

turns = 9

while turns > 0:

    failed = 0

    for char in chosen_word:
        if char in guesses:
            print(char)
        else:
            print("-")
            failed +=1


    if failed == 0:
        print("Congrats you won!")
        print("The word was: ", chosen_word)

        break


    guess = input("guess the next character:")

    guesses += guess

    if guess not in chosen_word:
        
        turns -= 1
        print("Uh no, try AGAIN!")
        print("You have ", + turns, " turns left")

    if turns == 0:
        print("You lost!")
        quit()
