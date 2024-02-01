import nltk 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re as r
nltk.download('stopwords')
nltk.download('punkt')

englishStopWords = set(stopwords.words("english"))

Text = ["hello, python is a great language", "python is not a good programming language"," C++ has been used for years", " I loved that movie [12]" ]

steamedText = PorterStemmer()



def talkToPc(phrase):
  steamedTextTable  = []
  for text in phrase:
    text= r.sub('\[[^]]*\]','',text)
    text= r.sub(r'[^a-zA-Z0-9\s]','',text)
    text= steamedText.stem(text)
    text= word_tokenize(text)
    for word in text:
      if(word not in englishStopWords):
        steamedTextTable.append(word)
  return " ".join(steamedTextTable)
  
print(talkToPc(Text))

#SENTIMENT ANALYSER-------------------------------------------------------------------------------------------------------------
from nltk.sentiment import SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()
print(sentiment.polarity_scores(fullsentence))

#EXERCICE 2-----------------------------------------------------------------------------------------------------------

#La base contient 1000 documents, calculer la TF-IDF du mot "compteur" dans le
#document d, sachant que le document d contient 3 fois le mot compteur et que 70 textes
#contiennent également le mot "compteur"

#TFIDF(,wd) = TF(w,d)log(N/DFw)
#TFIDF("compteur",d) = 3 log(1000/70) = 11.5

#Le mot "compteur" apparaît toujours 3 fois dans le document mais apparait cette fois
#dans 900 documents 

#TFIDF("compteur",d) = 3 log(1000/900) = 0.45

