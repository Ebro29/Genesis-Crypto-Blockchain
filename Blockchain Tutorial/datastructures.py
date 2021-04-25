simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)
del(simple_list[0])#delete 1st value of the list

d = {'name': 'Max'} #Dictionary
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['name'])
print(d)

t = (1,2,3)
print(t.index(1))
#del(t[0]) CANT WORK BECAUSE TUPLES CANT BE EDITED

s = {'Max', 'Anna', 'Max'} #set (ignores duplicates)
print(s)


