#Kindly Enter Fullscreen in The NoVNC Module(second button on top right)

import tkinter as tk



window=tk.Tk()
window.title('Anime City Metro Map')
window.geometry('100x100')
window.configure(bg='Violet')

c=tk.Canvas(window, width = 1500, height = 1000)
c.pack()

stn_Al=['Infinity Castle','Manevolent Shrine','Infinite Void','Gum-Gum Airport','Chimaera Garden','Wibyte','Butterfly Mansion','Soul Society Park','Shibuya Station','Jujutsu High','Swordsmith Village']
x_s = 50
y_s = 200
d_stn= 130
r_stn=6
allstations = stn_Al
#for loop for line
for stn in stn_Al:
    # line and stn name
    if stn != stn_Al[-1]:
        c.create_line(x_s,y_s,x_s+d_stn,y_s,fill = 'DarkOrange')
    c.create_oval(x_s-r_stn,y_s-r_stn,x_s+r_stn,y_s + r_stn, fill = 'DarkOrange')
    c.create_text(x_s,y_s+30,text = stn)
    x_s=x_s+d_stn
startstation=tk.StringVar()
d_start= tk.OptionMenu(window,startstation,*allstations)
d_start.place(x=50,y=350)





























tk.mainloop()