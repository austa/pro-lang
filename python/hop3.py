def hop(s, p):
	sayi  = len(p)
	for i in range(len(s)):
		if s[i:i+sayi] == p:
			return i
print hop("1011010101","01")
