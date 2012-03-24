def dizi(sayi,aranilan):
	new=""
	for i in sayi:
		new+=i
		if new==aranilan:
			 return True
	if new != aranilan:
		return False
print dizi("11011110","111")
