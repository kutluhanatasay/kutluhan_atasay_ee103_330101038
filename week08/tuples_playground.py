seq = (2, 'a', 4, (1, 2))
print(seq)
#import pdb; pdb.set_trace()

x = 1
y = 2

print(x,y)

(x, y) = (y, x)

print(x,y)

ex_name = 'Kutluhan Atasay'

def name_spliter(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[1]
    return(first_name, last_name)



print(name_spliter(ex_name)[0])
print(name_spliter(ex_name)[1])



def vovel_counter(full_name):
    v_counter = 0
    c_counter = 0
    vovels = 'aeiou'
    for i in range(len(full_name)):
        if full_name[i].lower() in vovels:
           v_counter += 1
        elif full_name[i].isalpha():
            c_counter += 1
    return(v_counter, c_counter)

print(vovel_counter(ex_name))

