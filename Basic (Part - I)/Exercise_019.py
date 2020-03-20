def addLS(str):
    if(str[0:2] == 'ls'):
        return str
    else:
        return 'ls' + str

print(addLS('aasdf'))
print(addLS('lsasdf'))