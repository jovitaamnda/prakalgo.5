# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:18:10 2022

@author: jovita amanda putri
"""

umur = "0"
total = 0
while (umur != ""):
    umur = input("masukkan umur: ")
    if umur != '':
        umur_angka = int(umur)
        if umur_angka <= 2:
            print("Gratis")
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12:
            print("Harga $14.00")
            price = 14
        elif umur_angka >= 65:
            print("Harga $18.00")
            price = 18
        else:
            print("Harga $23.00")
            price = 23  
        total = total + price
        print("Running total: %0.2f" % total)
        
jumlah = int(input("masukkan jumlah uang: "))
hasil = jumlah - total
print("Running kembalian: %0.2f" % hasil)
