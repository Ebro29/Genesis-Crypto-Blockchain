#modes: r (read), w (write), r+ (read & write), x (write only), 
#a (write only by appened), #b (binary mode)
with open('demo.txt', mode='w') as f: #with keyword  
#f.write('Hello from Python!') #python will auto close the file and  not save anything without close
#file_content = f.read() #doesn't work with w, use r 
#PROBLEM - demo.txt data is overwritten to be blank
#f.write('Add this content!\n') #multiline
#file_content = f.read()

#file_content = f.readlines()
#f.close()
#for line in file_content: #read the entire file 
    #print(line[:-1])

#line = print(f.readline()) #read one line at a time
#while line:
#    print(line)
#    line = f.readline()
#f.close()
    f.write('Testing is this closes...')
user_input = input('Testing: ')
print('Done:')
