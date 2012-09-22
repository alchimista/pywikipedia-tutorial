#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#       (C) 2012 Alchimista <alchimistawp@gmail.com>
#         
#        Distributed under the terms of the GNU GPL license.

import sys, os

try:
	sys.path.append(os.environ['HOME'] + '/wp/bots/pywikipedia')
except:
	pass

''' 
 Primeiro importamos o módulo wikipedia, o qual nos trará as soluções mais básicas,
 e ao mesmo tempo grande parte das que normalmente são necessárias para interagir com
 o mediawiki. '''

import wikipedia

''' O primeiro passo antes de interagir com a API do mediawiki, é definir
qual o projecto/site com que estamos a lidar, para isso usamos:
'''
site= wikipedia.Site("pt", "wikipedia") # definimos que o site é a pt.wp

''' Agora, vamos estabelecer as definições de uma página, neste caso,
 a página de testes/4: '''

wpage = wikipedia.Page(site, u"wikipédia:Página de testes/4")

''' Agora que definimos a página, vamos obter o texto da página: '''
wpagetext = wpage.get()

print wpagetext # print ao conteúdo da página

''' Tendo o conteúdo, e ignorando-o por completo, vamos então substituir
 por um novo texto.
'''
newtext = u"Olá Mundo! Isto é um teste de edição :D" # definimos o novo texto

wikipedia.showDiff(wpagetext, newtext) # mostra o diferencial da edição sem salvar
