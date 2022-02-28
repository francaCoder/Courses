import os

# >>> import os
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
# >>> os.listdir()
# ['.idea', 'Curso em vídeo', 'DevAprender - Python', 'main.py', 'Mestre da Automação', 'Trash', 'venv']
# >>> os.chdir('Mestre da Automação')
# >>> os.chdir('03 Mestre dos Arquivos')
# >>> os.chdir('Classes')
# >>> os.chdir('CL023 Creating Directories')
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes\\Mestre da Automação\\03 Mestre dos Arquivos\\Classes\\CL023 Creating Directories'
# >>> os.mkdir('Musics')
# >>> os.makedirs('Musics' + os.sep + 'Hip-Hop') - Sub Folder


# os.path.isdir('Muscis')
if not os.path.isdir('Muscis'):
    os.mkdir('Musics')
else:
    print("[ERROR] This directory already exists!")