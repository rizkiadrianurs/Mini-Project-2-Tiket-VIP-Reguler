Tiket_vip = [1,2,3,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20]

Tiket_reguler = [21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
51,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,
81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]


Manager = {
    "Username": "Zian",
    "Password": "4321"
}

users = {
    "username": "rizki",
    "password": "1234"
}

Data_pusat =[4,56,80]

def menu_karyawan() :
    while True : 
        print("---------------------------------------------------")
        print("                       MENU                        ")
        print("---------------------------------------------------")
        print("1. Mengecek Tiket VIP Atau Reguler")
        print("2. Pengecekan Kursi VIP dan Reguler")
        print("3. Home ")
        print("--------------------------------------------------")

        try :
            Menu = int(input ("Pilih Menu Apa: "))
        except ValueError:
            print("Tolong masukkan angka")
        except KeyboardInterrupt:
            print("\nJangan tekan CTRL+C")
        except EOFError:
            print("Jangan tekan CTRL+Z")

        if Menu == 1:
            try :
                Pengecekan_tiket1 = int( input("Sebutkan No Tiket Untuk Mengecek Jenis Tiket: ") )
                if Pengecekan_tiket1 in Tiket_vip :
                    Tiket_vip.remove(Pengecekan_tiket1)
                    Data_pusat.append(Pengecekan_tiket1)
                    print ("Tiket Ini Adalah Vip")
                    print ("Tiket vip : \n", Tiket_vip) 
                    print ("Tiket Reguler \n", Tiket_reguler)
                    print ("Data Pusat \n", Data_pusat)                
                else :
                    Tiket_reguler.remove(Pengecekan_tiket1)
                    Data_pusat.append(Pengecekan_tiket1)
                    print ("Tiket vip : \n", Tiket_vip) 
                    print ("Tiket Reguler \n", Tiket_reguler)
                    print ("Data Pusat \n", Data_pusat) 
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

        elif Menu == 2:
            try :
                Pengecekan_tiket2 = int(input("Sebutkan No Tiket Untuk Mengecek Kursi: "))
                if Pengecekan_tiket2 in Tiket_vip:
                    if Pengecekan_tiket2 <= 10:
                        print(f"Kursi Anda adalah A{Pengecekan_tiket2}")
                    else:
                        print(f"Kursi Anda adalah B{Pengecekan_tiket2 - 10}")
                else:
                    print("Penonton Tidak Memiliki Kursi Khusus dan Bisa Menonton Dengan Berdiri")
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

        elif Menu == 3 :
            print ("Anda Telah Keluar")
            break

def menu_manager() :
    while True :
        print("--------------------------------------------")
        print("                   MENU                     ")
        print("--------------------------------------------")
        print("1. Lihat Data Pusat")
        print("2. Mengecek sisa tiket VIP dan Reguler ")
        print("3. Menghapus tiket dari data pusat")
        print("4. Update Tiket Di Data Pusat")
        print("5. Masukkan Tiket Ke Data Pusat")
        print("6. Home ")
        print("--------------------------------------------")

        menu2 = int (input ("Pilih Menu Apa :"))

        if menu2 == 1 :
            print (f"Ini Adalah Informasi Terbaru \n{Data_pusat}")

        elif menu2 == 2 :
            print(f"Sisa Tiket VIP = \n{Tiket_vip}")
            print(f"Sisa Tiket Reguler = \n{Tiket_reguler}")

        elif menu2 == 3 :
            try :
                Pengecekan_tiket4 =int(input("Sebutkan No Tiket Untuk Di Hapus: "))
                if Pengecekan_tiket4 in Data_pusat:
                    Data_pusat.remove(Pengecekan_tiket4)
                    print (f"{Pengecekan_tiket4} Sudah Terhapus")
                    print (Data_pusat)
                else:
                    print("Tiket Tersebut Belum Masuk Data Pusat")
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

        elif menu2 == 4 :
            try :
                tiket_lama = int(input("Masukkan Nomor Tiket Lama : "))
                if tiket_lama in Data_pusat:
                    tiket_baru = input("Masukkan Nomor Tiket Baru: ")
                    index = Data_pusat.index(tiket_lama)
                    Data_pusat[index] = tiket_baru
                    print(f"Tiket {tiket_lama} berhasil diupdate menjadi {tiket_baru}")
                else:
                    print("Tiket lama tidak ditemukan di Data Pusat")
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

        elif menu2 == 5 :
            try :
                Pengecekan_tiket3 = int(input("Sebutkan No Tiket Untuk Dimasukkan Ke Data Pusat: "))
                Data_pusat.append(Pengecekan_tiket3)
                print(f"{Pengecekan_tiket3} Sudah Di Masukkan")
                print(Data_pusat)
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

        elif menu2 == 6 :
            try :
                ("Anda Sudah Keluar")
                break
            except ValueError:
                print("Tolong masukkan angka")
            except KeyboardInterrupt:
                print("\nJangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan CTRL+Z")

while True:
    try:
        print("---------------")
        print("     MENU :    ")
        print("---------------")
        print("| 1. Manager  |")
        print("---------------")
        print("| 2. Karyawan |")
        print("---------------")
        print("| 3. Logout   |")
        print("---------------")
        pilihan = int(input("Mau pilih Menu Apa : "))

        if pilihan == 1:
            print("-------------------------------------------------")
            print("       SELAMAT DATANG MANAGER PERUSAHAAN         ")
            print("-------------------------------------------------")

            username1 = input("Username : ")
            password1 = input("Password : ")

            if username1 == Manager["Username"] and password1 == Manager["Password"]:
                print("Anda Berhasil Login sebagai Manager")
                menu_manager()
            else:
                print("Username atau Password salah!")

        elif pilihan == 2:
            print("-------------------------------------------------")
            print("         SELAMAT DATANG DI PERUSAHAAN            ")
            print("-------------------------------------------------")

            username2 = input("Username : ")
            password2 = input("Password : ")

            if username2 == users["username"] and password2 == users["password"]:
                print("Anda Berhasil Login sebagai Karyawan")
                menu_karyawan()
            else:
                print("Username atau Password salah!")

        elif pilihan == 3 :
            ("Terimaksih, Silahkan Datang Kembali")
            break

        else:
            print("Pilihan tidak valid")

    except ValueError:
        print("Tolong masukkan angka")
    except KeyboardInterrupt:
        print("\nJangan tekan CTRL+C")
    except EOFError:
        print("Jangan tekan CTRL+Z")


