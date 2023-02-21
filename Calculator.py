import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg='black')
font_style = ("Comic Sans", 20)
def button_clicked(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))
display = tk.Entry(root, width=20, borderwidth=5, font=font_style, justify="right", bg="black", fg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
result = tk.Label(root, text="", width=20, borderwidth=5, relief="sunken", font=font_style, bg="black", fg="white")
result.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    "C", "%","*","",
    "7", "8", "9", "+",
    "4", "5", "6","-",
    "1", "2", "3", 
    ".","", "0", "=", 
]

row = 6
col = 0
for button_label in button_list:
    if button_label == "C":
        button = tk.Button(root, text=button_label, padx=20, pady=10, font=font_style, bg="black", fg="white", command=lambda: clear_display())
    elif button_label == "=":
        button = tk.Button(root, text=button_label, padx=20, pady=10, font=font_style, bg="orange", fg="white", command=lambda: evaluate_expression())
    else:
        button = tk.Button(root, text=button_label, padx=20, pady=10, font=font_style, bg="black", fg="white", bd=2, command=lambda number=button_label: button_clicked(number))

    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        row += 1
        col = 0

def clear_display():
    display.delete(0, tk.END)
    result.config(text="")

def evaluate_expression():
    expression = display.get()
    try:
        result_val = eval(expression)
        result.config(text=result_val)
    except:
        result.config(text="Error")

root.mainloop()
