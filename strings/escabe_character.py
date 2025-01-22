# # Example 1: Using escape character for newline (\n)
# newline_example = "Hello\nWorld!"
# print("Example 1 - Newline:")
# print(newline_example)
# print()  # Prints an empty line for separation

# # Example 2: Using escape character for tab (\t)
# tab_example = "Name\tAge\tCountry"
# print("Example 2 - Tab:")
# print(tab_example)
# print()

# # Example 3: Using escape character for backslash (\\)
# backslash_example = "C:\\Users\\User\\Documents"
# print("Example 3 - Backslash:")
# print(backslash_example)
# print()

# # Example 4: Using escape characters for quotes (\' and \")
# quote_example = "He said, \"It's a beautiful day!\""
# print("Example 4 - Quotes:")
# print(quote_example)
import time

# Example using carriage return (\r) to overwrite text
for i in range(10):
    print(f"\rCount: {i}", end="", flush=True)
    time.sleep(1)
print("hello\r\tworld")