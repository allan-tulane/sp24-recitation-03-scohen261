"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    
    ###
  xvec, yvec = pad(x.binary_vec, y.binary_vec)

  if binary2int(xvec).decimal_val <= 1 and binary2int(yvec).decimal_val   <= 1:
    return BinaryNumber(binary2int(xvec).decimal_val * binary2int(yvec).decimal_val)

  x_left, x_right = split_number(xvec)
  y_left, y_right = split_number(yvec)

  one = bit_shift(_quadratic_multiply(x_left, y_left), len(xvec))
  two = bit_shift(_quadratic_multiply(x_left, y_right), len(xvec) // 2)
  three = bit_shift(_quadratic_multiply(x_right, y_left), len(xvec) // 2)
  four = _quadratic_multiply(x_right, y_right)

  result = BinaryNumber(one.decimal_val + two.decimal_val +       three.decimal_val + four.decimal_val)

  return result
    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    f(BinaryNumber(x), BinaryNumber(y)
    return (time.time() - start)*1000



    
    

