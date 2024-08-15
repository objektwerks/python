# files and dirs

with open('requirements.txt', 'r') as f:
    data = f.read()
    print(f'read requirements.txt:\n\n{data}')

with open('test.txt', 'w') as f:
    data = 'test data'
    f.write(data)
    print('write text.txt')

