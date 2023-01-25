import random
import hangman_art
import hangman_words

# randomization
chosen_word = random.choice(hangman_words.word_list)
# debug - No need
# print("Random word: ", chosen_word)

# create an empty list
display = []
# make list with "_" according to the length of choose_word
lowerDash = "_"
for i in range(0, len(chosen_word)):
    display += lowerDash

# debug - No need
# print(display)
# lives - check how many try user can try
lives = 6

# print the game logo
print(hangman_art.logo)

# trigger - to end while loop
end_of_theGame = False
# while loop
while not end_of_theGame:

    # input
    guess = input("Guess a number: ").lower()
    # test of user's input is matched with the choose_word
    for letter in chosen_word:
        # check it;s available or not
        # debug - No need
        if letter == guess:
            print("True")
        else:
            print("False")

    # display message - repeating
    if guess in display:
        print("You have already entered this letter. Try another one.")

    # replace the "_" with the guess, if matches choose_Word
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    # debug
    print(display)

    # checking the guess was in the chosen_word or not!
    if guess not in chosen_word:
        lives -= 1

        # display message - wrong letter
        print(f"You choose this letter {guess} which is wrong. You lose a life.\n Be Careful!")
        # when lives becomes 0, user will lose.
        if lives == 0:
            # turn on the trigger
            end_of_theGame = True
            print("You lose!")

    # check if lowerDash "_" is in the list or not. If not end the while loop
    if lowerDash not in display:
        # turning on the trigger
        end_of_theGame = True
        print("You win!")

    # hangman art print - if mistake made
    print(hangman_art.stages[lives])
