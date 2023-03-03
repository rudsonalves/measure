from measure.measure import *

def test_measure():
  A = Measure(12.2, .2)
  B = Measure(3.7, .5)
  C = Measure(0.52, .05)
  
  # Sum and subtractions tests
  assert (A+B).round(5) == Measure(15.9, .7)
  assert (A-B).round(5) == Measure(8.5, .7)

  # Sum with float
  assert A+2. == Measure(14.2, .2)
  assert 2.+A == Measure(14.2, .2)
  assert A-2. == Measure(10.2, .2)
  assert 2.-A == Measure(-10.2, .2)

  # Sum with int
  assert A+2 == Measure(14.2, .2)
  assert 2+A == Measure(14.2, .2)
  assert A-2 == Measure(10.2, .2)
  assert 2-A == Measure(-10.2, .2)

  # Product with int
  assert A*2 == Measure(24.4, .4)
  assert 2*A == Measure(24.4, .4)

  # Product with float
  assert A*2. == Measure(24.4, .4)
  assert 2.*A == Measure(24.4, .4)

  # Product with Measure
  assert (A*B).round(5) == Measure(45.14, 6.84)
  assert (B*A).round(5) == Measure(45.14, 6.84)

  # Division with int
  print(A/2)
  assert (A/2).round(5) == Measure(6.1, .1)
  print(2/A)
  assert (2/A).round(5) == Measure(0.16393, 0.00269)
  
  # Division with float
  print(A/2.)
  assert (A/2.).round(5) == Measure(6.1, .1)
  print(2./A)
  assert (2./A).round(5) == Measure(0.16393, 0.00269)

  # Division with Measere
  print(A/B)
  assert (A/B).round(5) == Measure(3.2973, 0.49963)

  # Power with int
  print(B**2)
  assert (B**2).round(5) == Measure(13.69, 3.7)
  print(2**B)
  assert (2**B).round(5) == Measure(13.78438, 4.59479)

  # Power with float
  print(B**2.)
  assert (B**2.).round(5) == Measure(13.69, 3.7)
  print(2.**B)
  assert (2.**B).round(5) == Measure(13.78438, 4.59479)

  # Power with Measure
  print(A**B)
  assert (A**B).round(5) == Measure(10459.99251, 634.45856)

  # Trigonometric Functions
  print(sin(C))
  assert sin(C).round(5) == Measure(.49626, .04337)
  print(cos(C))
  assert cos(C).round(5) == Measure(.86673, .02483) 
  print(tan(C))
  assert tan(C).round(5) == Measure(.57447, .06650)
  print(asin(C))
  assert asin(C).round(5) == Measure(.54790, .05861)
  print(acos(C))
  assert acos(C).round(5) == Measure(1.02290, .05861)
  print(atan(C))
  assert atan(C).round(5) == Measure(0.47871, .03935)

  # log e log10
  print(log(A))
  assert log(A).round(5) == Measure(2.50130, 0.01639)
  print(log10(A))
  assert log10(A).round(5) == Measure(1.08630, 0.00712)

  # rad2deg and deg2rad
  print(rad2deg(A))
  assert rad2deg(A).round(5) == Measure(699.00851, 11.45916)
  print(deg2rad(A))
  assert deg2rad(A).round(5) == Measure(0.21293, 0.00349)

  # cos/sin maximum/minimum limits
  C = deg2rad(Measure(89, 2))
  print(rad2deg(C))
  assert sin(C).round(5) == Measure(.99931, .00069)
  C = deg2rad(Measure(179, 2))
  print(rad2deg(C))
  assert cos(C).round(5) == Measure(-.99931, .00069)
  C = deg2rad(Measure(1, 2))
  print(rad2deg(C))
  assert cos(C).round(5) == Measure(.99931, .00069)

  # acos/sin/tan limits
  # C = Measure(.99, .02)
  # print(asin(C))
  # assert asin(C).round(5) == Measure(.99931, .00069)
