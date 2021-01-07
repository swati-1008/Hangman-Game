import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6
stages = hangman_art.stages

print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
  display.append('_')

already_guessed_letters = []

print(stages[lives])

while '_' in display:
  guess = input("Guess a letter: ").lower()
  if guess in already_guessed_letters:
    print("You have already guessed the letter " + guess + ".")
    print(display)
    print(stages[lives])
  else:
    already_guessed_letters.append(guess)
    if guess not in chosen_word:
      lives -= 1
      print(guess + " is not in the word. You lose a life.")
      print(display)
      print(stages[lives])
    else:
      for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
          display[index] = guess
      print(display)
      print(stages[lives])
    if lives == 0:
      break

if lives == 0:
  print('You lose')
else:
  print('You win')
