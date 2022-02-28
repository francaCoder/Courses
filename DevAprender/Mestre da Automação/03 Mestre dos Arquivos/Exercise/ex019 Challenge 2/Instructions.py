"""
- Create a new folder inside the current folder, called 'Files'
- Using other command, create a new folder inside the directory 'files' called 'Files pdf'
- Using just one line, create a folder called 'photos' with 'summer photos' as sub-folder.
"""

"""
>>> import os
>>> os.getcwd()
'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
>>> os.chdir('Mestre da automação') 
>>> os.chdir('03 Mestre dos Arquivos') 
>>> os.chdir('Exercise') 
>>> os.chdir('ex019 Challenge 2') 
>>> os.mkdir('Files') 
>>> os.makedirs('Files' + os.sep + 'Files pdf') 
>>> os.chdir('..') 
>>> os.getcwd()
'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes\\Mestre da automação\\03 Mestre dos Arquivos\\Exercise'
>>> os.chdir('ex019 Challenge 2') 
>>> os.makedirs('photos' + os.sep + 'summer photos') 

"""