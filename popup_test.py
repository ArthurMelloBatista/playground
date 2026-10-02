import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CAIXA DE MENSAGEM")

tk.Label(root, text="TEST").pack(padx=24, pady=(20, 12))

buttons = tk.Frame(root)
buttons.pack(padx=16, pady=(0, 16))

tk.Button(buttons, text="Close", command=root.destroy, activebackground="red").pack(side=tk.LEFT, padx=4)
tk.Button(buttons, text="Keep running").pack(side=tk.LEFT, padx=4)
tk.Button(buttons, text="If you are curious, click me", command=lambda: messagebox.showinfo("Mensagem", "Stop clicking me!")).pack(side=tk.LEFT, padx=4)

root.mainloop()