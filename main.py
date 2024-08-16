import json
import os
from datetime import datetime

students = []
heres = []
absents = []
hereFolder = 'here_log'
absentFolder = 'absent_log'

# class student():
#     def __init__():
#         studen.fname = name + sname
#     def areTheyHere():
#         if student.fname in heres:
#             return True
#         else:
#             return False

def saveRollCall(saveFolder,saveList,saveName):
    dateStr = datetime.now().strftime("%Y-%m-%d")
    saveFile = f"{saveName}_{dateStr}.json"
    savePath = os.path.join(saveFolder, saveFile)
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)
    with open(savePath, 'w') as f:
        json.dump(saveList, f)
def list_and_choose_log(folder, type_name):
    if os.path.exists(folder):
        logs = [f for f in os.listdir(folder) if f.endswith(".json")]

        if not logs:
            print(f"{type_name} logu bulunamadı.")
        print(f"\nMevcut {type_name} logları:")

        for i, filename in enumerate(sorted(logs), 1):
            print(f"{i}. {filename}")

        while True:
            try:
                choice = int(input(f"Bir {type_name} logunu seçin (1-{len(logs)}): "))

                if 1 <= choice <= len(logs):
                    logPath = os.path.join(folder, sorted(logs)[choice - 1])
                    break
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyin.")
                    break
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
                break
        else:
            print(f"{type_name} log klasörü bulunamadı.")

    if logPath:
        with open(logPath, 'r') as f:
            logContent = json.load(f)
            print(f"\n{os.path.basename(logPath)} İçeriği:")

            for i, student in enumerate(logContent, 1):
                print(f"  {i}. {student}")



try:
    with open('students.json', 'r') as f:
        content = f.read().strip()
        if content:
            students = json.loads(content)
        else:
            students = []
except FileNotFoundError:
    students = []
x = None

print("Sınıf Listesi!")
print("Hoşgeldiniz, lütfen eyleminizi seçin")

while True:
    print("1. Yoklama al\n2. Listeyi görüntüle\n3. Öğrenci ekle/çıkar\n4. Logları Görüntüle\n5. Çıkış")
    choice = input("(1/2/3/4/5): ")
    if choice == "1":
        heres.clear()
        absents.clear()
        print("Yoklama alınıyor!\n0: Öğrenci gelmedi\n1: Öğrenci geldi\niptal: yoklamayı iptal eder")
        complate = True
        x = None
        for student in students:
            if x == "iptal":
                complate = False
                break
            else:
                while True:
                    x = input(f"{student} geldi mi?\n")
                    if x == "0":
                        absents.append(student)
                        print("Öğrenci gelmeyenlere eklendi.")
                        break
                    elif x == "1":
                        heres.append(student)
                        print("Öğrenci gelenlere eklendi.")
                        break
                    elif x == "iptal":
                        heres.clear()
                        absents.clear()
                        print("Yoklama iptal edildi.")
                        break
                    else:
                        print("Hatalı giriş yaptınız!")
        if complate:
            saveRollCall(hereFolder,heres,"here")
            saveRollCall(absentFolder,absents,"absent")
            print("Gelenler:")
            x = 0
            for student in heres:
                x += 1
                print(f"{x}. {student}")
            for _ in range(20):
                print("-",end="")
            print()
            print("Gelmeyenler:")
            x = 0
            for student in absents:
                x += 1
                print(f"{x}. {student}")
            for _ in range(20):
                print("-",end="")
            print()
    elif choice == "2":
        x = 0
        print("Öğrenciler:")
        for student in students:
            x += 1
            print(f"{x}. {student}")
        for _ in range(20):
            print("-",end="")
        print()
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
        print("Logları Görüntüle")
        list_and_choose_log(hereFolder, 'Gelenler')
        list_and_choose_log(absentFolder, 'Gelmeyenler')
                     
    elif choice == "5":
        print("Uygulamadan çıkılıyor...")
        with open('students.json', 'w') as f:
            json.dump(students, f)
        break
    else:
        print("Hatalı Giriş!")
