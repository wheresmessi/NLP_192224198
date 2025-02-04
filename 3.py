import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')

# Example sentence
sentence = "The cats are chasing the mice."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Perform stemming
stemmed_words = [stemmer.stem(word) for word in tokens]

print("Original words:", tokens)
print("Stemmed words:", stemmed_words)
