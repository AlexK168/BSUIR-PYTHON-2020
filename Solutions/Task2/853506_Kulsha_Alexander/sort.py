import tempfile
import random

def initial_chunks():
    data = []
    temp_files = []
    with open("numbers.txt", buffering = 4000000) as f:
        i = 0
        for line in f:
            data.append(int(line))
            i += 1  
            if i == 700000: # nums amount in each file
                tmp = tempfile.TemporaryFile(mode = "w+")
                data.sort()
                tmp.writelines('{}\n'.format(value) for value in data)
                temp_files.append(tmp)
                data.clear()
                i = 0          
        if i > 0:
            tmp = tempfile.TemporaryFile(mode = "w+")
            data.sort()
            tmp.writelines('{}\n'.format(value) for value in data)
            temp_files.append(tmp)
            data.clear()
    return temp_files

def merge(f1, f2): #merges two files in one and returns merged file
    result = tempfile.TemporaryFile(mode = "w+")
    str1 = f1.readline()
    str2 = f2.readline()
    while str1 != '' and str2 != '':
        num1 = int(str1) 
        num2 = int(str2)
        if num1 < num2:
            result.write("{}\n".format(num1))
            str1 = f1.readline()
        else:
            result.write("{}\n".format(num2))
            str2 = f2.readline()
    if str2 != '':
        while str2 != '':
            num = int(str2)
            result.write("{}\n".format(num))
            str2 = f2.readline() 
    if str1 != '':
        while str1 != '': 
            num = int(str1)
            result.write("{}\n".format(num))
            str1 = f1.readline()
    f1.close()
    f2.close()
    return result

def output():
    chunks = initial_chunks()
    for i in chunks:
        i.seek(0)
    while len(chunks) > 1:
        for i in range(0, int(len(chunks) / 2), 1):
            f = merge(chunks[i], chunks[i + 1])
            f.seek(0)
            del chunks[i]
            del chunks[i]
            chunks.insert(i, f)  
    line = chunks[0].readline() 
    with open("output.txt",'w+') as f:
        while line != '':
            f.write(line)
            line = chunks[0].readline()
    chunks[0].close()
