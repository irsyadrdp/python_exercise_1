#struktur data di python, pakae list, tuple, dictionary
#list []		--> bisa diedit isinya
#tuple()		--> ga bisa diedit isinya
#dictionary{}	--> dinamis.....	

#cara definiisi list
sebuah_list = ['Zorin OS','Ubuntu','FreeBSD','NetBSD','OpenBSD','Backtrack','Fedora','Slackware']

#cara definisi tuple
sebuah_tuple = (0,1,2,3,4,5,6,7,8,9)

#cara definisi dictionary
sebuah_dictionary= {'Nama':'Wiro Sableng','Prodi':'Ilmu Komputer','Email':'Wirosableng@localhost','Website':'http://www.sitampanggarang.com'}

#################################################
print"Akses salah satu elemen: "
print sebuah_list[5]
print sebuah_tuple[8]
print sebuah_dictionary['Website']
print"\n"

print"Akses beberapa elemen: "
print sebuah_list[2:5]
print sebuah_tuple[3:6]

##################################################

#akses elemen
print"Mengakses semua elemen dengan looping for: "
print"-------------------------\n\n\n\n"

for sebuah in sebuah_list:
	print sebuah
print"\n"

for sebuah in sebuah_tuple:
	print sebuah
print"\n"

for sebuah in sebuah_dictionary:
	print sebuah, ':' , sebuah_dictionary[sebuah]


##################################################
print"\n\n\n\n-------------------------\n\n\n\n"

#cara manambah elemen baru
print"Cara manambah elemen baru: "
print"\n"

print sebuah_list
list_baru = sebuah_list + ['PC Linux OS','Blankon','IGOS','OpenSUSE']
print list_baru
print"\n"

print sebuah_tuple
tuple_baru = sebuah_tuple + (100,200,300)
print tuple_baru
print"\n"

print sebuah_dictionary
dictionary_baru = {'Telp':'022-12345678','Alamat':'Bandung, Jabar'}
sebuah_dictionary.update(dictionary_baru)
print sebuah_dictionary
print"\n\n"

"""
- array ibsa dikali jadi isinya bisa diduplikat array = [a,b,b,b] * 3
- terus kalo mau hapus tinggal del array[2]
	

"""



















