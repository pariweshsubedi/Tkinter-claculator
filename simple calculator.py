import Tkinter as tk
top= tk.Tk();
top.title("Simple calculator")

def click(key):
    if key=="=":
        str1 = "0123456789."
        if entry.get()[0] in str1:
            result =  eval(entry.get())
            entry.insert(tk.END, "=" + str(result))
              
    else:
        entry.insert(tk.END,key)

button_list=[
    '9','8','7',
    '6','5','4',
    '3','2','1',
    '+','0','-',
    "*","/","="
]

entry= tk.Entry(top, width=60)
entry.grid(row=1, columnspan=15)
r=2
c=0
for b in button_list:
    rel="ridge"
    command= lambda x=b: click(x)
    tk.Button(top, text=b, width=20, relief=rel, command=command).grid(row=r, column=c)
    c+=1
    if c>2 and r>=2:
        c=0
        r+=1
    

top.mainloop()
