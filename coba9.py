#nested for pakai range

#contoh looping biasa
for i in range(1,10):
	print"ini pengulangan ke-",i

#membuat segitiga siku-siku
for i in range(0,10):
	for j in range(0,i+1):
		if j == 1:
			print "X"
		else:
			print "*",
	print""
