import csv
import random
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer


greet_in = ('hey', 'sup', 'waddup', 
            'wassup', 'hi', 'hello', 'good day','ola', 
            'bonjour', 'namastay', 'hola', 'heya', 'hiya', 'howdy',
'greetings', 'yo', 'ahoy')
greet_out = ['hey', 'hello', 'hi there', 'hi', 'heya', 'hiya', 
             'howdy', 'greetings', '*nods*', 'ola', 'bonjour', 'namastay']

def greeting(sent):
   for word in sent.split():
      if word.lower() in greet_in:
         return random.choice(greet_out)

small_talk_responses = {
'how are you': 'I am fine. Thankyou for asking ',
'how are you doing': 'I am fine. Thankyou for asking ',
'how do you do': 'I am great. Thanks for asking ',
'how are you holding up': 'I am fine. Thankyou for asking ',
'how is it going': 'It is going great. Thankyou for asking ',
'goodmorning': 'Good Morning ',
'goodafternoon': 'Good Afternoon ',
'goodevening': 'Good Evening ',
'good day': 'Good day to you too ',
'whats up': 'The sky ',
'sup': 'The sky ',
'thanks': 'Dont mention it. You are welcome ',
'thankyou': 'Dont mention it. You are welcome ',
'thank you': 'Dont mention it. You are welcome '
}
small_talk = small_talk_responses.values()
small_talk = [str (item) for item in small_talk]
def tfidf_cosim_smalltalk(doc, query):
   query = [query]
   tf = TfidfVectorizer(use_idf=True, sublinear_tf=True)
   tf_doc = tf.fit_transform(doc)
   tf_query = tf.transform(query)
   cosineSimilarities = cosine_similarity(tf_doc,tf_query).flatten()
   related_docs_indices = cosineSimilarities.argsort()[:-2:-1]
   if (cosineSimilarities[related_docs_indices] > 0.7):
      ans = [small_talk[i] for i in related_docs_indices[:1]]
      return ans[0]


def train(data):
  reader = csv.reader(data)
  corpus = {}
  for row in reader:
    corpus[row[0]] = {row[1]: row[2]}
   
  all_text = corpus.values()
  all_text= [str (item) for item in all_text]
  return all_text


def stem_tfidf(doc, query):
   query = [query]
   p_stemmer = PorterStemmer()
   tf = TfidfVectorizer(use_idf=True, sublinear_tf=True,
                        stop_words=stopwords.words('english'))
   stemmed_doc = [p_stemmer.stem(w) for w in doc]
   stemmed_query = [p_stemmer.stem(w) for w in query]
   tf_doc = tf.fit_transform(stemmed_doc)
   tf_query = tf.transform(stemmed_query)
   return tf_doc, tf_query
   
def cos_sim(data,a, b):
   cosineSimilarities = cosine_similarity(a, b).flatten()
   related_docs_indices = cosineSimilarities.argsort()[:-2:-1]
   if (cosineSimilarities[related_docs_indices] > 0.5):
      ans = [data[i] for i in related_docs_indices[:1]]
      for item in ans:
         c, d = item.split(':')
         d=d[:-1]
         d=eval(d)
         return d
   else:
      k = 'I am sorry, I cannot help you with, this one. Hope to in the future. Cheers :)'
      return k


# f = open('C:/Users/mishr/Desktop/project/Dataset.csv', 'r', encoding='utf-8')

# all_text=train(f)

# sametest="hello"

def responce(data,query):
  if(greeting(query)!=None):
              print(greeting(query))
              return greeting(query)
  elif(tfidf_cosim_smalltalk(small_talk_responses, query)!=None):
      x = tfidf_cosim_smalltalk(small_talk_responses, query)
      print(x)
      return x
  else:
      a, b = stem_tfidf(data, query)
      g = cos_sim(data,a, b)
      print(g)
      return g

# responce(all_text,"hi")


