import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
text = """Perform tokenization, stemming, and stop-word removal on sample text."""
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and
word.isalpha()]
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
print("Original Tokens: ", tokens)
print("Filtered Tokens (no stop-words): ", filtered_tokens)
print("Stemmed Tokens: ", stemmed_tokens)
