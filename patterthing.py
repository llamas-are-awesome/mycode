pattern = ['*']



for i in range(5):
    
    print(pattern)
    pattern.append('*')

for i in range(4):
    pattern.remove('*')
    print(pattern)
