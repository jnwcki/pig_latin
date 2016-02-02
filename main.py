#pig latinizer

first_name = input("What is your first name? >")

if first_name[0].lower() in ["a","e","i","o","u"]:
    print("Your pig latin first name is: {}".format(first_name[1].upper() + first_name[2:]) + 'say!')
else:
    print("your pig latin first name is: {}".format(first_name[1].upper() + first_name[2:] + first_name[0]) + 'ay!')