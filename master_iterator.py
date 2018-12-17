import csv
import os
import time
import io

start = time.time()
globals_file = open('globals.csv', 'r')

# path = input('Copy and paste the folder path and hit enter.')
path = r'C:\Users\kgunn\PycharmProjects\xml_parse_test\Test'
new_path = os.mkdir(os.path.join(path, 'Updates'))
print('\n', f'You are working inside {path}.', '\n')

# Iterate through all files in the provided path
def global_replace():
    for file in os.listdir(path):
        if file.endswith('.xml'):
            with io.open(path + "\\" + file, 'r+', newline=None, encoding='utf-8') as openfile:
                openfile = openfile.read().replace("', '", ' ').replace('\n', ' ')
                f = open('globals.csv', 'r')
                f.seek(0)
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    openfile = openfile.replace(row[0], row[1])
                    new_path = os.path.join(path, 'Updates', file)
                    changed = open(new_path, 'w', encoding='utf-8')
                changed.write(openfile)
                changed.close()


global_replace()

print('\n', f'This took {time.time() - start} seconds to run.')
