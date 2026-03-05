import tkinter as tk 

color_black = "#000000"
color_white = "white"

def mode_change(mode):
    if mode == "jour":
        window.config(bg=color_white)
        label.config(bg=color_white, fg=color_black)
    else :
        window.config(bg=color_black)
        label.config(bg=color_black, fg=color_white)

# WINDOW CREATION
window = tk.Tk()
window.title("Exo")
window.geometry("300x300")
window.resizable(False, False)
window.config(bg=color_white)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# LABEL
label=tk.Label(window, text="Test de texte", font=("Arial", 15, "bold"))
label.config(bg=color_white)
label.grid(row=0, column=0, columnspan=2, pady=20)

# BUTTONS
mode_jour = tk.Button(window, text="Mode Jour", font=("Arial", 10), command=lambda: mode_change("jour"))
mode_jour.grid(row=1, column=0, pady=60, padx=10)

mode_nuit = tk.Button(window, text="Mode Nuit", font=("Arial", 10), command=lambda: mode_change("nuit"))
mode_nuit.grid(row=1, column=1, pady=60, padx=10)

# CENTER WINDOW
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()