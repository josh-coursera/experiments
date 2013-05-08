def a(func):
  def wrapped():
    return 'a' + func()
  return wrapped

def b(func):
  def wrapped():
    return 'b' + func()
  return wrapped

@a
@b
def c():
  return 'c'

print c()
