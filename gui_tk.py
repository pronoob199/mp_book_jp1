from tkinter import *


root = Tk()
root.geometry('800x700')
root.title('Map Book')


ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektu=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_uzytkownikow, text='Lista znajomych:')
listbox_lista_obiektow=Listbox(ramka_lista_uzytkownikow, width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text='Pokaz szczegoly')
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text='Usuń')
button_edytjuj_uzytkownika=Button(ramka_lista_uzytkownikow, text='Edytjyj')


label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_uzytkownika.grid(row=2, column=1)
button_edytjuj_uzytkownika.grid(row=2, column=2)

#ramka_formularz

label_formularz=Label(ramka_formularz, text='Formularz edycji dodawaia')
label_formularz.grid(row=0, column=0, columnspan=3)






root.mainloop()