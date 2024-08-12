# Bậc 1: 0 - 50 kWh đầu tiên, giá 1.678 VND/kWh.
# Bậc 2: 51 - 100 kWh tiếp theo, giá 1.734 VND/kWh.
# Bậc 3: 101 - 200 kWh tiếp theo, giá 2.014 VND/kWh.
# Bậc 4: 201 - 300 kWh tiếp theo, giá 2.536 VND/kWh.
# Bậc 5: 301 - 400 kWh tiếp theo, giá 2.834 VND/kWh.
# Bậc 6: Trên 400 kWh, giá 2.927 VND/kWh.

bac1 = 1678
bac2 = 1734
bac3 = 2014
bac4 = 2536
bac5 = 2834
bac6 = 2927

sotientieuthu = float(input("Nhập số tiền tiêu thụ: "))

if sotientieuthu <= 50:
    sotienphaitra = sotientieuthu * bac1
elif sotientieuthu <= 100:
    sotienphaitra = 50 * bac1 + (sotientieuthu-50)*bac2
elif sotientieuthu <= 200:
    sotienphaitra = 50 * bac1 + 50 * bac2 + (sotientieuthu-100)*bac3
elif sotientieuthu <= 300:
    sotienphaitra = 50 * bac1 + 50 * bac2 + 100 * bac3 + (sotientieuthu-100)*bac4
elif sotientieuthu <= 400:
    sotienphaitra = 50 * bac1 + 50 * bac2 + 100 * bac3 + 100 * bac4 + (sotientieuthu-200)*bac5

print("Số tiền phải trả là: %2f"%sotienphaitra)
