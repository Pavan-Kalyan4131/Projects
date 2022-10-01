from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.font import Font
from tkinter import colorchooser
from PIL import ImageTk, Image

# File Menu Event Handling Functions

# To make a new file
def NewFile(t):
    global open_status
    input = str(text.get('1.0', 'end-1c')) # To check any text entered
    if input == "": return
    if open_status: # checks whether any file is open
           root.title("Untitled - Textpad")
           text.delete("1.0", "end-1c")
    else:
         data = askyesnocancel('Textpad',f"Do you want to save changes?")
         if data:
               SaveFile(False)
         elif data == False:
               text.delete("1.0", "end-1c")

# To open a file       
def OpenFile(t):
    if t:
         data = askopenfilename(initialdir = "C:/Users/Aravind/Desktop/P@van Kaly@n/Textfiles",
                                filetypes = [("Text Files", "*.txt"),
                                             ("HTML Files", "*.html"),
                                             ("Python Files", "*.py")
                                ])
         if data == '' : return True
         name = data.replace("C:/Users/Aravind/Desktop/P@van Kaly@n/Textfiles/", "")
         root.title(f"{name} - Textpad")
         file = open(data,"r")
         text.insert(INSERT, file.read())
         file.close()
         global open_status
         open_status = data
         return True
    else: return False
     
# To save a file
def SaveFile(t):
     global open_status
     if open_status: # To check whether any file is open
          file = open(open_status, 'w')
          file.write(text.get('1.0', 'end-1c'))
          file.close()
     else:
          SaveAsFile(True)

# To Save as a file
def SaveAsFile(t):
    if t:
         file = asksaveasfile(initialdir = "C:/Users/Aravind/Desktop/P@van Kaly@n/Textfiles",
                              defaultextension = '.txt',
                              filetypes = [("Text file", ".txt"),
                                           ("HTML file", ".html"),
                                           ("All files", ".*")
                                              ])
         if file is None: return True
         filetext = str(text.get('1.0','end-1c'))
         file.write(filetext)
         file.close()
         return True
    else: return False

# To Exit a window
def exit_window(t):
    input = str(text.get('1.0', 'end-1c'))
    if input == '': root.destroy()
    else:
        data = askyesnocancel('Textpad', "Do you want to save changes?")
        if data:
             SaveFile(False)
        elif data == False:
             root.destroy()
        

#Edit Menu Event Handling Functions
     
# To cut the text
def cut_text(t):
     global selected
     if t:
          selected = root.clipboard_get()
     else:
          if text.selection_get():
               selected = text.selection_get()
               text.delete('sel.first', 'sel.last')
               root.clipboard_clear()
               root.clipboard_append(selected)
               
# To copy the text
def copy_text(t):
     global selected
     if t:
          selected = root.clipboard_get()
     else:
          if text.selection_get():
                selected = text.selection_get()
                root.clipboard_clear()
                root.clipboard_append(selected)

# To paste the text
def paste_text(t):
     global selected
     if t:
          selected = root.clipboard_get()
     else:
          if selected:
               pos = text.index(INSERT)
               text.insert(pos, selected)


# Format Menu Event Handling Functions

# To select all the text
def select_text(t):
    text.tag_add('sel', '1.0', 'end')

def clear_all():
    text.delete(1.0, END)
               
# To delete the selected text
def del_text(t):
     if text.selection_get():
          text.delete('sel.first', 'sel.last')

# To make the text bold
def bold_text(t):
    
     bold_font = Font(text, text.cget("font"))
     
     bold_font.configure(weight = 'bold')
     
     text.tag_configure("bold", font = bold_font)
     
     current_tags = text.tag_names("sel.first")
     
     if "bold" in current_tags:
         text.tag_remove("bold", "sel.first", "sel.last")
     else:
         text.tag_add("bold", "sel.first", "sel.last")

# To make the text italic
def italic_text(t):
    
    italic_font = Font(text, text.cget("font"))
    
    italic_font.configure(slant = 'italic')
     
    text.tag_configure("italic", font = italic_font)
     
    current_tags = text.tag_names("sel.first")
     
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")
        
# To underline the text
def underline_text(t):
     
     underline_font = Font(text, text.cget('font'))

     underline_font.configure(underline = 1)

     text.tag_configure('underline', font = underline_font)

     current_tags = text.tag_names("sel.first")

     if "underline" in current_tags:
          text.tag_remove('underline', 'sel.first', 'sel.last')
     else:
          text.tag_add('underline', 'sel.first', 'sel.last')

#To Change the text color
def color_text():
    my_color = colorchooser.askcolor()[1]
    
    if my_color:
        color_font = Font(text, text.cget("font"))
     
        text.tag_configure("colored", font = color_font, foreground = my_color)
     
        current_tags = text.tag_names("sel.first")
     
        if "colored" in current_tags:
            text.tag_remove("colored", "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")

def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text.config(bg = my_color)

def all_text():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text.config(fg = my_color)

# Help Menu event handling functions
def abt():
    wn = Toplevel()
    wn.title('About Textpad')
    wn.geometry('1000x600')
    path = 'final-logo1.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(wn, image = img)
    label.pack()
    l = Label(wn, text = 'TextPad Project using Python', font = ('Trebuchet MS', 40, 'bold', 'underline'), fg = 'Red')
    l.pack()
    l2 = Label(wn, text = 'The Packages used in the Project are: ', font = ('Trebuchet MS', 30, 'bold'), fg = 'blue')
    l2.pack(anchor = NW, padx = 15, pady = 30)
    l3 = Label(wn, text = 'tkinter\ntkinter.messagebox\ntkinter.filedialog\ntkinter.font\nPIL', font = ('Trebuchet MS', 25, 'bold'), fg = 'Green', bg = 'orange')
    l3.pack(anchor = N, pady = 5)
    l4 = Label(wn, text = 'Instructor: Mr.VEERA PRAKASH', font = ('Trebuchet MS', 25, 'bold'), fg = 'dark orchid')
    l4.pack(anchor = SE, pady = 20)
    l5 = Label(wn, text = 'Developed by: PAVAN KALYAN C\nRoll No: 194G1A0571\nClass: II CSE - B', font = ('Trebuchet MS', 25, 'bold'), fg = 'magenta')
    l5.pack(anchor = SE)
    b = Button(wn, text = 'OK', font = ('bold', 25), bg = 'red', command = wn.destroy)
    b.pack(anchor = S)
    wn.mainloop()
    
# Main Program
root = Tk()

root.title("Untitled - Textpad")

root.geometry("1000x1000")

menubar = Menu(root)

global selected

global open_status

selected = False

open_status = False

# Adding Scroll bars
vert_scroll = Scrollbar(root)

hori_scroll = Scrollbar(root, orient = 'horizontal')

vert_scroll.pack(side = RIGHT, fill = Y)

hori_scroll.pack(side = BOTTOM, fill = X)

# Adding Text to the window
text = Text(root,height = 1000, width = 1000,font = (10), undo = True, yscrollcommand = vert_scroll.set, wrap = 'none', xscrollcommand = hori_scroll.set)

text.pack()

#Handling Scroll bars
vert_scroll.config(command = text.yview)

hori_scroll.config(command = text.xview)

#Adding Keyboard Shortcuts by binding events

root.bind('<Control-o>',OpenFile)

root.bind('<Control-s>',SaveFile)

root.bind('<Control-Shift-S>',SaveAsFile)

root.bind('<Control-n>',NewFile)

root.bind('<Control-x>',cut_text)

root.bind('<Control-v>',paste_text)

root.bind('<Control-Shift-B>',bold_text)

root.bind('<Control-Shift-I>',italic_text)

root.bind('<Control-Shift-U>',underline_text)

root.bind('<Alt-x>',exit_window)

# File Menu with event handling functions
file = Menu(menubar, tearoff = 0)
file.add_command(label = 'New', font = ('bold',12), command = lambda:NewFile(False), accelerator = "Ctrl+N")
file.add_command(label = 'Open', font = ('bold',12), command = lambda:OpenFile(True), accelerator = "Ctrl+O")
file.add_command(label = 'Save',font = ('bold',12), command = lambda:SaveFile(False), accelerator = "Ctrl+S")
file.add_command(label = 'Save As', font = ('bold',12), command = lambda:SaveAsFile(True), accelerator = "Ctrl+Shift+S")
file.add_separator()
file.add_command(label = 'Exit', font = ('bold',12), command = lambda:exit_window(False), accelerator = "Alt+X")
menubar.add_cascade(label = 'File', menu = file)

#Edit Menu with event handling functions
edit = Menu(menubar, tearoff = 0)
edit.add_command(label = 'Undo', font = ('bold',12), command = text.edit_undo, accelerator = 'Ctrl+Z')
edit.add_command(label = 'Redo', font = ('bold',12), command = text.edit_redo, accelerator = 'Ctrl+Y')
edit.add_separator()
edit.add_command(label = 'Cut',font = ('bold',12), command = lambda: cut_text(False), accelerator = 'Ctrl+X')
edit.add_command(label = 'Copy', font = ('bold',12), command =  lambda: copy_text(False), accelerator = 'Ctrl+C')
edit.add_command(label = 'Paste', font = ('bold',12), command = lambda: paste_text(False), accelerator = 'Ctrl+V')
edit.add_separator()
edit.add_command(label = 'Select All', font = ('bold',12), command = lambda: select_text(False), accelerator = 'Ctrl+A')
edit.add_command(label = 'Clear All', font = ('bold', 12), command = clear_all)
edit.add_command(label = 'Delete', font = ('bold',12), command = lambda: del_text(False), accelerator = 'Del')
menubar.add_cascade(label = 'Edit', menu = edit)

# Format Menu without event handling functions
format = Menu(menubar, tearoff = 0)
# Font submenu
font = Menu(format, tearoff = 0)
font.add_command(label = "Bold", font = ('bold', 12), accelerator = 'Ctrl+Shift+B', command = lambda:bold_text(False))
font.add_command(label = "Italic", font = ('bold', 12), accelerator = 'Ctrl+Shift+I', command = lambda:italic_text(False))
font.add_command(label = 'Underline', font = ('bold', 12), accelerator = 'Ctrl+Shift+U', command = lambda:underline_text(False))

format.add_cascade(label = 'Font', font = ('bold', 12), menu = font)
# Font Color submenu
font_color = Menu(format, tearoff = 0)
font_color.add_command(label = 'Change Selected Text color', font = ('bold', 12), command = color_text)
font_color.add_command(label = 'Change All Text color', font = ('bold', 12), command = all_text)
font_color.add_command(label = 'Change BG color', font = ('bold', 12), command = bg_color)

format.add_cascade(label = 'Font Color', font = ('bold', 12), menu = font_color)
menubar.add_cascade(label = 'Format', menu = format)

#Help Menu without event handling functions
help = Menu(menubar, tearoff = 0)
help.add_command(label = 'About Textpad', font = ('bold', 12), command = abt)
menubar.add_cascade(label = 'Help', menu = help)
     
root.config(menu = menubar)

if __name__ == '__main__':
    root.mainloop()
