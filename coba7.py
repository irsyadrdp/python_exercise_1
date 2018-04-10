#nested condition

username = raw_input("Masukkan username: ")
password = raw_input("Masukkan passowrd: ")

username_db = "user"
password_db = "admin"

if username == username_db:
	if password == password_db:
		print"WELCOME !"
	else:
		print"Password salah"
else:
	print"User tidak terdaftar"
