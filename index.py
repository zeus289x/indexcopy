import os
import webbrowser
import requests
import sys

downloads_folder = '/storage/emulated/0/Download' 

os.system("clear")

print("\033[1;35m")
print("  _____       __      ___     __  __  __  ")
print("  \\_   \\   /\\ \\ \\    /   \\   /__\\ \\ \\/ /  ")
print("   / /\\/  /  \\/ /   / /\\ /  /_\\    \\  /   ")
print(" /\\/ /_   / /\\  /   / /_//  //__    /  \\   ")
print(" \\____/   \\_\\ \\/   /___,'   \\__/   /_/\\_\\  ")
print("\033[0m")
print("\033[1;36mBu tool Zeus289 tarafından hazırlanmıştır.\033[0m")
print("\033[1;34mDiscord: https://discord.gg/289\033[0m")
print("")

url = input("Hedef URL örnek: https://example.com: ")

if not url:
    print("Bir URL girmelisin!")
    exit()

print("Sitenin indexi indiriliyor...")

try:
    response = requests.get(url)
    response.raise_for_status()
    file_path = os.path.join(downloads_folder, "index.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"\033[1;32mIndex başarıyla indirildi! '{file_path}' dosyasına kaydedildi.\033[0m")
    print("\033[1;33mDiscord linkine yönlendiriliyorsunuz...\033[0m")
    webbrowser.open("https://discord.gg/289")
except Exception as e:
    print(f"\033[1;31mBir hata oluştu: {e}\033[0m")
