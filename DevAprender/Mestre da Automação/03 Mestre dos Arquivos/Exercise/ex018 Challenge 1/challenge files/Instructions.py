"""
Create a new folder called 'challenge files' with 3 files inside it:
- prices.txt
- report.pdf
- birthday.xlsx
After that, create a sub-folder called 'challenges.txt' and inside it create more 3 files:
- challenge text1.txt
- challenge.text2.txt
- challenge text3.txt

Now do the following:
1 - Show all files of that folder
2 - Make and show the path of the 3 files of the current folder
3 - Make and show the path that are inside sub-folders
4 - Navigate to the 3 folders use the 'os.chdir()'
    1. Navigate to the folder 'challenges text'
    2. Navigate back the folder 'challenge files'
    3. Navigate to the main directory of folder files
"""


# 1

# >>> import os
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
# >>>
# >>> os.listdir()
# ['.idea', 'Curso em vídeo', 'DevAprender - Python', 'main.py', 'Mestre da Automação', 'Trash', 'venv']
# >>> os.chdir('Mestre da Automação')
# >>> os.listdir()
# ['01 Bootcamp Python', '02 Mestre da Web', '03 Mestre dos Arquivos']
# >>> os.chdir('03 Mestre dos Arquivos')
# >>> os.listdir()
# ['Classes', 'Exercise', 'Projects']
# >>> os.chdir('Exercise')
# >>> os.listdir()
# ['ex018 Challenge 1']
# >>> os.chdir('ex018 Challenge 1')
# >>> os.listdir()
# ['challenge files']

# 2
# >>> os.chdir('challenge files')
# >>> os.listdir()
# ['birthday.xlsx', 'challenges text', 'Instructions.py', 'prices.txt', 'report.pdf']

# 3
# os.chdir('..')

# 4
# os.chdir('File Name :)')