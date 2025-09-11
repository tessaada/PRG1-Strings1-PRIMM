# Snippet 1
name = "Ada Lovelace"
print(name[0])

# Snippet 2
name = "Ada Lovelace"
for char in name:
    print(char)

# Snippet 3
text = "Gaming is relaxing" 
print(text[:3])

# Snippet 4
text = "Gaming is relaxing"
slice = text[15:]  
print(slice)

# Snippet 5
text = "Gaming is relaxing" 
print(text[-3:])

# Snippet 6
phrase = "coding gives your brain a workout"
print(phrase.upper())

# Snippet 7
game = "Cyberpunk 2077" 
release_year = 2020 
print(f"My favorite game is {game}, released in {release_year}.")

# Snippet 8
part1 = "Stream"
part2 = "is"
part3 = " good"
print(part1 + "ing " + part2 + part3)

# Snippet 9
part1 = "Stream"
part2 = "is"
part3 = " good"
sentence = part1 + "ing " + part2 + part3
print(sentence)

# Snippet 10
colours = "red,blue,green" 
colour_list = colours.split(",")
print(colour_list[2])

# Snippet 11
title = " THE HANGOVER "
edited_title = title.strip().lower() 

# Snippet 12
price = 49.99 
print(f"The item is on sale! Was: ${price}, Now: ${price - 15.00}")

# Snippet 13
url = "[www.youtube.com/watch?v=dQw4](https://www.youtube.com/watch?v=dQw4)" 
new_url = url.replace("youtube", "invidious") 
print(new_url)

# Snippet 14
message = "HELLO_WORLD_123"
part = message.split("_")
print(part[1].lower())

# Snippet 15
user_input = " I love python! " 
cleaned_input = user_input.strip().replace("love", "♥").capitalize() 
print(cleaned_input)