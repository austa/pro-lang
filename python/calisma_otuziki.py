def fib(n):
	a,b=0,1
	i=0
	while n-1 > i:
		a,b=b,a+b
		i+=1
	print b
fib(6)
