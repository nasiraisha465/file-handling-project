# open the file in read  mode
file_read = open('codingal.txt','r')
print("file in read mode -")
print(file_read.read)
file_read.close()
# open the file in write mode 
file_write  = open('codingal.txt','w')
# write in the file
file_write.write("file in write mode ....")
file_write.write("hi! I am a roy.I am in class. 8")
file_write.close()
# open the file in append mode
file_append = open('codingal.txt','a')
# append in the file 
file_append.write("\n File in append mode .....")
file_append.write("Hi! I am a roy. I am in class. 8")
file_append.close()