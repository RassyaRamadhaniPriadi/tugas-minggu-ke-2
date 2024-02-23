english = int(input("masukan nilai B.inggris:"))
matematika = int(input("masukan nilai matematika : "))
indo = int(input("masukan nilai B.indo :"))
ipa = int(input("masukan nilai ipa : "))
ips = int(input("masukan nilai ips  : "))

planA = (english+matematika+indo)/3
planB = (english+matematika+indo+ipa+ips)/5

if planA >= 75 :
    hasil = "lulus"
elif planB >= 70:
    hasil = "lulus"
elif matematika ^ english >= 90 :
    hasil = "lulus"
else :
    hasil = "tidak lulus"
print ("kamu",hasil,"pada ujian ini")
