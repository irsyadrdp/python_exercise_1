#latihan IF, ELIF

print"Masukkan dua buah angka..\n"

angka1= raw_input("Angka ke-1: ")
angka1=int(angka1)

angka2= raw_input("Angka ke-2: ")
angka2=int(angka2)	
	

if angka1==angka2 :
	print"%d sama dengan %d\n" %(angka1,angka2)	#inget identasi, ada tab

elif angka1!=angka2 :
	print"%d tidak sama dengan %d\n" %(angka1,angka2)

elif angka1<angka2 :
	print"%d kurang dari %d\n" %(angka1,angka2)

elif angka1>angka2 :
	print"%d lebih dari %d\n" %(angka1,angka2)

elif angka1<=angka2 :
	print"%d kurang dari sama dengan %d\n" %(angka1,angka2)

elif angka1>=angka2 :
	print"%d lebih dari %d\n" %(angka1,angka2)
