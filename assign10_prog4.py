def unique_list(n):
  x = []
  for a in n:
    if a not in x:
      x.append(a)
  return x
 
print(unique_list([3,14,2,3,12,2,14,12,7,6,14]))