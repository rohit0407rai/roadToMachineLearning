f=open('sample.text','r') #use open content to read the content of file
# data=f.read()
data =f.read(5)#it will read the opened file  and specifically it will read 5 chaacters only
print(data)#it will print the file thats been read
f.close()#aftering opening file , closing of file is good practice so that we can free the disk

