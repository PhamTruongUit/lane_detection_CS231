from main import *
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog 
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk,Image
import imageio

root = Tk()
root.columnconfigure(0, weight=1) 

class NewWindow():
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20 
        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        self.update_image()
    def update_image(self):
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = Image.fromarray(self.image) 
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.window.after(self.interval, self.update_image)

def show_video():
    new = Toplevel(root)
    new.title("Result with lane") 
    NewWindow(new,cv2.VideoCapture('output.mp4'))
    mainloop()

def show_img():
    new = Toplevel(root)
    new.title("Result with lane") 
    new.geometry("720x405") 
    img = Image.open('output.jpg').resize((720,405))
    img = ImageTk.PhotoImage(img)
    panel = Label(new, image = img)
    panel.pack(side = 'bottom', fill = 'both', expand = 'yes')      
    mainloop()  

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
                                            filetypes = (("videos", "*.mp4*"),
                                            ("images", "*.jpg*"), 
                                            ("images", "*.png*"), 
                                            ("all files", "*.*"))) 
    file_explorer.configure(text="File Opened: "+filename)  
def main():
    file = file_explorer.cget('text')[13:]
    if file[-3:] != 'mp4' and file[-3:] != 'jpg' and file[-3:] != 'png':
        messagebox.showwarning('Error', 'Please check file again!')
    elif file[-3:] == 'mp4':
        try:
            lane_video(file,'output.mp4')
        except:
            messagebox.showwarning('Error', 'Please check input again!')
    else:
        try:
            lane_image(file)
        except:
            messagebox.showwarning('Error', 'Please check input again!')
         
def show():
    file = file_explorer.cget('text')[13:]
    if file[-3:] != 'mp4' and file[-3:] != 'jpg' and file[-3:] != 'png':
        messagebox.showwarning('Error', 'Please check file again!')
    elif file[-3:] == 'mp4':
        try:
            show_video()
        except:
            messagebox.showwarning('Error', 'Please check input again!')
    else:
        try:
            show_img()
        except:
            messagebox.showwarning('Error', 'Please check input again!')
        
    
if __name__ == "__main__":
    root.title('Lane Detection')
    myFont = font.Font(family = 'Helvetica', size = 16)
    file_explorer = Label(root, text = "Link")
    file_explorer.grid(row = 1,sticky = N)
    button_explore = Button(root, text = "Browse Files", command = browseFiles)
    button_explore.grid(row = 2, sticky = N)    
    run = Button(root, text= "Run", command=main)
    run.grid(row = 3, sticky = N)
    play = Button(root, text= "Show Result", command=show)
    play.grid(row = 4, sticky = N)
    exit = Button(root, text= "Exit", command=exit)
    exit.grid(row = 5, sticky = N)
    root.geometry("450x280")
    mainloop()