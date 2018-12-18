import csv
import os
import time
import io
import logging

log = logging.basicConfig(level=logging.DEBUG)
start = time.time()

# path = input('Copy and paste the folder path and hit enter.')
path = r'C:\Users\PATH TO FOLDER WITH XML FILES'
new_path = os.mkdir(os.path.join(path, 'Updates'))
print('\n', f'You are working inside {path}.', '\n')

# Iterate through all files in the provided path
def global_replace():
    breaker = False
    for file in os.listdir(path):
        if file.endswith('.xml'):
            with io.open(path + "\\" + file, 'r+', newline=None, encoding='utf-8') as openfile:
                openfile = openfile.read().replace("', '", ' ').replace('\n', ' ')
                f = open('globals.csv', 'r')
                f.seek(0)
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if row[0] in openfile and breaker:
                        print('\n', f"Found '{row[0]}' in {file}, replacing with '{row[1]}'.")
                        breaker = True
                    openfile = openfile.replace(row[0], row[1])
                    new_path = os.path.join(path, 'Updates', file)
                    changed = open(new_path, 'w', encoding='utf-8')
                    if row[0] not in openfile and not breaker:
                        print('\n', 'The below changes have been made.')
                        breaker = True
                changed.write(openfile)
                changed.close()


global_replace()

print('\n', f'This took {time.time() - start} seconds to run.')
