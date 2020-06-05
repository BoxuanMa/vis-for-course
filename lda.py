# -*- coding: utf-8 -*
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
chachedWords = stopwords.words('english')
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import csv
import numpy as np
np.set_printoptions(threshold=np.inf)

doc_set=[]
f=open("syllabus_en.csv", "r", encoding='utf-8')

reader=csv.reader(f)

for item in reader:
    doc_set.append(item[3])

tokenizer = RegexpTokenizer(r'\w+')
en_stop = stopwords.words('english')
p_stemmer = PorterStemmer()
texts = []

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    stopped_tokens = [i for i in tokens if not i in en_stop]

    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=1,no_above=0.8)
dictionary.filter_n_most_frequent(5)

corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word=dictionary, update_every=5, chunksize=10000, passes=100)
print(ldamodel.print_topics(num_topics=6,num_words=15))

vec=[]
for text in texts:
    bow = dictionary.doc2bow(text)
    a=ldamodel.get_document_topics(bow)
    vec.append(a)
matrix = gensim.matutils.corpus2dense(vec, num_terms=6)

np.savetxt("matrix.txt", matrix.T, fmt="%.5f", delimiter=",")


