import tkinter as tk
def click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)


root = tk.Tk()
root.title("Калькулятор")
root.geometry("700x700")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, font=("Times New Roman", 14), width=5, height=2,
        command=lambda b=button: click(b)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()