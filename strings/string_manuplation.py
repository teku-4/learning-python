#string manuplation
# Original string for manipulation
original_string = "  Hello, World! Welcome to Python programming.  "

# Removing leading and trailing whitespaces
trimmed_string = original_string.strip()
print(f"Original String: '{original_string}'")
print(f"Trimmed String: '{trimmed_string}'\n")

# Converting to uppercase
uppercase_string = trimmed_string.upper()
print(f"Uppercase Conversion: '{trimmed_string}' -> '{uppercase_string}'\n")

# Converting to lowercase
lowercase_string = trimmed_string.lower()
print(f"Lowercase Conversion: '{trimmed_string}' -> '{lowercase_string}'\n")

# Replacing a substring
replaced_string = trimmed_string.replace("World", "Universe")
print(f"Substring Replacement: '{trimmed_string}' -> '{replaced_string}'\n")

# Splitting into a list of words
word_list = trimmed_string.split()
print(f"Splitting into Words: '{trimmed_string}' -> {word_list}\n")

# Joining a list of words into a string
joined_string = " ".join(word_list)
print(f"Joining Words Back: {word_list} -> '{joined_string}'\n")

# Finding a substring
substring_to_find = "Python"
substring_index = trimmed_string.find(substring_to_find)
print(f"Finding Substring '{substring_to_find}': Index = {substring_index}\n")

# Checking if string starts with a prefix
prefix = "Hello"
starts_with_prefix = trimmed_string.startswith(prefix)
print(f"Starts with '{prefix}': {starts_with_prefix}\n")

# Checking if string ends with a suffix
suffix = "programming."
ends_with_suffix = trimmed_string.endswith(suffix)
print(f"Ends with '{suffix}': {ends_with_suffix}\n")

# Counting occurrences of a substring
substring_to_count = "o"
occurrences = trimmed_string.count(substring_to_count)
print(f"Occurrences of '{substring_to_count}': {occurrences}\n")

# Reversing a string
reversed_string = trimmed_string[::-1]
print(f"Reversed String: '{trimmed_string}' -> '{reversed_string}'\n")

# Capitalizing the first word
capitalized_string = trimmed_string.capitalize()
print(f"Capitalized String: '{trimmed_string}' -> '{capitalized_string}'\n")

# Title-casing the string
title_cased_string = trimmed_string.title()
print(f"Title Cased String: '{trimmed_string}' -> '{title_cased_string}'\n")

# Checking for alphanumeric characters
is_alphanumeric = trimmed_string.replace(" ", "").isalnum()
print(f"Is Alphanumeric (ignoring spaces): {is_alphanumeric}\n")
