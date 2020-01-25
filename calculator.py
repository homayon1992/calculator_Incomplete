from tkinter import *


def cole(src, side):
    pass


def button(src, side, text, command=None):
   pass


class app(Frame):
    def __init__(self, root=Tk(), width=364, height=425):
        Frame.__init__(self)
        self.option_add("*Font", 'arial')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Simple Calculator")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display, state=DISABLED, justify='right', bd=20, bg="silver").pack(side=TOP, expand=YES,
                                                                                              fill=BOTH)
        clrChar = "Clear"
        button(self, TOP, clrChar, lambda appObj=display, i=clrChar: appObj.set(''))

        for btnNum in ("789/", "456*", "123-", "0.+"):

            FunctionNum = cole(self, TOP)
            for fEquals in btnNum:
                button(FunctionNum, LEFT, fEquals,
                       lambda appObj=display, i=fEquals: appObj.set(appObj.get() + i))
                EqualsButton = cole(self, TOP)

        for fEquals in "=":
            if fEquals == "=":
                btnEquals = button(EqualsButton, LEFT, fEquals)
                btnEquals.bind('<ButtonRelease-1>',
                               lambda e, s=self, appObj=display: s.result(appObj), "+")
            else:
                btnEquals = button(EqualsButton, LEFT, fEquals,
                                   lambda appObj=display, s=" %s " % fEquals: appObj.set(appObj.get() + s))

    def result(self, display):
        try: pass
        except: pass



if __name__ == '__main__':
    app().mainloop()


