from change_dict import *
import os

# path = input('Copy and paste the folder path and hit enter.')
path = r'Path to your files'
print('\n', path, '\n')


def global_replace():
    for file in os.listdir(path):
        if file.endswith('.xml'):
            with open(path + "\\" + file) as openfile:
                orig_files = openfile.read()
                for aPair in Changes:
                    orig_files = orig_files.replace(aPair[0], aPair[1])
                    # output = orig_files
                changed = open(path, 'w')
                changed.write(orig_files)
                changed.truncate()
    print(f'{file} successfully updated')


global_replace()
