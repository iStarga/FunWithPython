import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

x = str(input("Enter the title : "))
title = wikipedia.search(x)[0]
page = wikipedia.page(title)
text = page.content
print(text)
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", max_words=200, stopwords=stopwords)

wc.generate(text)
wc.to_file("result.png")
