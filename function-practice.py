#max_num(a,b,c)
def max_num(a,b,c):
  if a > b:
    if a > c:
      return a
    else:
      return c;
  else:
    if b > c:
      return b
    else:
      return c

#mult_list(*args)
def mult_list(*args):
  res = 1
  for arg in args:
    res *= arg

  return res

#rev_string(str)
def rev_string(string):
  return string[::-1] #Combine negative index slicing with extended syntax

#fib(n)
def fib(n):
  if n == 0:
    return n;
  else:
    return n+fib(n-1)

#num_within(num, btm, top)
def num_within(num, low, high):
  if num > low:
    if num < high:
      return True
    else:
      return False
  else:
    return False

#pascal(n)
def pascal(n):
  #Going to use powers of 11 form to make pascals triangle (easiest way but only works up to 5 rows)
  for m in range(n):
    print(" "*(m-n), end=" ")
    print(f" ".join(str(11**m)))
    
    

###
# TEST FUNCTIONS
###

print( max_num(6,1,3) )
print( mult_list(4,5,2,3) )
print( rev_string("Hello") )
print( fib(1) )
print( num_within(4,1,10) )
print( num_within(22,4,9) )
pascal(3)
pascal(10)