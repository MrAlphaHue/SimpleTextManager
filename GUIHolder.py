from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open():
	#파일 대화창을 askopenfile을 이용해서 만들고, 동시에 읽는다
    file = filedialog.askopenfile(parent=window, mode='r')
    if file != None:
        lines = file.read()
        # 1.0은 line.column이다.
        #line은 1부터 시작하고 column은 0부터 시작함..
        text.insert('1.0', lines)
        file.close()
        
def save():
	#쓰고 저장하는 기능
    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None:
        lines = text.get('1.0', END+'-1c') # 마지막에서 1 char 뺀다, \n제거!
        file.write(lines)
        file.close()
        
def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()
        
def about():
    label = messagebox.showinfo("About", "메모장 프로그램")

#창 생성
window = Tk()
text = Text(window, height=30, width=80)
text.pack()

#메뉴를 붙인다
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="저장하기", command=save)
filemenu.add_command(label="종료", command=exit)

helpmenu = Menu(menu, tearoff=0) # 자르는 선

menu.add_cascade(label="도움말", menu=helpmenu)
helpmenu.add_command(label="프로그램 정보", command=about)

window.mainloop()