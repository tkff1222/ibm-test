n = input("N is ")
size = input('Enter a list of size separated by space ')
m = input('M is ')
req_size = input('Enter a list of size separated by space ')
size_list = size.split()
req_size_list = req_size.split()

#n = 5
#m = 4
#size_list=['XL','XXXXXXXXXL','XXS','M','XXS']
#req_size_list=['L','M','L','XXS']

print('size_list: ', size_list)
print('req_size_list: ', req_size_list)

taken=[]
for j in range(n):
    taken.append(False)

countTaken=0
for i in req_size_list:
    for j in range(n):
        pos = size_list[j].find(i)
        if (pos != -1 and taken[j] is False):
            taken[j] = True
            countTaken = countTaken +1
            break

print(countTaken)
if (countTaken == m):
    print('Yes')
else:
    print('No')
