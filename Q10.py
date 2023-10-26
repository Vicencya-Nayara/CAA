def existe_soma(s, x):

  # Ordena os elementos em S.

  s.sort()

  # Percorre os elementos em S, mantendo um ponteiro para o último elemento visitado.

  i = 0
  j = len(s) - 1
  while i < j:
    if s[i] + s[j] == x:
      return True
    elif s[i] + s[j] < x:
      i += 1
    else:
      j -= 1

  return False
  
s = [1, 2, 3, 4, 5]
x = 6

print(existe_soma(s, x))
