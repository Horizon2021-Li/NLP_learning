# https://blog.edrone.me/en/word2vec/
tiny_corpus = ['edrone is awesome',
               'The first CRM for eCommerce and AI fueled marketing machine']
print(tiny_corpus, '\n')

# LOWER CASE
tiny_corpus_lowered = [sentence.lower() for sentence in tiny_corpus] # 把大写全部转为小写
print(tiny_corpus_lowered, '\n')

# TOKENIZATION
tiny_corpus_lowered_tokenized = [sentence.split() for sentence in tiny_corpus_lowered]
print(tiny_corpus_lowered_tokenized, '\n')

# DICTIONARY
words = [word for sentence in tiny_corpus_lowered_tokenized for word in sentence]
print(sorted(words), '\n')

unique_words = list(set(words)) # 去重

# ASIGN TO DICTIONARY
id2word = {nr: word for nr, word in enumerate(unique_words)} # enumerate(unique_words)：这个函数用于遍历列表 unique_words 中的元素，并返回每个元素以及其对应的索引（从零开始）的组合。这样，nr 变量将是每个单词在 unique_words 列表中的索引，而 word 变量将是对应的单词
print(id2word, '\n')

word2id = {word: id for id, word in id2word.items()}
print(word2id, '\n')

# ONE HOT ENCODING
from pprint import pprint
import numpy as np

num_word = len(unique_words)
word2one_hot = dict()

for i in range(num_word): # 生成一个矩阵 num_word*num_word，独热编码，对角线为1的对角矩阵diag
    zero_vec = np.zeros(num_word)
    zero_vec[i] = 1
    word2one_hot[id2word[i]] = list(zero_vec) # 把字符和编码对应起来

# RESULT
pprint(word2one_hot)

#--------------------------------上面是做独热编码-------------------------------

import gensim
import gensim.downloader as api # 导入 Gensim 的下载器模块，这个模块提供了一种简便的方式来下载和访问预训练的词向量模型

wv = api.load('word2vec-google-news-300')

vec_king = wv['king']
print(f"Embedding dimension is :{vec_king.shape}\n")
print(f"Embedding Vector of 'king' is :\n\n{vec_king}")
