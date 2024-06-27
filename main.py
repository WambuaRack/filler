import os 
from random import randint

for i in range(1,20):
    for j in range(0, randint(1, 100)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Add a newline after each date
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "Commit ' + d + '"')

os.system('git push -u origin main')
