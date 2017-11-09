# import gensim
import json
import _pickle as cPickle
# from keras.models import Sequential
# print ("test")
# model = gensim.models.KeyedVectors.load_word2vec_format('./word2vec/GoogleNews-vectors-negative300.bin', binary=True)
# print("Loaded google model")
"""
read_json
Author: Ranga

Sentence compression sample data is a dump of json objects one after the other. Standard json.read fails because its 
an invalid format.

This method reads document line by line. Counts open and closed paranthesis for determining end of document, then uses 
json.reads instead of directly reading from file.

json file is in utf8 format, encoding must be specified as utf8

"""

def read_json(filename):
	docs=[]
	with open(filename, encoding="utf8" ) as jsonfile:
		openbraces=0
		closed_braces=0
		doc=""
		for line in jsonfile:
			openbraces += line.count('{')
			closed_braces += line.count('}')
			doc += line
			if ( line.rstrip('\n') == "" ):
				continue
			# if ( openbraces ==0 and closed_braces == 0):
			# 	continue;
			if ( openbraces == closed_braces ):
				jdoc=json.loads(doc)
				# print (doc)
				# print ( "document: " + str(jdoc))
				# docs.append(jdoc)
				docs.append( {"sentence": jdoc["graph"]["sentence"],
				         "compressed": jdoc["compression"]["text"],
				         "compression_ratio": jdoc["compression_ratio"]} )
				doc = ""
				openbraces=closed_braces=0
	return docs

def unpickle(file):
    with open(file, 'rb') as fhandle:
        list_of_dicts = cPickle.load(fhandle, encoding='bytes')
    return list_of_dicts

def appendpickle(file,word2idx):
	with open(file, 'ab') as fhandle:
		cPickle.dump(word2idx, fhandle)

if __name__ == '__main__':
	path = 'C:\Amar\SMAI\Project\sentence-compression-1\data'
	file = path+'\\train.pickle'

	word2idx = read_json(path+'\\sent-comp.train01.json')
	appendpickle(path + '\\train01.pickle', word2idx)
	b = unpickle(path+'\\train01.pickle')

	if (word2idx == b):
		print (word2idx == b)
		appendpickle(file,word2idx)
	else:
		print('false')

	word2idx = read_json(path+'\\sent-comp.train02.json')
	appendpickle(path + '\\train02.pickle', word2idx)
	b = unpickle(path+'\\train02.pickle')

	if (word2idx == b):
		print (word2idx == b)
		appendpickle(file,word2idx)
	else:
		print('false')

	#FILE 3
	word2idx = read_json(path + '\\sent-comp.train03.json')
	appendpickle(path + '\\train03.pickle', word2idx)
	b = unpickle(path + '\\train03.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 4
	word2idx = read_json(path + '\\sent-comp.train04.json')
	appendpickle(path + '\\train04.pickle', word2idx)
	b = unpickle(path + '\\train04.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 5
	word2idx = read_json(path + '\\sent-comp.train05.json')
	appendpickle(path + '\\train05.pickle', word2idx)
	b = unpickle(path + '\\train05.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 6
	word2idx = read_json(path + '\\sent-comp.train06.json')
	appendpickle(path + '\\train06.pickle', word2idx)
	b = unpickle(path + '\\train06.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 7
	word2idx = read_json(path + '\\sent-comp.train07.json')
	appendpickle(path + '\\train07.pickle', word2idx)
	b = unpickle(path + '\\train07.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 8
	word2idx = read_json(path + '\\sent-comp.train08.json')
	appendpickle(path + '\\train08.pickle', word2idx)
	b = unpickle(path + '\\train08.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 9
	word2idx = read_json(path + '\\sent-comp.train09.json')
	appendpickle(path + '\\train09.pickle', word2idx)
	b = unpickle(path + '\\train09.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	#FILE 10
	word2idx = read_json(path + '\\sent-comp.train10.json')
	appendpickle(path + '\\train10.pickle', word2idx)
	b = unpickle(path + '\\train10.pickle')

	if (word2idx == b):
		print(word2idx == b)
		appendpickle(file, word2idx)
	else:
		print('false')

	final_list_of_dicts = unpickle(file)
	print(final_list_of_dicts)

