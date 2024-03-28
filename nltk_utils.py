#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 分词：
import nltk

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
print(tokens)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)

#---------------------------------------------------------------------------------------------#
# 词性标注：
import nltk

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

# 输出：
# [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN'), ('.', '.')]

#---------------------------------------------------------------------------------------------#
# 去除停用词：
import nltk
from nltk.corpus import stopwords

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)

stop_words = set(stopwords.words('english'))

filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
print(filtered_tokens)

# 输出：
# ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', '.']

#---------------------------------------------------------------------------------------------#
# 词干提取：
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
words = ["connect", "connects", "connected", "connecting", "connection", "connections"]

for word in words:
    stem_word = stemmer.stem(word)
    print(stem_word)

# 输出：
# connect
# connect
# connect
# connect
# connect
# connect


#---------------------------------------------------------------------------------------------#
# 词行归一化
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = ["ran", "running", "runs", "goes", "went", "gone", "cars"]

for word in words:
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(lemma)

# 输出：
# run
# run
# run
# go
# go
# go
# cars
