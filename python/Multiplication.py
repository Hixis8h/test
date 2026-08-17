import tkinter as tk

def show_output():
    number= int(number_input.get())

    if number == 0 :
        output_lable.configure(text='ผิดที่ไว้ใจ')
        return

    output = ''
    for i in range(1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

        output_lable.configure(text=output)

window = tk.Tk()
window.title('Justpython')
window.minsize(width=400,height=400)

title_lable = tk.Label(master=window,text='สุตรคูณแม่')
title_lable.pack(pady=20)

number_input = tk.Entry(master=window)
number_input.pack()

go_button =tk.Button(
    master=window , text='ได้แก่',
    command=show_output,width=20,height=15
    )
go_button.pack(pady=20)

output_lable = tk.Label(master=window)
output_lable.pack(pady=5)

window.mainloop()