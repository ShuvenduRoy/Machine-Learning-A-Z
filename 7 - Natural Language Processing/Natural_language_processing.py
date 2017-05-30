import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) # Ignoring the double quote

# Getting the stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Cleaning the text
import re
# Keeping the letters only
review = re.sub('[^a-zA-Z]',' ', dataset['Review'][0])
# Kepping the lower letter only
review = review.lower()
review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]


