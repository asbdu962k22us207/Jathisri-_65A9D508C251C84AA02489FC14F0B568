def recursion_fact(X):
  if X==1:return 1
  else: return (X*recursion_fact (X-1))
num=int (input("enter a number:"))
if num>=1:
  print ("The factorial of",num,"is",recursion_fact(num))