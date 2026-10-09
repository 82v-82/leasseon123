import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("500x500")


def insert_value():
    pass

def init():
    frame_top = tk.Frame(root, width=500, height=100, background="grey")
    frame_top.pack(side="top")
    frame_bottom_left = tk.Frame(root, width=350, height=400, background="grey")
    frame_bottom_left.pack(side="left")
    frame_bottom_right = tk.Frame(root, width=150, height=400, background="grey")
    frame_bottom_right.pack(side="right")

    return frame_bottom_left


def gui():
    frame_bottom_left = init()
    frame_bottom_left.pack(side="left", padx=15, pady=15)
    col=0
    row=0

    for button in range(10):
        button = tk.Button( frame_bottom_left, width=10,height=2, text=button,command=insert_value)
        button.grid(row=row, column=col)
        col+=1
        if col==3:
            col =0
            row+=1




gui()
root.mainloop()

