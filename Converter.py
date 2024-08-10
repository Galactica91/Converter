import tkinter as tk

def fahrenheit():
    num1 = int(number1_entry.get())
    celsius = ((num1 - 32) * 0.5556)
    number2_entry.delete(0, 'end')
    number2_entry.insert(0, celsius)


window = tk.Tk()
window.title('Converter')
window.geometry("300x250")
window.resizable(False, False)
window.configure(background="#66B2FF")

button_convert = tk.Button(window, text="Convert", width=20, height=2, command=fahrenheit)
button_convert.place(x=75, y=100)
button_convert.configure(background="#99CC99")

number1_entry = tk.Entry(window, width=35)
number1_entry.place(x=35, y=55)
number2_entry = tk.Entry(window, width=35)
number2_entry.place(x=35, y=190)

label_1 = tk.Label(window, text="Введите температуру в Фаренгейт: ")
label_1.configure(background="#66B2FF")
label_1.place(x=35, y=25)
label_2 = tk.Label(window, text="Температура по Цельсию: ")
label_2.configure(background="#66B2FF")
label_2.place(x=35, y=160)

window.mainloop()








