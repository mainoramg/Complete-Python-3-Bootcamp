def myfunc0(name):
    print('Hello {}'.format(name))

myfunc0('Mainor')

def myfunc2(flag):
    if flag:
        return 'Hello'
    else:
        return 'Goodbye'

print(myfunc2(True))
print(myfunc2(False))

def myfunc3(*args):
    return [x for x in args if x%2 == 0]

print(myfunc3(1,2,3,4,5,6,7,8,9,10))

def myfunc(text):
    result = ''
    for i,c in enumerate(text):
        if i % 2 == 0:
            result += c.upper()
        else:
            result += c.lower()
    return result

print(myfunc('mainor'))
print(myfunc('MIRANDA'))

def old_macdonald(name):
    result = ''
    for i,letter in enumerate(name):
        if i == 0 or i == 3:
            result += letter.upper()
        else:
            result += letter.lower()
    return result
print(old_macdonald('mainor'))

def master_yoda(text):
    result = text.split(" ")
    result.reverse()
    return " ".join(result)

print(master_yoda('I am home'))