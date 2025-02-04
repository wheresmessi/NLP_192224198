import re

def pluralize_noun(noun):
    # Rule 1: If the noun ends with 's', 'x', 'z', 'sh', or 'ch', add 'es'
    if re.search(r'(s|x|z|sh|ch)$', noun):
        return noun + 'es'
    # Rule 2: If the noun ends with a consonant + 'y', change 'y' to 'ies'
    elif noun.endswith('y') and not noun[-2] in 'aeiou':
        return noun[:-1] + 'ies'
    # Rule 3: For most other nouns, just add 's'
    else:
        return noun + 's'

# Test cases
nouns = ["cat", "bus", "box", "lady", "church", "baby"]

plural_nouns = [pluralize_noun(noun) for noun in nouns]

print("Singular Nouns:", nouns)
print("Plural Nouns:", plural_nouns)
