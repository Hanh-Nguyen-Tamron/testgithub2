# Bậc 1: 0 - 50 kWh đầu tiên, giá 1.678 VND/kWh.
# Bậc 2: 51 - 100 kWh tiếp theo, giá 1.734 VND/kWh.
# Bậc 3: 101 - 200 kWh tiếp theo, giá 2.014 VND/kWh.
# Bậc 4: 201 - 300 kWh tiếp theo, giá 2.536 VND/kWh.
# Bậc 5: 301 - 400 kWh tiếp theo, giá 2.834 VND/kWh.
# Bậc 6: Trên 400 kWh, giá 2.927 VND/kWh.

sodientieuthu = float(input('Mời bạn nhập số điện đã tiêu thụ'))

bac1=1.678
bac2 =1.734
bac3=2.014
bac4=2.536
bac5=2.834
bac6=2.927

if(sodientieuthu<=50):
    sotienphaitra=sodientieuthu *bac1
elif(sodientieuthu<=100):
    sotienphaitra= 50*bac1 +(sodientieuthu-50)*bac2
elif(sodientieuthu<=200):
    sotienphaitra = 50*bac1 +50*bac2 + (sodientieuthu-100)*bac3
elif(sodientieuthu<=300):
    sotienphaitra= 50*bac1 + 50 *bac2 + 100*bac3 +(sodientieuthu-200)*bac4
elif(sodientieuthu<=400):
    sotienphaitra=50*bac1 +50*bac2+100*bac3 +100*bac4 +(sodientieuthu-300)*bac5
elif(sodientieuthu>400):
    sotienphaitra=50*bac1 +50*bac2+100*bac3 +100*bac4 +100*bac5 + (sodientieuthu-400)*bac6
else:
    print('Số điện không hợp lệ')
print("Số tiền phải trả là : %2.f"%sotienphaitra)