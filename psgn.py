from random import choice

print("Password Generator By Alex Zab")

bg_ltrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sml_ltrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nmbrs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
smbls = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', '|', ']', '}', '[', '{' ]

while True:
    try:
        rng = int(input("На скільки символів?: "))
    except Exception:
        print("Потрібно написати цифру!!! (2, 59, 18)")

    incld_bg_ltrs = input("Пароль має містити великі літери? (т - так / н - ні): ")

    incld_sml_ltrs = input("Пароль має містити малі літери? (т - так / н - ні): ")

    incld_nmbrs = input("Пароль має містити цифри? (т - так / н - ні): ")

    incld_smbls = input("Пароль має містити символи? (т - так / н - ні): ")


    full_pass = []
    if incld_bg_ltrs == 'т' or incld_bg_ltrs == 'так':
        full_pass = full_pass + bg_ltrs

    if incld_sml_ltrs == 'т' or incld_sml_ltrs == 'так':
        full_pass = full_pass + sml_ltrs

    if incld_nmbrs == 'т' or incld_nmbrs == 'так':
        full_pass = full_pass + nmbrs

    if incld_smbls == 'т' or incld_smbls == 'так':
        full_pass = full_pass + smbls

    try:
        r = 0
        rw = []
        delete = ['[', "'", ',', ']']
        while r != rng:
            chois = choice(full_pass)
            r += 1
            rw.append(chois)
        for d in delete:
            rw = str(rw).replace(d, '')
            rw = rw.replace(" ", "")
        print("It's --  " + str(rw))
    except Exception:
        pass