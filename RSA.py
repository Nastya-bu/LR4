import random

def main():
    n = e = d = 0
    n, e, f = public_keys()
    d = private_key(e,f)
    f = open('key.txt', 'w')
    f.write("Public keys: \n e = ")
    f.write(str(e))
    f.write("  n = ")
    f.write(str(n))
    f.write("\nPrivate keys: \n d = ")
    f.write(str(d))
    f.write("  n = ")
    f.write(str(n))
    f.close()
    encrypt (e,n)
    decrypt (d,n)
    

def public_keys():
    p = prost()
    q = prost()
    print("p: ",p)
    print("q: ",q)
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    f = (p - 1) * (q - 1)
    e = get_e(f)
    return [n, e, f]

def prost():
    """Генератор простого числа"""
    n =100
    a = list(range(n+1))
    a[1] = 0
    lst = []
    
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, (n+1), i):
                a[j] = 0
        i += 1
    i=0
    while lst[i] <= 17:
        lst.remove(lst[i]) 
    return random.choice(lst)

def is_prime(num):
    """Проверка простого числа"""
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def get_e(f):
    """Нахождение взаимно простого числа е"""
    e = 2
    while gcd(e, f) != 1:
        e += 1
    return e

def gcd(a,b):
    """нахождение НОД"""
    while b > 0:
        a, b = b, a % b
    return a


def gcdex(e, f):
    """ Расширенный алгоритм Евклида"""
    if f == 0:
        return e, 1, 0
    else:
        a, x, y = gcdex(f, e % f)
        return a, y, x - y * (e // f)

def private_key(e,f):
    """Нахождение d """
    x, d, y = gcdex(e, f)
    while d < 0:
        d += f
    return d

def encrypt (e,n):
    input = open('in.txt', 'r')
    output = open('output.txt','w')
    m = input.read(1)
    while len(m) > 0:
        c = (ord(m)**e)%n
        output.write(str(c))
        output.write("\n")
        m = input.read(1)
    input.close()
    output.close()

def decrypt (d,n):
    input = open('output.txt', 'r')
    output = open('dec.txt', 'w')
    m = input.readline()
    while len(m) > 0:
        c = (int(m)**d)%n
        output.write(chr(c))
        m = input.readline()
    input.close()
    output.close()



    

if __name__ == "__main__":
    main()
