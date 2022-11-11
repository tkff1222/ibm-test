#n = input("n is ")
#list=[]
#for i in range(n):
#    record = input("record is ")
#    list.append(record.split())

n = 5
list = [['1', 'false', 'ERR_OOM'], ['2', 'true'], ['3', 'false', 'ERR_TIME_OUT'], ['4', 'true'], ['5', 'true']]

print(list)

allValid = True
errorCodes = []
for record in list:
    print(record)
    if (record[1] == 'false'):
        allValid = False
        errorCodes.append(record[2])

if allValid is True:
    print('Yes')
else:
    print('No')
    for i in errorCodes:
        print(i, end=" ")
    