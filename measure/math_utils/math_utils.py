import measure.measure as M
import math


# Mathmatical constants
pi = math.pi
e = math.e


def function(a, func):
  if isinstance(a, M.Measure):
    f0 = func(a.value + a.delta)
    f1 = func(a.value - a.delta)
    return M.Measure((f0+f1)/2, abs(f0-f1)/2)
  else:
    raise Exception('Measure function does not support "{}" parameter'.format(M.getType(a)))


def pow(a, b):
  if isinstance(a, int) | isinstance(a, float):
    if isinstance(b, M.Measure):
      f0 = math.pow(a, b.value - b.delta)
      f1 = math.pow(a, b.value + b.delta)
      return M.Measure((f0+f1)/2, abs(f0-f1)/2)
    
    return math.pow(a, b)
  
  elif isinstance(a, M.Measure):
    p = b
    if isinstance(b, int) | isinstance(b, float):
      pass
    elif isinstance(b, M.Measure):
      p = b.value
    else:
      raise Exception('pow Measure function does not support "{}" parameter'.format(M.getType(b)))
    
    value = math.pow(a.value, p)
    delta = abs(value*p*a.delta/a.value)
    return M.Measure(value, delta)
  
  else:
    raise Exception('pow Measure function does not support "{}" parameter'.format(M.getType(b)))


def log(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.log(a)
  elif isinstance(a, M.Measure):
    return function(a, math.log)
  else:
    raise Exception('log Measure function does not support "{}" parameter'.format(M.getType(a)))


def log10(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.log10(a)
  elif isinstance(a, M.Measure):
    return function(a, math.log10)
  else:
    raise Exception('log10 Measure function does not support "{}" parameter'.format(M.getType(a)))


def sin(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.sin(a)
  elif isinstance(a, M.Measure):
    v0 = a.value + a.delta
    v1 = a.value - a.delta
    if cos(v0)*cos(v1) < 0:
      s0 = sin(v0)
      s1 = sin(v1)
      if s0 > 0:
        d0 = 1-s0
        d1 = 1-s1
        if d0 > d1:
          return M.Measure((1+s0)/2, d0/2)
        else:
          return M.Measure((1+s1)/2, d1/2)
      else:
        d0 = 1+s0
        d1 = 1+s0
        if d0 > d1:
          return M.Measure((-1+s0)/2, d0/2)
        else:
          return M.Measure((-1+s1)/2, d1/2)
    else:
      return function(a, math.sin)
  else:
    raise Exception('sin Measure function does not support "{}" parameter'.format(M.getType(a)))


def cos(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.cos(a)
  elif isinstance(a, M.Measure):
    v0 = a.value + a.delta
    v1 = a.value - a.delta
    if sin(v0)*sin(v1) < 0:
      c0 = cos(v0)
      c1 = cos(v1)
      if c0 > 0:
        d0 = 1-c0
        d1 = 1-c1
        if d0 > d1:
          return M.Measure((1+c0)/2, d0/2)
        else:
          return M.Measure((1+c1)/2, d1/2)
      else:
        d0 = 1+c0
        d1 = 1+c1
        if d0 > d1:
          return M.Measure((-1+c0)/2, d0/2)
        else:
          return M.Measure((-1+c1)/2, d1/2)
    else:
      return function(a, math.cos)
  else:
    raise Exception('cos Measure function does not support "{}" parameter'.format(M.getType(a)))


def tan(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.tan(a)
  elif isinstance(a, M.Measure):
    return function(a, math.tan)
  else:
    raise Exception('tan Measure function does not support "{}" parameter'.format(M.getType(a)))


def asin(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.asin(a)
  elif isinstance(a, M.Measure):
    return function(a, math.asin)
  else:
    raise Exception('asin Measure function does not support "{}" parameter'.format(M.getType(a)))


def acos(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.acos(a)
  elif isinstance(a, M.Measure):
    return function(a, math.acos)
  else:
    raise Exception('acos Measure function does not support "{}" parameter'.format(M.getType(a)))


def atan(a):
  if isinstance(a, int) | isinstance(a, float):
    return math.atan(a)
  elif isinstance(a, M.Measure):
    return function(a, math.atan)
  else:
    raise Exception('atan Measure function does not support "{}" parameter'.format(M.getType(a)))


def rad2deg(a):
  if isinstance(a, int) | isinstance(a, float):
    return a*180/pi
  elif isinstance(a, M.Measure):
    angle = a.value*180/pi
    delta = a.delta*180/pi
    return M.Measure(angle, delta)
  else:
    raise Exception('rad2deg Measure function does not support "{}" parameter'.format(M.getType(a)))


def deg2rad(a):
  if isinstance(a, int) | isinstance(a, float):
    return a*pi/180
  elif isinstance(a, M.Measure):
    angle = a.value*pi/180
    delta = a.delta*pi/180
    return M.Measure(angle, delta)
  else:
    raise Exception('deg2rad Measure function does not support "{}" parameter'.format(M.getType(a)))

