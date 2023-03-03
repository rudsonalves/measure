from measure.math_utils.math_utils import *

class Measure:
  def __init__(self, value, delta):
    self.value = value
    self.delta = delta


  def __repr__(self):
    return '{} ± {}'.format(self.value, self.delta)

  
  def __eq__(self, other):
    if isinstance(other, Measure):
      return (self.value == other.value) & (self.delta == other.delta)

    return False


  def __add__(self, other):
    if isinstance(other, Measure):
      return Measure(self.value + other.value, self.delta + other.delta)
    if isinstance(other, int) | isinstance(other, float):
      return Measure(self.value + other, self.delta)

    raise Exception('The add operation of a Measure with an {} is not supported'.format(getType(other)))


  __radd__ = __add__


  def __sub__(self, other):
    if isinstance(other, Measure):
      return Measure(self.value - other.value, self.delta + other.delta)
    if isinstance(other, int) | isinstance(other, float):
      return Measure(self.value - other, self.delta)

    raise Exception('The sub operation of a Measure with an {} is not supported'.format(getType(other)))


  def __rsub__(self, other):
    if isinstance(other, int) | isinstance(other, float):
      return Measure(-self.value + other, self.delta)

    raise Exception('The sub operation of a Measure with an {} is not supported'.format(getType(other)))


  def __mul__(self, other):
    if isinstance(other, Measure):
      m = self.value * other.value
      dm = abs(m)*(self.delta/self.value + other.delta/other.value)
      return Measure(m, dm)
    if isinstance(other, int) | isinstance(other, float):
      m = self.value * other
      dm = self.delta * other
      return Measure(m, dm)

    raise Exception('The mul operation of a Measure with an {} is not supported'.format(getType(other)))


  __rmul__ = __mul__


  def __truediv__(self, other):
    if isinstance(other, Measure):
      m = self.value / other.value
      dm = abs(m)*(self.delta/self.value + other.delta/other.value)
      return Measure(m, dm)
    if isinstance(other, int) | isinstance(other, float):
      m = self.value / other
      dm = self.delta / other
      return Measure(m, dm)

    raise Exception('The mul operation of a Measure with an {} is not supported'.format(getType(other)))


  def __rtruediv__(self, other):
    if isinstance(other, int) | isinstance(other, float):
      m = other / self.value
      dm = abs(m)*self.delta / self.value
      return Measure(m, dm)

    raise Exception('The mul operation of a Measure with an {} is not supported'.format(getType(other)))


  def __pow__(self, n):
    result = pow(self, n)
    return result


  def __rpow__(self, n):
    result = pow(n, self)
    return result


  def round(self, n):
    return Measure(round(self.value, 5), round(self.delta, 5))


class MeasureException:
  def __init__(self, msg):
    raise('The add operation of a Measure with an integer type is not supported')

def getType(v):
  if isinstance(v, int):
    return 'int'
  if isinstance(v, float):
    return 'float'
  if isinstance(v, str):
    return 'string'
  if isinstance(v, Measure):
    return 'Measure'
  return 'unknow'
  