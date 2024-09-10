print("chao mung den cong vien tro choi!")
height = int(input("chieu cao cua ban la bao nhieu? "))
bill = 0
if height > 120:
    print("ban co the choi tro choi")
    age = int(input("tuoi cua ban la bao nhieu? "))
    if age > 18:
        print("ban phai tra 12$ de choi tro choi")
        bill = 12
    elif age <= 18:
        print("ban phai tra 7$ de choi tro choi")
        bill = 7
    else:
        print("ban phai tra 5$ de choi tro choi")
        bill = 5
    wants_photo = input("ban co muon chup hinh khong? (Y or N)")
    if wants_photo == "Y":
        bill += 3;
    print("Tong hoa don cuoi cung cua ban la {bill}")
    
else:
    print("ban khong co the choi tro choi")