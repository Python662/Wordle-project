import re

User_input = input('Enter Regular Expression: ')
try:
    with open('mbox-short.txt')  as file:
        num_list = []
        for line in file:
            if re.search(User_input,line):
                num_list.append(line)
                if len(num_list) !=0:
                    print(num_list)

except: FileNotFoundError
print('File not found')
quit()