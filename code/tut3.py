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
	site = wikipedia.Site("pt", "wikipedia")
	cat = catlib.Category(site, u"!Robótica")

	pages = pagegenerators.CategorizedPageGenerator(cat)
	for page in pages:

		print page.title()
				
		pageNamespaceNumber = page.namespace()
		namespace = site.namespace(pageNamespaceNumber)
		if namespace == u"Ajuda":

			print len(page.get())
			print u"namespace: ", site.namespace(page.namespace())
			print u"templates: ", page.templates()

		elif namespace == u"Wikipédia":

			print u"namespace: ", site.namespace(page.namespace())
			print u"Página principal (título sem subpágina): ", page.sectionFreeTitle()
			print u"Página principal sem título nem namespace: ", page.title(withNamespace=False)
			
			
if __name__ == "__main__":
	try:
		main()
	finally:
		wikipedia.stopme()	