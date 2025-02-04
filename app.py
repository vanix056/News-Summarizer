import nltk
from textblob import TextBlob
import tkinter as t
from newspaper import Article


def summarize():
    url = utext.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title if article.title else "No Title Available")

    author.delete('1.0', 'end')
    author.insert('1.0', ", ".join(article.authors) if article.authors else "No Authors Available")

    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date) if article.publish_date else "No Date Available")

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary if article.summary else "No Summary Available")

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0',
        f'Polarity: {analysis.polarity}, Sentiment: '
        f'{"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}'
    )

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
    
gui=t.Tk()
gui.title('News Summary Report')
gui.geometry('1200x600')
tlabel=t.Label(gui,text='Title')
tlabel.pack()
title=t.Text(gui,height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

alabel=t.Label(gui,text='Author')
alabel.pack()
author=t.Text(gui,height=1,width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel=t.Label(gui,text='Publication Date')
plabel.pack()
publication=t.Text(gui,height=1,width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel=t.Label(gui,text='Summary')
slabel.pack()
summary=t.Text(gui,height=20,width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

elabel=t.Label(gui,text='Sentiment Analysis')
elabel.pack()
sentiment=t.Text(gui,height=1,width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel=t.Label(gui,text='Enter URL')
ulabel.pack()

utext=t.Text(gui,height=1,width=140)
utext.pack()

bbutton=t.Button(gui,text='Summarize',command=summarize)
bbutton.pack()

gui.mainloop()


    
    
    


