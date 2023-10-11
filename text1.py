n = eval(input('请输入一个整数:'))
filepath = "C:/Users/tom20/Desktop/input.txt"
fi = open(filepath,'r')
l = list()
line = fi.readlines()
for line in line:
    v = line.strip()
    b = v.split(',')
    l.append(b)
string = ''.join([''.join(sublist)for sublist in l])
lst = [string[i:i+64]for i in range(0,len(string),64)]
for j in range(0,n):
    count = 1
    for k in range(j+1,len(lst)):
        if lst[j] == lst[k] :
            count+=1      
    print(count,end = ' ')     