def hop(s, p):
	sayi  = len(p)
	for i in range(len(s)):
		if s[i:i+sayi] == p:
			return True
	return False
print hop("110110101011","10100")
		
