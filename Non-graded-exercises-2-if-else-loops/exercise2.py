import random # You need this module to select a word randomly
print("Welcome to Hangman")
# Create a list of words that the game can choose from and then ask the user to guess 
word_list = ["black","myth","scrifice","game","science"]

# Store in this variable a random word from the above word_list
word_to_guess = random.choice(word_list)

total_attempts = 10
attempts_left = 10

letter_have_guessed = ''

hided_word = ""
for x in word_to_guess:
    hided_word += "_"
hided_word_with_space = " ".join(hided_word)

print(f"Attempts left: {attempts_left}.\nGuess: {hided_word_with_space}")

print(hided_word_with_space)

finish_flag = True

while finish_flag:
    while True:
        input_word = input("Enter a single letter to guess: ")
        alpha_flag = False
        number_flag = True
        special_flag = True
        guessed_flag = False

        for x in input_word:
            if x.isalpha():
                alpha_flag = True
            elif x.isdigit():
                number_flag = False
            else:
                special_flag = False
        for x in letter_have_guessed:
            if x == input_word:
                guessed_flag = True


        if not (alpha_flag and special_flag and number_flag and len(input_word) <= 1):
            print("Invalid input please try again")
            continue
        elif guessed_flag:
            print(f"You have guessed letter {input_word}")
        else:    
            letter_have_guessed += input_word
            break
    
    right_answer = False

    for index, value in enumerate(word_to_guess):
        if value == input_word:
            right_answer = True
            tamp_hided_word = hided_word_with_space
            hided_word_with_space = tamp_hided_word[0:index*2] + value + tamp_hided_word[index*2 + 1:]
    if right_answer:
        print("Correct guess!")
        print(f"Attempts left: {attempts_left}.\nGuess: {hided_word_with_space}")
    else:
        attempts_left = attempts_left -1
        print("Incorrect guess!")
        print(f"Attempts left: {attempts_left}.\nGuess: {hided_word_with_space}")

    print(f"The letter you guessed: {input_word}")

    if hided_word_with_space == " ".join(word_to_guess):
        finish_flag = False
        print("Awesome! You guessed the word correctly")
    elif attempts_left == 0:
        break

if finish_flag:
    print("Thank you for playing. Better luck next time.")
else:
    print("Thank you for playing. See you next time.")
# Complete the rest of the code. You will have to use the different methods you have learned so far. 