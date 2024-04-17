with open("2.txt", "w", encoding="utf-8") as f:
    f.write("Строка номер 1 файла номер 2\n")

with open("2.txt", "a", encoding="utf-8") as f:
    f.write("Строка номер 1 файла номер 1\n")
    f.write("Строка номер 2 файла номер 1\n")

with open("2.txt", encoding="utf-8") as f:
    print(f.read())

