#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	   
#	   (C) 2012 Alchimista <alchimistawp@gmail.com>
#		 
#		Distributed under the terms of the GNU GPL license.



import wikipedia
import catlib
import pagegenerators

def main():
	
	site = wikipedia.Site("pt", "wikipedia") # definimos que o site é a pt.wp

	cat = catlib.Category(site, u"Ambiente") # Aqui definimos a categoria Ambiente. 
	catList = cat.articlesList()


	for page in catList:
		print u"página (objecto):", page
		print u"Título da página: ", page.title() # mostra o título do artigo

	print u"\n Nº de artigos na categoria: ", len(catList)
	
if __name__ == "__main__":
	try:
		main()
	finally:
		wikipedia.stopme()	