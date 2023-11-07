import os
python = lambda : os.system('apt install python')
python()
python3 = lambda : os.system('apt install python3')
python3()
requests = lambda : os.system('pip install requests')
requests()
clear = lambda : os.system('clear')
clear()
print('''
\033[93m done!
''')
