import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def train():
    imdb = pd.read_csv('imdb_labelled.txt',sep='\t',header=None)
    amazon = pd.read_csv('amazon_cells_labelled.txt',sep='\t',header=None)
    yelp = pd.read_csv('yelp_labelled.txt',sep='\t',header=None)

    df = pd.DataFrame()

    df = pd.concat([imdb,amazon,yelp],ignore_index=True)
    df.columns = ['Review','Sentiment']
    tokens = []
    for i in range(len(df)):
        tokens.append(word_tokenize(df['Review'][i]))

    stopwordsList = stopwords.words("english")
    stopwordsList.extend([',','.','-','!'])

    wordsList = []
    for tokenList in tokens:
        words = []
        for word in tokenList:
            if word.lower() not in stopwordsList:
                words.append(word.lower())
        wordsList.append(words)

    wnet = WordNetLemmatizer()
    for i in range(len(wordsList)):
        for j in range(len(wordsList[i])):
            wordsList[i][j] = wnet.lemmatize(wordsList[i][j], pos='v')

    cv = CountVectorizer()

    for i in range(len(wordsList)):
        wordsList[i] = ' '.join(wordsList[i])

    vect = cv.fit_transform(wordsList)

    y = df['Sentiment'].values
    x_train,x_test,y_train,y_test = train_test_split(vect,y,test_size=0.25)

    reg = LogisticRegression()

    reg.fit(x_train,y_train)
    y_pred = reg.predict(x_test)

def test(review):
    pass
