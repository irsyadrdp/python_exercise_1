#nested for cari bilangan prima

for i in range(1,20):
	count_zero_remainder = 0
	for j in range(1,i+1):
		num_remainder = i%j
		#print num_remainder,
		if num_remainder == 0:
			count_zero_remainder = count_zero_remainder + 1

	if count_zero_remainder == 2:
		print i, "adalah bilangan prima"
	else:
		#print 1, "bukanlah bilangan prima"
		print""
