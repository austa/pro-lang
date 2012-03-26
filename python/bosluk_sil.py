def bosluk_sil(cumle):
	new = ""
	for c in range(len(cumle)):
		if cumle[c] != " ":
			new += cumle[c]
		elif cumle[c-1] != " ":
			new += cumle[c]
	return new		
print bosluk_sil("     .askn    ds sad  ads  a   ")
			
	
