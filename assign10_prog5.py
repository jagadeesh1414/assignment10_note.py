def test_range(n):
    if n in range(20,30):
        print( "Number %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(25)