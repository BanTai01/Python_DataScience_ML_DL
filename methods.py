def functions(name):
    print(name, 'Refsnes')
functions("Email")
functions("Linus")

def f_functions(fname, lname):
    print(fname,lname)
f_functions('zahid', 'hasan')

#Lamda (annonymus function)
add = lambda x, y: x + y
print(add(3,4))


#w3 school
def myfunc(n):
    return lambda a : a * n
doubler = myfunc(2)
print(doubler(9))