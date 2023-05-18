
import os

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('the file that you want to delete does not exit')

