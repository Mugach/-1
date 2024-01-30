import tkinter as tk
from tkinter import messagebox

# Глобальный список для хранения контактов
contacts = []

# Функция для добавления контакта
def add_contact():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    
    if name and surname and phone:
        contacts.append((name, surname, phone))
        update_listbox()
    else:
        messagebox.showerror("Ошибка", "Заполните все поля")

# Функция для обновления списка контактов
def update_listbox():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} {contact[1]}: {contact[2]}")

# Функция для редактирования контакта
def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        name, surname, phone = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        surname_entry.delete(0, tk.END)
        surname_entry.insert(0, surname)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        del contacts[index]
        update_listbox()

# Функция для удаления контакта
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        del contacts[selected[0]]
        update_listbox()

# Создание главного окна
root = tk.Tk()
root.title("Менеджер контактов")

# Создание элементов интерфейса
name_label = tk.Label(root, text="Имя:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

surname_label = tk.Label(root, text="Фамилия:")
surname_label.grid(row=1, column=0)
surname_entry = tk.Entry(root)
surname_entry.grid(row=1, column=1)

phone_label = tk.Label(root, text="Номер телефона:")
phone_label.grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Добавить контакт", command=add_contact)
add_button.grid(row=3, column=0)

edit_button = tk.Button(root, text="Редактировать контакт", command=edit_contact)
edit_button.grid(row=3, column=1)

delete_button = tk.Button(root, text="Удалить контакт", command=delete_contact)
delete_button.grid(row=3, column=2)

contact_list = tk.Listbox(root)
contact_list.grid(row=4, column=0, columnspan=3, sticky="ew")

# Запуск главного цикла
root.mainloop(112)