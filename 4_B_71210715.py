print("=====GEBYAR DISKON=====")
print("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")

#data
kipas = int(input("KIPAS ANGIN DISKON 10% Rp 25.000,00 : "))
sepeda = int(input("SEPEDA DISKON 55% Rp 6.000,00 : "))
helm = int(input("HELM ROSSI DISKON 77% Rp 8.000,00 : "))

print("=====TOTAL=====")

#potongan
potK = (10/100*25000)*kipas
potS = (55/100*6000)*sepeda
potH = (77/100*8000)*helm
total = potK+potS+potH

#cetak
print("TOTAL KIPAS ANGIN : Rp ", potK)
print("TOTAL SEPEDA      : Rp ", potS.float(None,5))
print("TOTAL HELM ROSSI  : Rp ", potH)

print("Jumlah total diskon yang didapat adalah", total)

