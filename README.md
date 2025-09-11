# Learning Strings with PRIMM

## Why PRIMM with Strings?
Strings are sequences of characters, making them perfect for practicing loops while learning text processing. This lesson uses **PRIMM methodology**:

- **PREDICT**: Think about what the code will do
- **RUN**: Execute and check your predictions
- **INVESTIGATE**: Experiment with different inputs
- **MODIFY**: Fix broken code or add features
- **MAKE**: Create new functions from scratch

### In your pairs, get as far as you can. It's not a race. There is meant to be something here for everyone. Completing the first tasks and having an understanding of how we can work with string is the most important thing.

---

## Activity 1: Basic String Exploration 

### Task: Understanding Strings as Sequences

* **PREDICT**: Look at the `print_each_character` function. What will happen when you call `print_each_character("hello")`? How many lines will be printed?
* **RUN**: Execute the code and verify your prediction.
* **INVESTIGATE**: Try with `"a"`, `""` (empty string), and `"Python"`. What happens with each?
* **MODIFY**: Fix the `print_with_positions` function to show both the position and character.
* **MAKE**: Complete the `string_length_manual` function to count characters without using `len()`.

---

## Activity 2: Character Analysis (20 mins)

### Task: Examining Individual Characters

* **PREDICT**: Look at the `count_letter_a` function. How many 'a's do you think are in "banana"? What about uppercase vs lowercase?
* **RUN**: Test with `count_letter_a("banana")` and `count_letter_a("Apple")`.
* **INVESTIGATE**: Try different words. How does the function handle uppercase letters?
* **MODIFY**: Fix the `count_vowels` function so it counts both uppercase and lowercase vowels.
* **MAKE**: Complete the `is_all_digits` function to check if a string contains only numbers.

---

## Activity 3: String Building and Modification (25 mins)

### Task: Creating New Strings from Existing Ones

* **PREDICT**: Look at the `reverse_string` function. What will `reverse_string("cat")` return? Trace through the loop step by step.
* **RUN**: Test your prediction with several different words.
* **INVESTIGATE**: Try with palindromes like "racecar" or "level". What do you notice?
* **MODIFY**: Fix the `remove_spaces` function to properly remove all spaces from a string.
* **MAKE**: Complete the `make_acronym` function to create acronyms from phrases (e.g., "North Atlantic Treaty Organisation" → "NATO").

---

## Activity 4: Slicing for Practical Tasks (Make a Username)

* **MAKE**: Challenge: Use string slicing to create a username.
* **MAKE**: The format should be: first letter of the first name + entire last name.



---

## Final Reflection 

* **String Operations**: What are the key ways to process strings character by character?
* **Building vs Searching**: When do you build new strings vs analyse existing ones?
* **Common Patterns**: What loop patterns did you use repeatedly (accumulation, searching, building)?
* **Real Applications**: Where might these string processing skills be useful?

---

## Extension Challenges

* **Challenge 1**: Create a function that checks if a string is a palindrome (reads the same forwards and backwards).
* **Challenge 2**: Write a function that converts "camelCase" to "snake_case".
* **Challenge 3**: Create a simple text analyser that counts sentences, words, and average word length.