from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(7)) == 5*7
    assert quadratic_multiply(BinaryNumber(11), BinaryNumber(13)) == 11*13
