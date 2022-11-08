import tkinter as tk
from win32api import Beep
import webbrowser
e1 = 0
b1 = 0
def doit():
    global e1
    global b1
    Beep(200,300)
    Beep(250,300)
    Beep(500,300)
    Beep(1000,300)
    Beep(2000,300)
    Beep(4000,300)
    Beep(8000,300)
    Beep(16000,300)
    e1 = tk.Entry()
    e1.insert(0, '들린 횟수를 입력하세요')
    e1.pack()
    b1 = tk.Button(text="완료",command=완료)
    b1.pack()
def 완료():
    value = int(e1.get())
    if value == 1 or value == 2:
        label = tk.Label(text="당신의 청력나이는 40대 이상입니다.\n가까운 이비인후과를 찾아가 보세요.\n삐 하는 소리는 총 8번 들렸습니다.")
        webbrowser.open("https://map.naver.com/v5/search/%EC%9D%B4%EB%B9%84%EC%9D%B8%ED%9B%84%EA%B3%BC")
    elif value == 3 or value == 4:
        label = tk.Label(text="당신의 청력나이는 30대입니다.\n삐 하는 소리는 총 8번 들렸습니다.")
    elif value == 5 or value == 6:
        label = tk.Label(text="당신의 청력나이는 20대입니다.\n삐 하는 소리는 총 8번 들렸습니다.")
    elif value == 7 or value == 8:
        label = tk.Label(text="당신의 청력나이는 10대입니다.\n삐 하는 소리는 총 8번 들렸습니다.")
    else:
        label = tk.Label(text="삐 하는 소리는 총 8번 들렸습니다.")
    label.pack()
window = tk.Tk()
window.title("청력 테스트")
window.geometry("300x300")

hello = tk.Label(text="시작 버튼을 누르면 삐 하는 소리가 나옵니다.\n몇 번 들리는지 집중해서 들어보세요.")
hello.pack()
button = tk.Button(text="시작",command=doit)
button.pack()

tk.mainloop()