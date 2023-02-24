
user_text = input("Type your text\n")
word_to_replace = input("What word would you like to replace in your text?: ")
new_word = input("What word would you replace '"+ word_to_replace + "' with?: ")
new_user_text = user_text.replace(word_to_replace, new_word)
print("Your new text is: " + new_user_text)