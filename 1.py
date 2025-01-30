import re

# Sample text
text = "The rain in Spain stays mainly in the plain."

# Regular expression pattern to search for words ending with 'ain'
pattern = r'\b\w*ain\b'

# Finding all matches in the text
matches = re.findall(pattern, text)

print("Words ending with 'ain':", matches)

# Searching for the first occurrence
search_result = re.search(pattern, text)
if search_result:
    print(f"First match found: '{search_result.group()}' at position {search_result.start()}")
else:
    print("No match found.")
