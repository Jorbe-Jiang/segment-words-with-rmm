#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Jorbe
#Date: 2014.03.13
def make_dict(dict_file):
	words={}
	for index, word in enumerate(open(dict_file,"rU")):
		word=unicode(word.strip(),"utf-8")
		words["word"]=1
	#print words
	return words

#获取前k个字，如果从索引位置i开始到最前面的字数少于k个的话就取全部字
def get_k_words(text,i,k):
	if i+1<k:
		return text[0:i+1],i+1
	else:
		return text[i-(k-1):i+1],k

def segment_words(text,dict_words,k=5):
	seg_words=""
	i=len(text)-1
    while i>=0:
		tmp_words,length=get_k_words(text,i,k)
		#print tmp_words.encode("utf-8"),length,i
		tmp_len=0
		for j in range(length):
			if dict_words.has_key(tmp_words[j:length]):
				seg_words+=(tmp_words[j:length]+" ")
				tmp_len=length-j
				break
			if j==length-1 and not dict_words.has_key(tmp_words[j:length]):
				seg_words+=(tmp_words[j:length]+" ")
				tmp_len=length-j
		i=i-tmp_len
	#print seg_words.encode("utf-8")
	return seg_words

################################################
if __name__=="__main__":
	text=u"我爱北京天安门"
	dict_file="dict.txt"
	seg_words=""
	dict_words={}
	dict_words=make_dict(dict_file)
	seg_words=segment_words(text,dict_words)
	#print seg_words.encode("utf-8")
	words_list=seg_words.strip().split()
        words_list.reverse()
        seg_words=" ".join(words_list)
	#print seg_words.encode("utf-8")
