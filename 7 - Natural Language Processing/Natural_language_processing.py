import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) # Ignoring the double quote

# Cleaning the text
import re
# Keeping the letters only
review = re.sub('[^a-zA-Z]',' ', dataset['Review'][0])
# Kepping the lower letter only
review = review.lower()

import nltk
nltk.download('stopwords')
