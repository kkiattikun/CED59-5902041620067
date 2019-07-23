class Calculator:
  x = 0
  y = 0

  def __init__(self, input_x, input_y):
    self.x = input_x
    self.y = input_y

  def puls(self):
    result = self.x + self.y
    print('result plus : ', result)

  def pop(self):
    result = self.x - self.y
    print('result pop : ', result)

  def multiply(self):
    result = self.x * self.y
    print('result mulriply : ', result)

  def divide(self):
    result = self.x / self.y
    print('result divide : ', result)

cal = Calculator(5,10)

print('x : ', cal.x)
print('y : ', cal.y)
cal.puls()
cal.pop()
cal.multiply()
cal.divide()
