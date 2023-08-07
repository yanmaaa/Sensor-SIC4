from mfrc522 import SimpleMFRC522
import os

reader = SimpleMFRC522()
inventory = {}
processed_tags = set()

# Membaca inventaris dari file log jika ada
if os.path.exists("inventory.log"):
    with open("inventory.log", "r") as log_file:
        for line in log_file:
            if line.startswith("Tag ID: "):
                tag_id, action, item = line.strip().split(", ")[0].split(": ")[1], line.strip().split(", ")[1].split(": ")[1], line.strip().split(", ")[2].split(": ")[1]
                processed_tags.add(tag_id)
                if action == "in":
                    if item in inventory:
                        inventory[item] += 1
                    else:
                        inventory[item] = 1
                elif action == "out":
                    if item in inventory and inventory[item] > 0:
                        inventory[item] -= 1
                        if inventory[item] == 0:
                            del inventory[item]

try:
    while True:
        print("Tempelkan tag pada pembaca...")
        id, _ = reader.read()
        print(f"Tag ID: {id}")

        if id in processed_tags:
            print("Tag ini sudah ditambahkan ke inventaris sebelumnya.")
            action = input("Masukkan tindakan (out/q untuk keluar): ")
        else:
            action = input("Masukkan tindakan (in/out/q untuk keluar): ")

        if action.lower() == "q":
            break

        if action.lower() == "in":
            item = input("Masukkan nama barang: ")
            if item in inventory:
                inventory[item] += 1
                print(f"{item} sudah tersimpan di inventaris.")
            else:
                inventory[item] = 1
                print(f"{item} berhasil ditambahkan ke inventaris.")
        elif action.lower() == "out":
            item = input("Masukkan nama barang: ")
            if item in inventory and inventory[item] > 0:
                inventory[item] -= 1
                print(f"{item} dikeluarkan dari inventaris.")
                if inventory[item] == 0:
                    del inventory[item]
            else:
                print(f"{item} tidak tersedia dalam inventaris atau stok habis.")
        else:
            print("Tindakan tidak valid. Silakan coba lagi.")

        if action.lower() in ["in", "out"]:
            # Menyimpan data ke dalam file .log jika tindakan valid (in atau out)
            with open("inventory.log", "a") as log_file:
                log_file.write(f"Tag ID: {id}, Tindakan: {action}, Nama Barang: {item}\n")
                processed_tags.add(id)  # Tandai tag ini sudah ditambahkan

        print("Inventaris saat ini:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
        print()

except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    reader.cleanup()
