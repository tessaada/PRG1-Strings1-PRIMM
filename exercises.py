
# ==============================================================================
# ACTIVITY 1: Basic String Exploration
# ==============================================================================

# Print each character on its own line
def print_each_character(text):
    for char in text:
        print(char)

# Show position and character - MODIFY this function
def print_with_positions(text):
    for i in range(len(text)):
        # TODO: Fix this to show position and character together
        print(text[i])  # Should show something like "0: h"

# MAKE: Count characters without using len()
def string_length_manual(text):
    # TODO: Use a loop to count how many characters are in the string
    # Don't use len() - count them yourself!
    pass

# ==============================================================================
# ACTIVITY 2: Character Analysis  
# ==============================================================================

# Count how many times 'a' appears
def count_letter_a(text):
    count = 0
    for char in text:
        if char == 'a':
            count += 1
    return count

# Count vowels - MODIFY this function
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:  # This only counts lowercase!
            count += 1
    return count

# MAKE: Check if string contains only digits
def is_all_digits(text):
    # TODO: Return True if every character is a digit (0-9)
    # Return False if any character is not a digit
    # Hint: Use char.isdigit() or check if '0' <= char <= '9'
    pass

# ==============================================================================
# ACTIVITY 3: String Building and Modification
# ==============================================================================

# Reverse a string
def reverse_string(text):
    result = ""
    for char in text:
        result = char + result  # Add to front, not back
    return result

# Remove spaces - MODIFY this function  
def remove_spaces(text):
    result = ""
    for char in text:
        if char == ' ':
            result = result + char  # This adds spaces instead of removing!
    return result

# MAKE: Create acronym from phrase
def make_acronym(phrase):
    # TODO: Take first letter of each word to make acronym
    # Example: "North Atlantic Treaty" -> "NAT"
    # Hint: You'll need to identify word boundaries (spaces)
    pass


# ==============================================================================
# ACTIVITY 4: Slicing for Practical Tasks (Make a Username)
# ==============================================================================
# Challenge: Use string slicing to create a username.
# The format should be: first letter of the first name + entire last name.

# MAKE: Create a username from a full name
def create_username(full_name):
    """
    Creates a username from a full name.
    Example: 'Zara Sharma' -> 'zsharma'
    """
    # TODO: Split the full_name into first and last names.
    # Use slicing to get the first initial and then combine it
    # with the last name. Make sure the username is all lowercase.
    pass



# ==============================================================================
# TEST YOUR FUNCTIONS
# ==============================================================================

# Make calls to your functions here as necessary
    