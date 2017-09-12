# -*- coding: utf-8 -*-
import codecs

def isEnglish(s):
    try:
        s.decode('ascii')
    except:
        return False
    return True

def search(fdir, query):
	f = codecs.open(fdir, 'r', 'utf-8')
	reverse = not isEnglish(query)
	if reverse:
		query = query[::-1]
		
	# query = query.decode('utf-8').lower() # [::-1] for persian
	query = query.lower() # [::-1] for persian
	# query = unicode(query).encode('utf-8').lower() # [::-1] for persian

	ret = []
	for line in f:
		if query in line.lower():
			if reverse:
				line = line[::-1]
			ret.append(line)

	f.close()
	return ret



