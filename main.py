import json
import os
from datetime import datetime

students = []
here = []
absent = []
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
                hereFolder = 'here_log'
                dateStr = datetime.now().strftime("%Y-%m-%d")
                hereFile = f"here_{dateStr}.json"
                herePath = os.path.join(hereFolder, hereFile)
                if not os.path.exists(hereFolder):
                    os.makedirs(hereFolder)
                    with open(herePath, 'w') as f:
                        json.dump(here, f)
                print("Gelenler:")
                x = 0
                for student in here:
                    x += 1
                    print(f"{x}. {student}")
                for _ in range(20):
                    print("-",end="")
                print()
                absentFolder = 'absent_log'
                dateStr = datetime.now().strftime("%Y-%m-%d")
                absentFile = f"absent_{dateStr}.json"
                absentPath = os.path.join(absentFolder, absentFile)
                if not os.path.exists(absentFolder):
                    os.makedirs(absentFolder)
                with open(absentPath, 'w') as f:
                    json.dump(absent, f)
                    print("Gelmeyenler:")
                x = 0
                for student in absent:
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
        here_folder = 'here_log'
        absent_folder = 'absent_log'
        def list_and_choose_log(folder, type_name):
            if os.path.exists(folder):
                logs = [f for f in os.listdir(folder) if f.endswith(".json")]
                if not logs:
                    print(f"{type_name} logu bulunamadı.")
                    return None
                print(f"\nMevcut {type_name} logları:")
                for i, filename in enumerate(sorted(logs), 1):
                    print(f"{i}. {filename}")
                while True:
                    try:
                        choice = int(input(f"Bir {type_name} logunu seçin (1-{len(logs)}): "))
                        if 1 <= choice <= len(logs):
                            return os.path.join(folder, sorted(logs)[choice - 1])
                        else:
                            print("Geçersiz seçim. Lütfen tekrar deneyin.")
                    except ValueError:
                        print("Geçersiz giriş. Lütfen bir sayı girin.")
            else:
                print(f"{type_name} log klasörü bulunamadı.")
                return None
        here_log_path = list_and_choose_log(here_folder, 'Gelenler')
        if here_log_path:
            with open(here_log_path, 'r') as f:
                log_content = json.load(f)
                print(f"\n{os.path.basename(here_log_path)} İçeriği:")
                for i, student in enumerate(log_content, 1):
                    print(f"  {i}. {student}")
        absent_log_path = list_and_choose_log(absent_folder, 'Gelmeyenler')
        if absent_log_path:
            with open(absent_log_path, 'r') as f:
                log_content = json.load(f)
                print(f"\n{os.path.basename(absent_log_path)} İçeriği:")
                for i, student in enumerate(log_content, 1):
                    print(f"  {i}. {student}")

    elif choice == "5":
        print("Uygulamadan çıkılıyor...")
        with open('students.json', 'w') as f:
            json.dump(students, f)
        break
    else:
        print("Hatalı Giriş!")
