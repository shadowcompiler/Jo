# coding:utf-8

# open file

story_file = open('ressources/story.txt', 'r', encoding='utf-8')
story_text = story_file.read()
story_file.close()