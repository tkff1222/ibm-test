#n = input("N is ")
#size = input('Enter a list of size separated by space ')
#m = input('M is ')
#req_size = input('Enter a list of size separated by space ')
#size_list = size.split()
#req_size_list = req_size.split()

n = 5
m = 4
size_list=['XL','XXXXXXXXXL','XXS','M','XXS']
req_size_list=['L','M','L','XXS']

print('size_list: ', size_list)
print('req_size_list: ', req_size_list)

taken=[]
n = int(n)
m = int(m)
for j in range(n):
    taken.append(False)

countTaken=0
for i in req_size_list:
    for j in range(n):
        pos = size_list[j].find(i)
        # take the shirt if it is the exact size
        if (pos == 0 and taken[j] is False):
            taken[j] = True
            countTaken = countTaken +1
            print(size_list[j], " is taken by ", i)
            break
        
        if ('S' in i):
            pos = size_list[j].find('M')
            if (pos == -1):
                pos = size_list[j].find('L')
        elif ('M' in i):
            pos = size_list[j].find('L')

        # if not exact size found then take a larger size
        if (pos != -1 and taken[j] is False):
            taken[j] = True
            countTaken = countTaken +1
            print(size_list[j], " is taken by ", i)
            break

print(countTaken)
if (countTaken == m):
    print('Yes')
else:
    print('No')
