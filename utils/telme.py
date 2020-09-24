# coding:utf-8

# open file

telme_file = open('ressources/telme.txt', 'r', encoding='utf-8')
telme_text = telme_file.read()
telme_file.close()