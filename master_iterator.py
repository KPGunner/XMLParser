from change_dict import *
import os
import time

start = time.time()

# path = input('Copy and paste the folder path and hit enter.')
path = r'<PATH GOES HERE>'
new_path = os.mkdir(os.path.join(path, 'Updates'))
print('\n', f'You are working inside {path}.', '\n')

# Iterate through all files in the provided path
def global_replace():
    for file in os.listdir(path):
        if file.endswith('.xml'):
            with open(path + "\\" + file) as openfile:
                orig_files = openfile.read()
                for aPair in Changes:
                    orig_files = orig_files.replace(aPair[0], aPair[1])
                    new_path = os.path.join(path, 'Updates', file)
                changed = open(new_path, 'w', encoding='utf-8')
                changed.write(orig_files)
                changed.close()
                openfile.close()


global_replace()

print(f'This took {time.time() - start} seconds to run.')
