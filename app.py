import nltk
from textblob import TextBlob
import tkinter as t
from newspaper import article


def summarize():
    url=utext.get('1.0','end').strip()
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    


