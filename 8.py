import nltk
from collections import Counter, defaultdict
import random

nltk.download('brown')
nltk.download('universal_tagset')

# Load Brown corpus for training
from nltk.corpus import brown
tagged_sents = brown.tagged_sents(tagset='universal')

# Build a simple probability model
word_tag_freq = defaultdict(Counter)
tag_freq = Counter()

for sentence in tagged_sents:
    for word, tag in sentence:
        word_tag_freq[word.lower()][tag] += 1
        tag_freq[tag] += 1

# Assign most probable tag to a word
def get_most_probable_tag(word):
    word = word.lower()
    if word in word_tag_freq:
        return word_tag_freq[word].most_common(1)[0][0]
    else:
        return tag_freq.most_common(1)[0][0]  # Assign the most common tag in the corpus

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()

# Perform POS tagging
stochastic_tags = [(word, get_most_probable_tag(word)) for word in words]

print("Stochastic POS Tags:", stochastic_tags)
