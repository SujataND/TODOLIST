#kets import the tkinter module to create GUIs
import tkinter


#lets use dir() functionto see whats inside the tkinter module
#print(dir(tkinter))
# Function to add a task to the to-do list
def add_task():
  task = entry.get()
  if task:
    listbox.insert(tkinter.END, task)
    entry.delete(0, tkinter.END)


# Function to delete a selected task from the to-do list
def delete_task():
  try:
    index = listbox.curselection()
    listbox.delete(index)
  except:
    pass


#lets create an empty GUI/root gui
root = tkinter.Tk()

#lets define the width and height off GUI
root.geometry('200x250')
root.resizable(width=False, height=False)

#lets change the title
root.title('To Do List')

#lets ad entry width
entry = tkinter.Entry(root)
entry.pack()

# Create the "Add" button
add_button = tkinter.Button(root, text='Add Task', command=add_task)
add_button.pack()

# Create the to-do list
listbox = tkinter.Listbox(root)
listbox.pack()

# Create the "Delete" button
delete_button = tkinter.Button(root, text='Delete Task', command=delete_task)
delete_button.pack()

#lets call the mainloop function
root.mainloop()
