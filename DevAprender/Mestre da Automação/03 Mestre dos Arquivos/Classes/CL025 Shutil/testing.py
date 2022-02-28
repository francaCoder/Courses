import shutil
import os

"""
shutil.copy()
shutil.copytree()
shutil.move()
shutil.rmtree()
shutil.make_archive()
shutil.unpack_archive()
"""

# Copy passwords.txt
os.getcwd()
os.chdir('..')
os.chdir('CL022')
shutil.copy(os.getcwd() + os.sep + 'passwords' + os.sep + 'passwords.txt', "CL025 Shutil")

# Copy folder
shutil.copytree("path main folder", "path distiny")

# Move any file
shutil.move("path main folder or file", "path distiny")

# Delete folder
shutil.rmtree("path foled")

# compact to zip
shutil.make_archive('exercise_shutil', 'zip', "path files")

shutil.unpack_archive('exercise_shutil.zip', 'exercises')