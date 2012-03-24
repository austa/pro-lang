def sesli_harf(cumle):
	sesliler="aeiouAEIOU"
	sesli=0
	for i in cumle:
		if i in sesliler:
			sesli+=1
	print sesli
	
sesli_harf("alaattin askin oynuyor")
		
	
