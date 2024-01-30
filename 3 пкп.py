import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel

# Функция для проверки логина и пароля
def login():
    if username_entry.get() == "admin" and password_entry.get() == "password":
        login_window.destroy()
        create_main_window()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

# Функция для создания основного окна приложения
def create_main_window():
    global main_window
    main_window = CTk()
    main_window.title("Менеджер контактов")
    
    # Создание элементов интерфейса для основного окна
    # ... (добавьте здесь свой функционал, например, управление контактами)
    
    main_window.mainloop()

# Создание окна входа
login_window = CTk()
login_window.title("Вход в систему")
login_window.geometry("300x150")

# Создание элементов интерфейса для окна входа
username_label = CTkLabel(login_window, text="Логин:")
username_label.pack()
username_entry = CTkEntry(login_window)
username_entry.pack()

password_label = CTkLabel(login_window, text="Пароль:")
password_label.pack()
password_entry = CTkEntry(login_window, show="*")
password_entry.pack()

login_button = CTkButton(login_window, text="Войти", command=login)
login_button.pack()

# Запуск главного цикла для окна входа
login_window.mainloop()