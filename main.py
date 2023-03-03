from measure.measure import *

A = Measure(3.43, .05)
B = Measure(.046, .002)
C = Measure(66.23, .03)
D = Measure(2.0045, .0005)
E = Measure(12.4, .7)
F = Measure(27, 3)
  
print('                 A+D: ', A+D)
print('             A+B+C+D: ',A+B+C+D)
print('         A+2*B-4*C+D: ',A+2*B-4*C+D)
print('           2*B^2+4*D: ',2*B**2 + 4*D)
print('                 A*B: ',A*B)
print('                 F/D: ',F/D)
print('               B^2/C: ',B**2/C)
print('E^2*A^3*B/(4*F^3*D^3: ',E**2 * A**3 * B/(4*F**3 * D**3))
