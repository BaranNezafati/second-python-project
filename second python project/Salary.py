
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "password":
        messagebox.showinfo("خوش آمدید", "صحیح است")
        create_new_window()
        win.withdraw()
    else:
        messagebox.showerror("رمز عبور یا نام کاربری اشتباه است", "تلاش مجدد")


def create_new_window():

    new_window = tk.Toplevel(win)
    new_window.title("اطلاعات کاربری")
    new_window.resizable(False, False)

    box1_label = tk.Label(new_window, text="نام و نام خانوادگی")
    box1_entry = tk.Entry(new_window)

    box2_label = tk.Label(new_window, text="تعداد روز های تعطیلی")
    box2_entry = ttk.Combobox(new_window, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    box3_label = tk.Label(new_window, text="تعداد ساعت اضافه کاری")
    box3_entry = ttk.Combobox(new_window, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    box4_label = tk.Label(new_window, text="تعداد ساعت شب کاری")
    box4_entry = ttk.Combobox(new_window, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    box5_label = tk.Label(new_window, text="تعداد روز های ماه")
    box5_entry = ttk.Combobox(new_window, values=[29,30,31])


    new_window_button = tk.Button(new_window, text="محاسبه", command=lambda: calculate_expression(box2_entry, box3_entry, box4_entry,box5_entry))

    box1_label.pack(padx=20, pady=20)
    box1_entry.pack(padx=10, pady=10)
    box2_label.pack(padx=20, pady=20)
    box2_entry.pack(padx=10, pady=10)
    box3_label.pack(padx=20, pady=20)
    box3_entry.pack(padx=10, pady=10)
    box4_label.pack(padx=20, pady=20)
    box4_entry.pack(padx=10, pady=10)
    box5_label.pack(padx=20, pady=20)
    box5_entry.pack(padx=10, pady=10)
    new_window_button.pack(padx=10, pady=10)

def calculate_expression(box2_entry, box3_entry, box4_entry, box5_entry):
    box2_value = int(box2_entry.get())
    box3_value = int(box3_entry.get())
    box4_value = int(box4_entry.get())
    box5_value = int(box5_entry.get())
    
    result = (1769428/22*8*box5_value+1769428*0.35*box4_value+1769428/220*1.4*box5_value/box3_value-1769428*box2_value)/100000
    
    messagebox.showinfo("نتیجه", f"(ریال)مقدار محاسبه شده: {result}")

win = tk.Tk()
win.title("ورود")
win.resizable(False, False)

username_label = tk.Label(win, text="نام کاربری:")
username_entry = tk.Entry(win)

password_label = tk.Label(win, text="رمز عبور:")
password_entry = tk.Entry(win, show="*")

login_button = tk.Button(win, text="ورود", command=validate_login)

username_label.pack(padx=100, pady=10)
username_entry.pack(padx=20, pady=20)
password_label.pack(padx=20, pady=20)
password_entry.pack(padx=10, pady=10)
login_button.pack(padx=20, pady=20)

win.mainloop()

