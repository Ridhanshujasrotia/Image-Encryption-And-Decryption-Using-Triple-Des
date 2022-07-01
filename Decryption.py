#importing important module
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pyDes import *


global img
global key


# creating root object
root = Tk()

# defining size of window
root.geometry("770x550")

# setting up the title of window
root.title("Image Security With Encryption")


out = "Decrypted.jpg"
fig = plt.figure()
ax = fig.subplots()

#==============================================#

#file opening function
def openfile():
    global path
    path = filedialog.askopenfilename()
    path_data = plt.imread(path)
    img = path
  
       
def imgPath():
    return path


# clicked function 1
def clicked1():
    messagebox.showinfo('INFO', 'DECRYPTION DONE')
    


# Function to Display Image
def imgdis(img):
    file = mpimg.imread(img)
    imgplot = plt.imshow(file)
    ax.axis('off')
    plt.show()
    
    
#function for the key
def forKey():
    key = txtkey.get()
    print("Your key = ", key)
    return key



# Function to Encrypt an File with Triple DES
def decrypt(key, img, output=out):
    with open(img, 'rb') as file1:
        ciphertext = file1.read()
        cipher_decrypt = triple_des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        plaintext = cipher_decrypt.decrypt(ciphertext)
    with open(output, 'wb') as file2:
        file2.write(plaintext)
        print("Decryption Complete.")
        clicked1()



# exit function
def qExit():
    root.destroy()


# labels for heading
lblInfo = Label(root, font=('arial', 30, 'bold'),
                text="  IMAGE OPERATION ",
                fg="Black", bd=10, anchor='w')
lblInfo.grid(row=1, column=3)


# labels for decryption
lblInfo = Label(root, font=('arial', 20, 'bold'),
                text=" (DECRYPTION) ",
                fg="Black", bd=10, anchor='w')
lblInfo.grid(row=2, column=3)



# labels line 1
lblline1 = Label(root, font=('arial', 16, 'bold'),
                 text="==============================", bd=16, anchor="w")
lblline1.grid(row=3, column=3)



# Choose button
btnchoose2 = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="choose", bg="grey",command=openfile)
btnchoose2.grid(row=4, column=3)



# labels for the key entry
lblkey = Label(root, font=('arial', 16, 'bold'),
               text="Enter The Key", bd=16, anchor="w")
lblkey.grid(row=5, column=1)



# Entry box for the key
txtkey = Entry(root, font=('arial', 16, 'bold'), bd=10, insertwidth=4,
               bg="powder blue", justify='right')
txtkey.grid(row=5, column=3)



# Decryption button
btndecrypt = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="decrypt", bg="grey",command= lambda :decrypt(forKey(), imgPath(), out))
btndecrypt.grid(row=6, column=3)



# labels line 2
lblline2 = Label(root, font=('arial', 16, 'bold'),
                 text="==============================", bd=16, anchor="w")
lblline2.grid(row=7, column=3)



# labels for Name
lblname = Label(root, font=('arial', 16, 'bold'),
               text="Ridhanshu Jasrotia (2017359)", bd=16, anchor="w")
lblname.grid(row=8, column=3)



# Exit button
btnExit = Button(root, padx=16, bd=10, fg="white", font=('arial', 10, 'bold'), width=7, text="Exit", bg="grey",
                 command=qExit)
btnExit.grid(row=8, column=4)


# keeps window alive
root.mainloop()