#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#       (C) 2012 Alchimista <alchimistawp@gmail.com>
#         
#        Distributed under the terms of the GNU GPL license.



import wikipedia


site= wikipedia.Site("pt", "wikipedia") # definimos que o site é a pt.wp


wpage = wikipedia.Page(site, u"wikipédia:Página de testes/4")


wpagetext = wpage.get()

print wpagetext # print ao conteúdo da página


newtext = u"Olá Mundo! Isto é um teste de edição :D" # definimos o novo texto

wikipedia.showDiff(wpagetext, newtext) # mostra o diferencial da edição sem salvar
