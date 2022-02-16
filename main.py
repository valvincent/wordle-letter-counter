### list.py contains Python list named 'wordlist'.
### contains all 12,972 5-letter words found in the ORIGINAL Wordle JavaScript.

### nyt_list.py contains Python list named 'wordlist'.
### contains all 12,947 5-letter words found in the NYTimes Wordle JavaScript.

### Uncomment/comment out the appropriate line/s of code whether using ORIGINAL or NYTIMES Wordle.

# from list import wordlist as wordle_list ### ORIGINAL Wordle
from nyt_list import wordlist as wordle_list ### NYTimes Wordle


### Python dictionary with the 26 letters of the alphabet as keys.
### Value for each key is the number of occurence, to be updated as the program runs.
alphabet = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
    "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
    "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,
    }

### Iterate through each word in the Wordle list.
for word in wordle_list:
    broken_word = list(word)
    ### Iterate through each letter in the alphabet and check if it is in the current word.
    for letter in alphabet:
        if letter in broken_word:
            alphabet[letter] += 1 ### Increment the count value in the dictionary if letter is found.

### Iterate through each key(letter) in the dictionary, printing the value(count) for each key.
for letter in alphabet:
    print(f"Letter {letter.upper()} appears in {alphabet[letter]} words.")
