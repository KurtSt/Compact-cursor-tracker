import pygetwindow as gw
from pynput import mouse
import tkinter as tk

def on_move(x, y):
    if show_coordinates:
        active_window = gw.getActiveWindow()
        window_x, window_y, window_width, window_height = (
            active_window.topleft[0], 
            active_window.topleft[1], 
            active_window.width, 
            active_window.height
        )
        relative_x, relative_y = x - window_x, y - window_y
        coords_label.config(
            text=f"Screen: ({x}, {y}) - Window: ({relative_x}, {relative_y})"
        )
        root.update_idletasks()

def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass

def toggle_coordinates():
    global show_coordinates
    show_coordinates = not show_coordinates
    if show_coordinates:
        coords_label.pack()
    else:
        coords_label.pack_forget()

def close_application():
    root.destroy()

root = tk.Tk()
root.attributes("-topmost", True)
root.geometry("300x30")
root.configure(bg="white")

show_coordinates = True

coords_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
coords_label.pack()


with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    root.mainloop()
