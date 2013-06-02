def fib(n):
    if n == 0:
      return 0
    if n == 1:
        return 1
    else:
    	return fib(n-1) + fib(n-2)

mainlist = []

for n in range(2, 35):
	if fib(n) % 2 == 0:
		mainlist.append(fib(n))

fib_sum = sum(mainlist)
print fib_sum
