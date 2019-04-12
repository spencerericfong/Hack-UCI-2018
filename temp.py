#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Feb 04, 2018 01:39:18 AM
import sys
import os
import PIL.Image
from PIL import ImageTk, Image

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import onelinesecurity_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    onelinesecurity_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    onelinesecurity_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    onelinesecurity_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    onelinesecurity_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("305x150+469+216")
        top.title("Oneline Security")
        top.configure(background="#d9d9d9")



        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(width=1094)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Edit Whitelist/Blacklist",underline="-1",)
        self.TNotebook1_t2 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Add to Database",underline="-1",)
        self.notebook_window1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.notebook_window1, padding=3)
        self.TNotebook1.tab(2, text="Settings",underline="-1",)

        self.Edit_Blacklist_Canvas = Canvas(self.TNotebook1_t1)
        self.Edit_Blacklist_Canvas.place(relx=0.08, rely=0.14, relheight=0.41
                , relwidth=0.35)
        self.Edit_Blacklist_Canvas.configure(background="white")
        self.Edit_Blacklist_Canvas.configure(borderwidth="2")
        self.Edit_Blacklist_Canvas.configure(insertbackground="black")
        self.Edit_Blacklist_Canvas.configure(relief=RIDGE)
        self.Edit_Blacklist_Canvas.configure(selectbackground="#c4c4c4")
        self.Edit_Blacklist_Canvas.configure(selectforeground="black")
        self.Edit_Blacklist_Canvas.configure(width=378)
        

        self.Edit_Whitelist_Canvas = Canvas(self.TNotebook1_t1)
        self.Edit_Whitelist_Canvas.place(relx=0.55, rely=0.14, relheight=0.41
                , relwidth=0.35)
        self.Edit_Whitelist_Canvas.configure(background="white")
        self.Edit_Whitelist_Canvas.configure(borderwidth="2")
        self.Edit_Whitelist_Canvas.configure(insertbackground="black")
        self.Edit_Whitelist_Canvas.configure(relief=RIDGE)
        self.Edit_Whitelist_Canvas.configure(selectbackground="#c4c4c4")
        self.Edit_Whitelist_Canvas.configure(selectforeground="black")
        self.Edit_Whitelist_Canvas.configure(width=378)

        
        self.Edit_Blacklist_Label = Label(self.TNotebook1_t1)
        self.Edit_Blacklist_Label.place(relx=0.24, rely=0.09, height=21
                , width=49)
        self.Edit_Blacklist_Label.configure(background="#d9d9d9")
        self.Edit_Blacklist_Label.configure(disabledforeground="#a3a3a3")
        self.Edit_Blacklist_Label.configure(foreground="#000000")
        self.Edit_Blacklist_Label.configure(text='''Blacklist''')

        self.Edit_Whitelist_Label = Label(self.TNotebook1_t1)
        self.Edit_Whitelist_Label.place(relx=0.72, rely=0.09, height=21
                , width=52)
        self.Edit_Whitelist_Label.configure(background="#d9d9d9")
        self.Edit_Whitelist_Label.configure(disabledforeground="#a3a3a3")
        self.Edit_Whitelist_Label.configure(foreground="#000000")
        self.Edit_Whitelist_Label.configure(text='''Whitelist''')

        self.Edit_Blacklist_List = Listbox(self.TNotebook1_t1)
        for val, file in enumerate(os.listdir("/home/pi/Desktop/HackUCI/blacklisted/")):
            self.Edit_Blacklist_List.insert(val, os.path.splitext(file)[0])
        self.Edit_Blacklist_List.pack()
        
        self.Edit_Blacklist_List.place(relx=0.16, rely=0.59, relheight=0.2
                , relwidth=0.21)
        self.Edit_Blacklist_List.configure(background="white")
        self.Edit_Blacklist_List.configure(disabledforeground="#a3a3a3")
        self.Edit_Blacklist_List.configure(font="TkFixedFont")
        self.Edit_Blacklist_List.configure(foreground="#000000")
        self.Edit_Blacklist_List.configure(setgrid="1")
        self.Edit_Blacklist_List.configure(width=194)

        def selected_b(event):
            value = self.Edit_Blacklist_List.get(self.Edit_Blacklist_List.curselection()[0])
            print(value)
            path = "/home/pi/Desktop/HackUCI/blacklisted/"+value + '.jpg'     
            img = ImageTk.PhotoImage(PIL.Image.open(path))
            self.Edit_Blacklist_Canvas.create_image(300,250,image=img)
            root.mainloop()
            
        self.Edit_Blacklist_List.bind('<ButtonRelease-1>', selected_b)
        

        self.Edit_Whitelist_List = Listbox(self.TNotebook1_t1)
        for val, file in enumerate(os.listdir("/home/pi/Desktop/HackUCI/whitelisted/")):
            self.Edit_Whitelist_List.insert(val, os.path.splitext(file)[0])
            
        self.Edit_Whitelist_List.pack()
        self.Edit_Whitelist_List.place(relx=0.63, rely=0.59, relheight=0.2
                , relwidth=0.21)
        self.Edit_Whitelist_List.configure(background="white")
        self.Edit_Whitelist_List.configure(disabledforeground="#a3a3a3")
        self.Edit_Whitelist_List.configure(font="TkFixedFont")
        self.Edit_Whitelist_List.configure(foreground="#000000")
        self.Edit_Whitelist_List.configure(setgrid="1")
        self.Edit_Whitelist_List.configure(width=224)
        

        def selected_w(event):
            value=self.Edit_Whitelist_List.get(self.Edit_Whitelist_List.curselection()[0])
            print(value)
            path = "/home/pi/Desktop/HackUCI/whitelisted/"+value + '.jpg'
            img = ImageTk.PhotoImage(PIL.Image.open(path))
            self.Edit_Whitelist_Canvas.create_image(300,250,image=img)
            root.mainloop()

        self.Edit_Whitelist_List.bind('<ButtonRelease-1>', selected_w)


        self.Move_to_Whitelist = Button(self.TNotebook1_t1)
        self.Move_to_Whitelist.place(relx=0.2, rely=0.83, height=24, width=123)
        self.Move_to_Whitelist.configure(activebackground="#d9d9d9")
        self.Move_to_Whitelist.configure(activeforeground="#000000")
        self.Move_to_Whitelist.configure(background="#d9d9d9")
        self.Move_to_Whitelist.configure(disabledforeground="#a3a3a3")
        self.Move_to_Whitelist.configure(foreground="#000000")
        self.Move_to_Whitelist.configure(highlightbackground="#d9d9d9")
        self.Move_to_Whitelist.configure(highlightcolor="black")
        self.Move_to_Whitelist.configure(pady="0")
        self.Move_to_Whitelist.configure(text='''Move to Whitelist >>''')

        def move_to_whitelist(event):
            if self.Edit_Blacklist_List.size() != 0:
                value = self.Edit_Blacklist_List.get(self.Edit_Blacklist_List.curselection())
                path = "blacklisted/"+value + '.jpg'
                os.rename(path, "whitelisted/"+value + '.jpg')
                print('f')
                #self.Edit_Whitelist_List.insert(self.Edit_Blacklist_List.curselection())
                self.Edit_Blacklist_List.delete(self.Edit_Blacklist_List.curselection())
                self.Edit_Whitelist_List.delete(0,END)
                self.Edit_Whitelist_List.insert(0,self.Edit_Blacklist_List.curselection())
                root.mainloop()

        self.Move_to_Whitelist.bind('<Button-1>', move_to_whitelist)
        
            

        self.Move_to_Blacklist = Button(self.TNotebook1_t1)
        self.Move_to_Blacklist.place(relx=0.68, rely=0.83, height=24, width=120)
        self.Move_to_Blacklist.configure(activebackground="#d9d9d9")
        self.Move_to_Blacklist.configure(activeforeground="#000000")
        self.Move_to_Blacklist.configure(background="#d9d9d9")
        self.Move_to_Blacklist.configure(disabledforeground="#a3a3a3")
        self.Move_to_Blacklist.configure(foreground="#000000")
        self.Move_to_Blacklist.configure(highlightbackground="#d9d9d9")
        self.Move_to_Blacklist.configure(highlightcolor="black")
        self.Move_to_Blacklist.configure(pady="0")
        self.Move_to_Blacklist.configure(text='''<< Move to Blacklist''')


        def move_to_blacklist(event):
            if self.Edit_Whitelist_List.size() != 0:
                value = self.Edit_Whitelist_List.get(self.Edit_Whitelist_List.curselection())
                path = "whitelisted/"+value + '.jpg'
                os.rename(path, "blacklisted/"+value + '.jpg')
                #self.Edit_Blacklist_List.insert(self.Edit_Whitelist_List.curselection())
                self.Edit_Whitelist_List.delete(self.Edit_Whitelist_List.curselection())
                self.Edit_Blacklist_List.delete(0,END)
                self.Edit_Blacklist_List.insert(0,self.Edit_Whitelist_List.curselection())
                root.mainloop()
        
        self.Move_to_Blacklist.bind('<Button-1>', move_to_blacklist)
        

        self.Add_Blacklist_Canvas = Canvas(self.TNotebook1_t2)
        self.Add_Blacklist_Canvas.place(relx=0.08, rely=0.12, relheight=0.41
                , relwidth=0.35)
        self.Add_Blacklist_Canvas.configure(background="white")
        self.Add_Blacklist_Canvas.configure(borderwidth="2")
        self.Add_Blacklist_Canvas.configure(insertbackground="black")
        self.Add_Blacklist_Canvas.configure(relief=RIDGE)
        self.Add_Blacklist_Canvas.configure(selectbackground="#c4c4c4")
        self.Add_Blacklist_Canvas.configure(selectforeground="black")
        self.Add_Blacklist_Canvas.configure(width=378)

        self.Add_Whitelist_Canvas = Canvas(self.TNotebook1_t2)
        self.Add_Whitelist_Canvas.place(relx=0.54, rely=0.12, relheight=0.41
                , relwidth=0.35)
        self.Add_Whitelist_Canvas.configure(background="white")
        self.Add_Whitelist_Canvas.configure(borderwidth="2")
        self.Add_Whitelist_Canvas.configure(insertbackground="black")
        self.Add_Whitelist_Canvas.configure(relief=RIDGE)
        self.Add_Whitelist_Canvas.configure(selectbackground="#c4c4c4")
        self.Add_Whitelist_Canvas.configure(selectforeground="black")
        self.Add_Whitelist_Canvas.configure(width=378)
        
        self.Add_Blacklist_Name = Entry(self.TNotebook1_t2)
        self.Add_Blacklist_Name.place(relx=0.17, rely=0.58, relheight=0.05
                , relwidth=0.2)
        self.Add_Blacklist_Name.configure(background="white")
        self.Add_Blacklist_Name.configure(disabledforeground="#a3a3a3")
        self.Add_Blacklist_Name.configure(font="TkFixedFont")
        self.Add_Blacklist_Name.configure(foreground="#000000")
        self.Add_Blacklist_Name.configure(insertbackground="black")
        self.Add_Blacklist_Name.configure(width=214)

        self.Add_Blacklist_Name_Label = Label(self.TNotebook1_t2)
        self.Add_Blacklist_Name_Label.place(relx=0.12, rely=0.58, height=21
                , width=38)
        self.Add_Blacklist_Name_Label.configure(background="#d9d9d9")
        self.Add_Blacklist_Name_Label.configure(disabledforeground="#a3a3a3")
        self.Add_Blacklist_Name_Label.configure(foreground="#000000")
        self.Add_Blacklist_Name_Label.configure(text='''Name''')

        self.Add_Whitelist_Name = Entry(self.TNotebook1_t2)
        self.Add_Whitelist_Name.place(relx=0.64, rely=0.58, relheight=0.05
                , relwidth=0.2)
        self.Add_Whitelist_Name.configure(background="white")
        self.Add_Whitelist_Name.configure(disabledforeground="#a3a3a3")
        self.Add_Whitelist_Name.configure(font="TkFixedFont")
        self.Add_Whitelist_Name.configure(foreground="#000000")
        self.Add_Whitelist_Name.configure(insertbackground="black")
        self.Add_Whitelist_Name.configure(width=194)

        self.Add_Whitelist_Name_Label = Label(self.TNotebook1_t2)
        self.Add_Whitelist_Name_Label.place(relx=0.6, rely=0.58, height=21
                , width=38)
        self.Add_Whitelist_Name_Label.configure(background="#d9d9d9")
        self.Add_Whitelist_Name_Label.configure(disabledforeground="#a3a3a3")
        self.Add_Whitelist_Name_Label.configure(foreground="#000000")
        self.Add_Whitelist_Name_Label.configure(text='''Name''')

        self.Add_Blacklist_Label = Label(self.TNotebook1_t2)
        self.Add_Blacklist_Label.place(relx=0.24, rely=0.08, height=21, width=49)

        self.Add_Blacklist_Label.configure(background="#d9d9d9")
        self.Add_Blacklist_Label.configure(disabledforeground="#a3a3a3")
        self.Add_Blacklist_Label.configure(foreground="#000000")
        self.Add_Blacklist_Label.configure(text='''Blacklist''')

        self.Add_Whitelist_Label = Label(self.TNotebook1_t2)
        self.Add_Whitelist_Label.place(relx=0.7, rely=0.08, height=21, width=52)
        self.Add_Whitelist_Label.configure(background="#d9d9d9")
        self.Add_Whitelist_Label.configure(disabledforeground="#a3a3a3")
        self.Add_Whitelist_Label.configure(foreground="#000000")
        self.Add_Whitelist_Label.configure(text='''Whitelist''')

        self.Submit_Addition = Button(self.TNotebook1_t2)
        self.Submit_Addition.place(relx=0.45, rely=0.77, height=64, width=89)
        self.Submit_Addition.configure(activebackground="#d9d9d9")
        self.Submit_Addition.configure(activeforeground="#000000")
        self.Submit_Addition.configure(background="#d9d9d9")
        self.Submit_Addition.configure(disabledforeground="#a3a3a3")
        self.Submit_Addition.configure(foreground="#000000")
        self.Submit_Addition.configure(highlightbackground="#d9d9d9")
        self.Submit_Addition.configure(highlightcolor="black")
        self.Submit_Addition.configure(pady="0")
        self.Submit_Addition.configure(text='''Submit''')
        self.Submit_Addition.configure(width=89)

        self.Choose_Blacklist_Photo = ttk.Button(self.TNotebook1_t2)
        self.Choose_Blacklist_Photo.place(relx=0.18, rely=0.68, height=35
                , width=116)
        self.Choose_Blacklist_Photo.configure(takefocus="")
        self.Choose_Blacklist_Photo.configure(text='''Choose Photo''')
        self.Choose_Blacklist_Photo.configure(width=116)

        self.Choose_Whitelist_Photo = ttk.Button(self.TNotebook1_t2)
        self.Choose_Whitelist_Photo.place(relx=0.65, rely=0.68, height=35
                , width=116)
        self.Choose_Whitelist_Photo.configure(takefocus="")
        self.Choose_Whitelist_Photo.configure(text='''Choose Photo''')
        self.Choose_Whitelist_Photo.configure(width=96)

        self.Email_Username = ttk.Entry(self.notebook_window1)
        self.Email_Username.place(relx=0.06, rely=0.21, relheight=0.05
                , relwidth=0.17)
        self.Email_Username.configure(width=186)
        self.Email_Username.configure(takefocus="")
        #self.Email_Username.configure(cursor="ibeam")

        self.Email_Provider = ttk.Combobox(self.notebook_window1)
        self.Email_Provider.place(relx=0.27, rely=0.21, relheight=0.05
                , relwidth=0.13)
        self.Email_Provider.configure(textvariable=onelinesecurity_support.combobox)
        self.Email_Provider.configure(width=143)
        self.Email_Provider.configure(takefocus="")

        self.At = Label(self.notebook_window1)
        self.At.place(relx=0.23, rely=0.23, height=21, width=37)
        self.At.configure(background="#d9d9d9")
        self.At.configure(disabledforeground="#a3a3a3")
        self.At.configure(foreground="#000000")
        self.At.configure(text='''@''')
        self.At.configure(width=37)

        self.Email_Label = Label(self.notebook_window1)
        self.Email_Label.place(relx=0.06, rely=0.17, height=21, width=35)
        self.Email_Label.configure(background="#d9d9d9")
        self.Email_Label.configure(disabledforeground="#a3a3a3")
        self.Email_Label.configure(foreground="#000000")
        self.Email_Label.configure(text='''Email''')

        self.Phone_Label = Label(self.notebook_window1)
        self.Phone_Label.place(relx=0.06, rely=0.33, height=21, width=40)
        self.Phone_Label.configure(background="#d9d9d9")
        self.Phone_Label.configure(disabledforeground="#a3a3a3")
        self.Phone_Label.configure(foreground="#000000")
        self.Phone_Label.configure(text='''Phone''')

        self.Phone_Number = ttk.Entry(self.notebook_window1)
        self.Phone_Number.place(relx=0.06, rely=0.38, relheight=0.05
                , relwidth=0.18)
        self.Phone_Number.configure(width=196)
        self.Phone_Number.configure(takefocus="")
        #self.Phone_Number.configure(cursor="ibeam")

        self.Submit_Contact_Info_Button = ttk.Button(self.notebook_window1)
        self.Submit_Contact_Info_Button.place(relx=0.17, rely=0.53, height=35
                , width=116)
        self.Submit_Contact_Info_Button.configure(takefocus="")
        self.Submit_Contact_Info_Button.configure(text='''Submit''')
        self.Submit_Contact_Info_Button.configure(width=116)

        self.Contact_Info_Label = Label(self.notebook_window1)
        self.Contact_Info_Label.place(relx=0.13, rely=0.08, height=41, width=174)

        self.Contact_Info_Label.configure(background="#d9d9d9")
        self.Contact_Info_Label.configure(disabledforeground="#a3a3a3")
        self.Contact_Info_Label.configure(foreground="#000000")
        self.Contact_Info_Label.configure(text='''Contact Info''')
        self.Contact_Info_Label.configure(width=174)

        self.Phone_Provider = ttk.Combobox(self.notebook_window1)
        self.Phone_Provider.place(relx=0.27, rely=0.38, relheight=0.05
                , relwidth=0.13)
        self.Phone_Provider.configure(textvariable=onelinesecurity_support.combobox)
        self.Phone_Provider.configure(width=143)
        self.Phone_Provider.configure(takefocus="")

        self.Provider_Label = Label(self.notebook_window1)
        self.Provider_Label.place(relx=0.3, rely=0.33, height=21, width=50)
        self.Provider_Label.configure(background="#d9d9d9")
        self.Provider_Label.configure(disabledforeground="#a3a3a3")
        self.Provider_Label.configure(foreground="#000000")
        self.Provider_Label.configure(text='''Provider''')


   
        

    @staticmethod
    def popup1(event):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)



if __name__ == '__main__':
    vp_start_gui()



