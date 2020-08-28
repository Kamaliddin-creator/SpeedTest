from speedtest import Speedtest
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('540x400')
root.resizable(width = False, height = False)
root['bg'] = '#ccc'
root.title('Speedtest by Grapple')

st = Speedtest()

def test_speed():
	download_speed = float(str(st.download())[0:2] + "." + str(round(st.download(), 2))[1]) * 0.125
	upload_speed = float(str(st.download())[0:2] + "." + str(round(st.upload(), 2))[1]) * 0.125

	messagebox.showinfo("Скорость скачивания(MB/s)", download_speed)
	messagebox.showinfo("Скорость загрузки(MB/s)", upload_speed)

lbl = Label(text='This is Speedtest programm that created just with python!',
			foreground='#fff', background='#000', font = 'Montserrat 15')

lbl2 = Label(text='Это программа для измерения скорости интернета,',
			foreground='#fff', background='#000', font = 'Montserrat 15')
lbl2_con = Label(text='созданная на Python!',
			foreground='#fff', background='#000', font = 'Montserrat 15')

lbl3 = Label(text='Вам придётся немножко подождать для того чтобы',
			foreground='#fff', background='red', font = 'Montserrat 15')
lbl3_con = Label(text='программа смогла измерить стабильную скорость',
			foreground='#fff', background='red', font = 'Montserrat 15')
lbl3_con_con = Label(text='интернета',
			foreground='#fff', background='red', font = 'Montserrat 15')

lbl.place(x = 10, y = 10)

lbl2.place(x = 10, y = 45)
lbl2_con.place(x = 10, y = 80)

lbl3.place(x = 10, y = 115)
lbl3_con.place(x = 10, y = 140)
lbl3_con_con.place(x = 10, y = 165)

test = Button(text='TESTSPEED', 
			  foreground='#fff', 
			  background='#000', 
			  activebackground='#111',
			  activeforeground='#fff',
			  padx='50',
			  pady='20',
			  font='Montserrat 20',
			  relief='flat',
			  command=test_speed)
test.place(relx=0.25, rely=0.5)



root.mainloop()