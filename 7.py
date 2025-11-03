import itertools

def apply_it(n, o):
    """
    given a list of numbers, take 2 at a time, and apply operators
    and return the result
    """
    if len(o) == 0:
        return n[0]

    a,b = n[0:2]
    
    return apply_it( [o[0](a,b)] + n[2:], o[1:])


def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def combine(a,b):
    return int( str(a) + str(b) )

#with open("data/7_demo.txt") as f:
with open("data/7.txt") as f:

    correct_totals = 0

    for line in f:
        total , numbers = line.strip().split(':')
        total = int(total)
        numbers = list(map(int, numbers.strip().split(" ")))

        # choices in base <current_base>
        choices = [[add, mult, combine]] * (len(numbers)-1)

        for c in itertools.product( *choices):
            _t = apply_it( numbers, c) 
            if _t == total:
                #print(numbers, total, c)
                correct_totals += total
                break

print(correct_totals)
