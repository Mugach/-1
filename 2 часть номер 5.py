import tkinter as tk
from tkinter import messagebox

# Функция для добавления контакта
def add_contact():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    
    if name and surname and phone:
        contact_list.insert(tk.END, f"{name} {surname}: {phone}")
        name_entry.delete(0, tk.END)
        surname_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Ошибка", "Заполните все поля")

# Функция для редактирования контакта
def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact = contact_list.get(index)
        name, surname, phone = contact.split(':')[0].strip().split()
        phone = phone.strip()
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        surname_entry.delete(0, tk.END)
        surname_entry.insert(0, surname)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, phone)
        contact_list.delete(index)

# Функция для удаления контакта
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact_list.delete(index)

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
root.mainloop(12)