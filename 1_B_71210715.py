nama = input("Nama : ")
nm = nama.split()
nm1 = nm[0]
nm2 = nm[1]

ttgl =input("Tempat tanggal lahir : ")
ttl = ttgl.split(" ",1)
tempat = ttl[0]
tgl = ttl[1]

if len(nm)<3:
    print("Haloo!", nm1,nm2)
else:
    nm3 = nm[2]
    print("Haloo!", nm1,nm2,nm3)

print("Anda lahir di", tempat, "pada tanggal", tgl)
    
