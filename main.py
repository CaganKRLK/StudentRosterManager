students = ["Ahmet","Ayşe","Mehmet","Zeynep"]
here = []
absent = []
x = None
print("Sınıf Listesi!")
print("Hoşgeldiniz, lütfen eyleminizi seçin\n1. Yoklama al\n2. Listeyi görüntüle\n3. Öğrenci ekle/çıkar\n4. Çıkış")
while True:
    choice = input("(1/2/3/4): ")
    if choice == "1":
        here.clear()
        absent.clear()
        print("Yoklama alınıyor!\n0: Öğrenci gelmedi\n1: Öğrenci geldi\niptal: yoklamayı iptal eder")
        for student in students:
            if x != "iptal":
                while True:
                    x = input(f"{student} geldi mi?\n")
                    if x == "0":
                        absent.append(student)
                        print("Öğrenci gelmeyenlere eklendi.")
                        break
                    elif x == "1":
                        here.append(student)
                        print("Öğrenci gelenlere eklendi.")
                        break
                    elif x == "iptal":
                        here.clear()
                        absent.clear()
                        print("Yoklama iptal edildi.")
                        break
                    else:
                        print("Hatalı giriş yaptınız!")
        print("Gelenler:")
        x = 0
        for student in here:
            x += 1
            print(f"{x}. {student}")
        print("Gelmeyenler:")
        x = 0
        for student in absent:
            x += 1
            print(f"{x}. {student}")
    elif choice == "2":
        x = 0
        print("Öğrenciler:")
        for student in students:
            x += 1
            print(f"{x}. {student}")
    elif choice == "3":
        print("Listeyi Düzenle")
        while True:
            print("1. Öğrenci ekle\n2. Öğrenci çıkar\n3. Geri dön")
            x = input("(1/2/3): ")
            if x == "1":
                add = input("Eklemek istediğiniz öğrenciyinin adı:\n").title()
                students.append(add)
                students.sort()
                print(f"{add} listedeki yerini aldı.")
            elif x == "2":
                delete = input("Silmek istediğiniz öğrencinin adı veya sırası:\n").title()
                if delete in students:
                    print(f"{delete} listeden kalıcı olaral silinecek!\nBu işlem geri alınamaz!")
                    while True:
                        sure = input("Eminmisin?\n(y/n): ")
                        if sure == "y":
                            students.sort()
                            students.remove(delete)
                            print("Silme işlemi başarılı.")
                            break
                        elif sure == "n":
                            print("Silme işlemi iptal edildi.")
                            break
                        else:
                            print("Hatalı Giriş!")
                elif delete.isdigit():
                    index = int(delete)-1
                    if 0 <= index <= len(students):
                        print(f"{students[index]} listeden silinecek.\nBu işlem geri alınamaz.")
                        while True:
                            sure = input("Eminmisin?\n(y/n): ")
                            if sure == "y":
                                students.sort()
                                students.pop(index)
                                print("Silme işlemi başarılı.")
                                break
                            elif sure == "n":
                                print("Silme işlemi iptal edildi.")
                                break
                            else:
                                print("Hatalı Giriş!")
                else:
                    print("Öğrenci bulunamadı")
            elif x == "3":
                print("Geri dönülüyor...")
                break
            else:
                print("Hatalı Giriş!")
    elif choice == "4":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Hatalı Giriş!")
