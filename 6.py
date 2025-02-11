import random
import nltk
from nltk.util import bigrams
from collections import defaultdict

nltk.download('punkt')

# Sample text
text = "This is a simple text generation example using a bigram model in Python."

# Tokenize text
tokens = nltk.word_tokenize(text)

# Generate bigrams
bigram_model = list(bigrams(tokens))

# Build frequency dictionary
bigram_dict = defaultdict(list)
for w1, w2 in bigram_model:
    bigram_dict[w1].append(w2)

# Generate text using bigram model
def generate_text(start_word, length=10):
    current_word = start_word
    generated_text = [current_word]
    
    for _ in range(length):
        next_words = bigram_dict.get(current_word, None)
        if not next_words:
            break
        current_word = random.choice(next_words)
        generated_text.append(current_word)
    
    return ' '.join(generated_text)

# Generate text starting with "This"
print(generate_text("This", length=10))
