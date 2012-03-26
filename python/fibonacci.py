def fib(n):
	a,b=0,1
	i=0
	while n > i:
		print b,
		a,b=b,a+b
		i+=1
		
fib(6)
