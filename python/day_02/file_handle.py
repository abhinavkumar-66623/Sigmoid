f=open('textfile.txt','w')
print('file name: ',f.name)
print('file mode: ',f.mode)
print('is readable: ',f.readable())
print('is writable: ',f.writable())
print('is closed: ',f.closed)
f.close()
print('is closed: ',f.closed)


f1=open('textfile1.txt','w')

for i in range(25):
    f1.write('the sample page id'+ str(i) +'\n')

f1.close()


f2=open('textfile1.txt','r')

print(f2.read())

lines=f2.readlines()
for l in lines:
    print(l.strip())


with open('anotherfile.txt','a') as f:
    for i in range(25):
        f.write('hii')
