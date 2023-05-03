# Bisection method
def nth_root(n, a, eps):

  # The root lies between 1 and a
  low  = min(1, a)
  high = max(1, a)

 #till error less than given toleance
  while(abs(high - low) > eps):
    mid = (high+low)/2

    if (((low**n)-a)* ((mid**n)-a) < 0):   # Checking for change of sign
      high = mid

    else:
      low = mid

  print((high+low)/2)


nth_root(9, 81, 0.00002)

