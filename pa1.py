
def evalf(x,y):
    return ((3*x*y)+1)/((x**2)+1)


def sum_of_cubes(n):
    timer = 1
    totalsum = 0
    while timer<=n:
        totalsum = totalsum + timer**3
        timer = timer +1
    return totalsum

def is_prime(p):
    divider = p - 1
    remainder = 0

    while divider >=1:
        remainder = p%divider

        if divider == 1 :
            return 0 == 0
        elif remainder == 0:
            return 0 == 1
        else:
            divider = divider -1
            
        
    
