{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang2057{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.22000}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 def smallest_multiple(n):\par
    if n <= 2:\par
        return n\par
    i = n * 2\par
    factors = [number for number in range(n, 1, -1) if number * 2 > n]\par
    print(factors)\par
    while True:\par
        for a in factors:\par
            if i % a != 0:\par
                i += n\par
                break\par
        if a == factors[-1] and i % a == 0:\par
            return i\par
\par
n = 13\par
result = smallest_multiple(n)\par
factors = [i for i in range(n, 0, -1)]\par
print(factors)\par
print(result)\par
}
 