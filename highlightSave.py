# highlightSave.py
# Creates a 'highlights' folder that will create a new text file each time
# the program is run. As the program runs, any new text that is copied to
# the clipboard (ctrl + c) will be automatically written into the text file

import pyperclip, os, time

#-----Note: If you are not running windows, you need to change the path to your home directory-----#

# Creates the necessary folders and files
if not os.path.exists('C:\\highlights'):
    os.makedirs('C:\\highlights\\')
print('What do you want the file to be called?')
name = input()
while os.path.exists('C:\\highlights\\' + name + '.txt'):
    print('This file already exists! Call it something else')
    name = input()
print('Creating ' + name + '.txt....')
file = open('C:\\highlights\\%s.txt' % name, 'a')

# Monitors paperclip and writes in all highlights
text = pyperclip.paste()
print('Highlight an empty space to stop the program')
print('The following are being copied:')
while text != ' ':
    if text != pyperclip.paste():
        file.write(text + '\n')
        text = pyperclip.paste()
        print(text)
        time.sleep(1)

print('Done.')
file.close()
