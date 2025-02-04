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
    
    title.delete('1.0','end')
    title.insert('1.0',article.title)
    
    author.delete('1.0','end')
    author.insert('1.0',article.authors)
    
    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)
    
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    analysis=TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')
    
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
    
gui=t.TK()
gui.title('News Summary Report')

    
    
    


