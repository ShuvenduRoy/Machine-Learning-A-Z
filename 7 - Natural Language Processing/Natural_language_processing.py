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
# Keeping the letters only
review = re.sub('[^a-zA-Z]',' ', dataset['Review'][0])
# Keeping the lower letter only
review = review.lower()
review = review.split()

ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]


