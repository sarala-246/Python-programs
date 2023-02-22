def divis(n):
    for i in range(n):
      if i % 3 == 0 and i % 4 == 0:
        return "yes"
      else:
        return "No"
