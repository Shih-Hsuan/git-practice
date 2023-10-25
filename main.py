# GUI 密碼管理器
from tkinter import messagebox
from tkinter import *
from unicodedata import name
from PIL import ImageTk
import json

def get_password():
    try:
        with open("password.json", "r") as f:
            password_str = f.read()
    except:
        with open("password.json", "r") as f:
             return {}
    else:
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)

def search_password():
    password_dic = get_password()
    name = account_name_input.get()
    if name in password_dic.keys():
        account = password_dic[name]["account"]
        password = password_dic[name]["password"]
        messagebox.showinfo(title=name, message=f"帳號: {account}\n密密碼: {password}")
    else:
        messagebox.showwarning(title="搜尋失敗", message="無此帳號名稱")

def add_password():
    password_dic = get_password()
    name = account_name_input.get()
    account = account_input.get()
    password = password_input.get()

    if name=="" or account =="" or password=="":
        messagebox.showerror(title="新增失敗",message="輸入框不可為空")
    elif name in password_dic.keys():
        messagebox.showerror(title="新增失敗",message="已有此帳號名稱")
    else:
        password_dic[name] = {
            "account": account,
            "password": password
        }

        with open("password.json", "w") as f:
            f.write(json.dumps(password_dic))
        
        # 已有此帳號清空
        account_name_input.delete(0, 'end')
        account_input.delete(0, 'end')
        password_input.delete(0, 'end')

        messagebox.showinfo(title="新增成功",message="新增成功")

window = Tk()
window.config(padx=50,pady=50)
# lock 
lock = ImageTk.PhotoImage(file="lock.png")
canvas = Canvas(width=224,height=224)
canvas.create_image(112,112,image=lock)
canvas.grid(row=0,column=0,columnspan=2)
# account_name
account_name_label = Label(text="帳戶名稱")
account_name_label.grid(row=1,column=0)
account_name_input = Entry(width=25) 
account_name_input.grid(row=1,column=1) 
# account
account_label = Label(text="帳戶")
account_label.grid(row=2,column=0)
account_input = Entry(width=25) 
account_input.grid(pady=5,row=2,column=1) 
# password
password_label = Label(text="密碼")
password_label.grid(row=3,column=0) 
password_input = Entry(width=25) 
password_input.grid(row=3,column=1) 
# search_button
search_button = Button(text="收尋",width=35,bg="#8E8E8E",fg="white",command=search_password)
search_button.grid(pady=5,row=4,column=0,columnspan=2)
# add_button
add_button = Button(text="新增",width=35,bg="#0066cc",fg="white",command=add_password)
add_button.grid(row=5,column=0,columnspan=2)



window.mainloop()

height_input = Entry(width=25) 
height_input.grid(row=0,column=1) 
cm_label = Label(text="公分") 
cm_label.grid(row=0,column=3) 