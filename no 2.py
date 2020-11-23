def main():
    distance()




def distance():
    dist = v*t+(0.5*a*(t**2))
    
kecepatanmobil = v = float(input("kecepatan mobil ini adalah:"))
percepatan = a = float(input("percepatan :"))
print("jarak yang sudah ditempuh mobil dalam setiap waktu")
t = 0
while t <= 9:
    t = t+1
    dist = v*t+(0.5*a*(t**2))

    print("t=" + str(t),"s(t):"+ str(dist))

    
