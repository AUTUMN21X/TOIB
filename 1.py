import tkinter as tk
import hashlib
def hash_password():
    password = entry.get()
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, hashed_password)

root = tk.Tk()
root.title("Хеширование пароля SHA-256")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry('500x150+{}+{}'.format(w, h))
root.resizable(False, False)

input_label = tk.Label(root, text="Введите пароль:")
input_label.pack()

entry = tk.Entry(root, width=80)
entry.pack(pady=10)

button = tk.Button(root, text="Хешировать", command=hash_password)
button.pack(pady=10)

output_entry = tk.Entry(root, width=80)
output_entry.pack(pady=10)

root.mainloop()
