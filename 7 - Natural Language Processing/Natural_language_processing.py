import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) # Ignoring the double quote

# Getting the stopwords
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords

# Cleaning the text
import re

corpus = []
for i in range(0, 1000):
    # Keeping the letters only
    review = re.sub('[^a-zA-Z]',' ', dataset['Review'][i])
    # Keeping the lower letter only
    review = review.lower()
    review = review.split()
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    
    review = ' '.join(review)
    corpus.append(review)
