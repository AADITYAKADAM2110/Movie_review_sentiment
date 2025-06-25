import re #re = Regular expressions library → used for pattern matching (like removing HTML, numbers)
import string #string.punctuation = a string of all punctuation characters: '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`
import nltk #nltk = Natural Language Toolkit → used for text processing
from nltk.corpus import stopwords #stopwords.words('english') = list of common English words we want to remove like "the", "is", "and"
from nltk.stem import PorterStemmer #PorterStemmer = reduces words to their root form: “playing” → “play”, “amazing” → “amaz”

nltk.download('stopwords')
nltk.download('punkt')

stopwords = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    tokens = text.split()
    cleaned_tokens = []
    for word in tokens:
        if word not in stopwords:
            stemmed = stemmer.stem(word)   
            cleaned_tokens.append(stemmed)  
    return ''.join(tokens) 