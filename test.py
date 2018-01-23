thang = {"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}

a = int(input("Nhap ngay sinh cua ban:"))
b = str(input("Nhap thang sinh cua ban:"))

b = b.upper()

if ( a >= 20 and thang[b] == 1)  or ( a < 19 and thang[b] == 2):
	print("Ban Cung \"Bao Binh\"")
elif (a >= 19 and thang[b] == 2) or ( a < 20 and thang[b] ==3):
	print("Ban Cung \"Song Ngu\"")
#print(thang[b])
