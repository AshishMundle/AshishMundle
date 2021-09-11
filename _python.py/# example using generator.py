# example using generator 

def myname() :           #called function
    yield 'p'
    yield 'r'
    yield 'a'
    yield 's'
    yield 'h'
    yield 'a'
    yield 'n'
    yield 't'

output=myname()          #calling function
print(type(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))
print(next(output))