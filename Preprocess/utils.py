


import re
import os
import sys


import pandas as pd
import numpy as np
import spacy


from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

def _get_wordcounts(x):
	length = len(str(x).split())
	return length

def _get_charcounts(x):
	s = x.split()
	x = ''.joins(s)
	return len(x)

def _get_avg_wordlength(x):
	count = _get_charcounts(x)/_get_wordcounts(x)
	return count


def _get_stopwords_counts(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

def _get_hashtags_counts(x):
    l = len([t for t in x.split() if t.startswith('@')])
    return l

def _get_mentions_counts(x):
	l = len([t for t in x.split() if t.startswith('#')])
	return l

def _get_digit_counts(x):
	l = len([t for t in x.split()if t.isdigit()])
	return l

def _get_uppercase_counts(x):
	l = len([t for t in x.split() if t.isupper()])
	return l
def _get_emails(x):
	emails =  re.findall(r'([a-z0-9+._-]+@)[a-Z0-9+._-]+\.[a-z0-9+._-]+\b)', x)
	counts = len(emails)
	return counts, emails


def _remove_emails(x):
	return re.sub(r'(([a-z0-9+._-]+@)[a-Z0-9+._-]+\.[a-z0-9+._-]+\)',"", x)

def _remove_special_chars(x):
	x = re.sub(r'[^\w ]+',"", x)
	x = ' '.join(x.split())
	return x

def _remove_html_tags(x):
	return BeautifulSoup(x, 'html.parser').get_text().strip()

def _remove_accented_chars(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x
def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords]) 


def make_base(x):
	x = str(x)
	x_list = []
	doc = nlp(x)

	for token in doc:
		lemma = token.lemma_
		if lemma == '-PRON-' or lemma == 'be':
			lemma = token.text

		x_list.append(lemma)
	return ' '.join(x_list) 

def _remove_common_words(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn =freq_comm[:n]
	x=  ' '.join([t for t in x.split() if t not in fn])
	return x

def _removerarewords(x, n= 20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm.tail(n)
	x = ' '.join([t for t in x.split() if t not in rare])
	return x
def _spelling_correction(x):
	x = TextBlob(x).correct()
	return x

