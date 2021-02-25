from tkinter import *

def pickName():
    root.destroy()

    ns = Tk()
    ns.title('Blochat | Pick Username')
    ns.geometry("300x300")
    ns.configure(background="#386FA4")
    Label(ns, text="hi").pack()
    ns.mainloop()

root = Tk()
#https://coolors.co/133c55-386fa4-59a5d8-84d2f6-91e5f6
root.title('Blochat')
#root.iconbitmap("../CTX/blochat_icon.ico")
root.configure(background="#386FA4")
#photo1 = PhotoImage(file="../CTX/blochat_icon.png")
#Label(root, image=photo1, bg="#386FA4").grid(row=1, column=0, columnspan=2, rowspan=2)
Label(root, text="Blochat", bg="#386FA4", fg="white", font="none 100 bold").grid(row=1, column=3, rowspan = 2)
Label(root, text="", bg="#386FA4", fg="white", font="none 20 bold").grid(row=4, column=0)
Label(root, text="Server IP:", bg="#386FA4", fg="white", font="none 15 bold").grid(row=5, column=0, sticky=E)
ipBox = Entry(root, width=15, bg="#59A5D8", fg="white").grid(row=5, column=1, sticky=W)
Button(root, text="Join Server", command=pickName).grid(row=5, column=1, sticky=E)
Button(root, text="Quit", command=root.quit).grid(row=5, column=5)
root.mainloop()

