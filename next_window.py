from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x200")
root.config(bg="Skyblue")
myList=StringVar()

list_label=Label(root, text="NUMBERS LIST: ")
list_label.place(x=100, y=20)
list_display=Label(root, text= "[54, 26, 93, 17, 77, 31, 44, 55, 20]" )
list_display.place(x=300, y=20)
# answer_label=Label(root, text="", textvariable=myList)
# answer_label.place(x=100, y=60)

def mergeSort(myList):

    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


# sort_button=Button(root, text="sort list", command=mergeSort)
# sort_button.place(x=250, y=150)


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
messagebox.showinfo("Sorted list", myList)
root.mainloop()