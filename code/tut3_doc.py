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
	site = wikipedia.Site("pt", "wikipedia")
	cat = catlib.Category(site, u"!Robótica")
	''' Como explicado anteriormente, temos definido o site e a categoria
		podendo então passar-mos a obter a listagem das páginas,
		onde desta vez usaremos o pagegenerators. Uma opção mais rápida será
		usar igualmente o preloadingGen, bastando para isso
		fazer algo como 
		pages = pagegenerators.PreloadingGenerator(pagegenerators.CategorizedPageGenerator(cat))
		Isto faz com que as páginas sejam carregadas no início, ao contrário
		do script actual, que carrega à medida que forem necessárias. 
	'''
	pages = pagegenerators.CategorizedPageGenerator(cat)
	for page in pages:
		'''Agora que temos a iteração vamos primeiro obter o título
		'''
		print page.title()
		
		''' Com o page.namespace() obtemos o namespace da página
			embora no formato canonico, ou seja, número. Para obter
			o nome do namespace, fazemos o site.namespace().
			Para fazer tudo junto, basta substituir as duas linhas por
			namespace = site.namespace(page.namespace())
		'''
		
		pageNamespaceNumber = page.namespace()
		namespace = site.namespace(pageNamespaceNumber)
		if namespace == u"Ajuda":
			''' Aqui filtramos as páginas que pertencem ao namespace Ajuda
				e obteremos o nome do namespace, assim como as predefinições
				contidas nas páginas. '''
			print len(page.get())
			print u"namespace: ", site.namespace(page.namespace())
			print u"templates: ", page.templates()
		elif namespace == u"Wikipédia":
			''' Neste bloco, apenas os artigos do namespace wikipédia são filtrados,
				e obteremos o namespage e o título do artigo, sem namespace ou subpáginas
				(resumidamente, o título do artigo principal)
			'''
			print u"namespace: ", site.namespace(page.namespace())
			print u"Página principal (título sem subpágina): ", page.sectionFreeTitle()
			print u"Página principal sem título nem namespace: ", page.title(withNamespace=False)
			
			
if __name__ == "__main__":
	try:
		main()
	finally:
		wikipedia.stopme()	