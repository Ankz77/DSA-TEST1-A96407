{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang2057{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.22000}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 import numpy as np\par
\par
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])\par
\par
print("Original array:")\par
print(a)\par
\par
print("Checking for complex number:")\par
print(np.iscomplex(a))\par
\par
print("Checking for real number:")\par
print(np.isreal(a))\par
\par
print("Checking for scalar type:")\par
print(np.isscalar(3.1))\par
print(np.isscalar([3.1]))\par
}
 