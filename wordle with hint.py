import random
from word_list import wordlist  # Importing the wordlist from word_list.py

class Wordle:
    def __init__(self, wordlist, target_word=None, max_attempts=6):
        self.wordlist = wordlist
        self.target_word = target_word or random.choice(wordlist).upper()
        self.guesses = []
        self.hints_given = 0
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts

    def give_hint(self):
        if self.attempts_left > 1:  # Ensure we still have guesses left after using a hint
            if self.hints_given < len(self.target_word):
                for i in range(len(self.target_word)):
                    if self.target_word[i] not in self.guesses:
                        self.hints_given += 1
                        self.attempts_left -= 1  # Hint counts as one attempt
                        return f"Hint: Letter at position {i+1} is '{self.target_word[i]}'."
        return "No more hints available or no attempts left!"

    def guess(self, guess_word):
        guess_word = guess_word.upper()
        if len(guess_word) != len(self.target_word):
            return "Invalid guess length."
        
        self.guesses.append(guess_word)
        self.attempts_left -= 1
        result = []
        
        for i in range(len(self.target_word)):
            if guess_word[i] == self.target_word[i]:
                result.append(f"{guess_word[i]}(correct)")
            elif guess_word[i] in self.target_word:
                result.append(f"{guess_word[i]}(wrong position)")
            else:
                result.append(f"{guess_word[i]}(wrong)")
        
        if guess_word == self.target_word:
            return f"Congratulations! You guessed the word correctly: {self.target_word}"
        
        if self.attempts_left == 0:
            return f"Game over! You've run out of attempts. The correct word was: {self.target_word}"
        
        return f"Result: {' | '.join(result)}\nAttempts left: {self.attempts_left}"

# Initialize the Wordle game with a target word (or a random word from the wordlist)
game = Wordle(wordlist)

print("Welcome to Wordle! Guess the 5-letter word.")
print("You have 6 total chances, including hints. You can type 'hint' for a hint.")

# Game loop
while True:
    command = input("Enter a guess or type 'hint' for a hint: ").strip().upper()
    
    if command == "HINT":
        print(game.give_hint())
    elif command == "EXIT":
        print("Thanks for playing!")
        break
    else:
        result = game.guess(command)
        print(result)
        
        if "Congratulations!" in result or "Game over!" in result:
            break
