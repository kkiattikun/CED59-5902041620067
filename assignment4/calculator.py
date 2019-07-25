print('------Start Calculator-------')
x = int(input('input num1 : '))
y = int(input('input num2 : '))
mark = input('input Punctuation is [ + or - or * or / ] : ')

class Calculator:

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

cal = Calculator(x,y)

print('---------Process-----------')
print(x,mark,y)
if mark=='+' :
  cal.puls()
elif mark=='-' :
  cal.pop()
elif mark=='*' :
  cal.multiply()
elif mark=='/' :
  cal.divide()
else :
  print('Error !!')
print('-----------End-------------')
