from line_profiler import LineProfiler

def do_stuff():
    result = []
    for x in range(100000):
        result.append(x ** 2)
    return result

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


lp = LineProfiler()

lp.add_function(do_stuff)
lp.add_function(fact)

lp.run('do_stuff()')
lp.run('fact(100)')

lp.print_stats()

l=[1,2,4]

mp=list(map(lambda x:x**3,l))
print(mp)

input=[1,2,3,4]
def add(*n):
    return sum(*n)

def fun(add,input):
    print("First func:")
    return add(input)

print(fun(add,input))


    

