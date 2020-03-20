import tkinter as tk
import Random_f as R

def save_pass():
	# x=GeneratePassword(length.get())
	f=open("Password.txt","a")
	f.write(l4.get()+"   -------	"+l.cget("text")+'\n\n')
	f.close()

def Gen():
	x=R.GeneratePass(int(length.get()))
	l.configure(text=x)

root=tk.Tk()
l4_length=tk.Label(root,text="Website Name")
l4_length.pack()
l4=tk.Entry(root)
l4.pack()
label_length=tk.Label(root,text="Number of Characters")
label_length.pack()
length=tk.Entry(root)
length.pack()
gen_button=tk.Button(root,text="Generate",command=Gen)
gen_button.pack()
l=tk.Label(root)
l.pack()
save_button=tk.Button(root,text="Save",command=save_pass)
save_button.pack()
root.mainloop()