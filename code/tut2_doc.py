#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	   
#	   (C) 2012 Alchimista <alchimistawp@gmail.com>
#		 
#		Distributed under the terms of the GNU GPL license.

import sys, os

try:
	sys.path.append(os.environ['HOME'] + '/wp/bots/pywikipedia')
except:
	pass


import wikipedia
import catlib
import pagegenerators

def main():
	''' Esta é a def onde o nosso script vai estar '''
	
	site = wikipedia.Site("pt", "wikipedia") # definimos que o site é a pt.wp
	
	'''De seguida, definimos a categoria Ambiente
	 e obtemos a listagem dos títulos dos artigos.
	 Na demonstração o código está por extenso para
	 mais fácil percepção, na prática, bastaria
	 pages = catlib.Category(site, u"Ambiente").articles()
	 para se obter a listagem	  
	'''
	cat = catlib.Category(site, u"Ambiente") # Aqui definimos a categoria Ambiente. 
	catList = cat.articlesList()


	'''Agora que temos uma listagem,
	 e antes de contar os elementos,
	 vamos ver os títulos que constam na catList.
	 
	 Esta abordagem serve bem para ilustrar este exemplo,
	 caso fosse para interagir directamente com os artigos,
	 como veremos noutro post, há abordagens mais eficientes.
 
	 O primeiro print, ou seja, no caso o objecto page,
	 é um objecto python, enquanto que o segundo print,
	 o do page.title(), já tem o formato de unicode.
	'''
	
	for page in catList:
		print u"página (objecto):", page
		print u"Título da página: ", page.title() # mostra o título do artigo


	''' Por fim, fazemos a contagem dos artigos	'''
	
	print u"\n Nº de artigos na categoria: ", len(catList)
	
if __name__ == "__main__":
	try:
		main()
	finally:
		wikipedia.stopme()	