from tkinter import ttk
import tkinter as tk



root = tk.Tk()
container = tk.Frame(root)
container.pack()
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

canvas.configure(yscrollcommand=scrollbar.set)


x=ttk.Label(scrollable_frame, text="Sample scrolling label")
x.pack()
but = tk.Button(scrollable_frame, text="cheese",background="orange")
but.pack()
canvas.pack(side="top", fill="both", expand=True)
scrollbar.pack(side="bottom", fill="x")

root.mainloop()