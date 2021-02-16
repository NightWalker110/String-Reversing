def reverse_string(j):
    j1 = ''
    for s in j:
        j1 = s + j1
    return j1
        
input_string = 'SHUBHAM'
print("reverse of string using for loop is : ",reverse_string(input_string))
