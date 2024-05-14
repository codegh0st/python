x = 100
y = 200

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y

def count_digit(num):
    c = 0
    while num>0:
        c = c+1
        num = num//10
    return c
if __name__ == '__main__':
    x=add(4,5)
    print(x)