import pygetwindow as gw
import pyautogui
from pynput import mouse
import tkinter as tk

def on_move(x, y):
    active_window = gw.getActiveWindow()
    window_x, window_y, window_width, window_height = active_window.topleft[0], active_window.topleft[1], active_window.width, active_window.height
    relative_x, relative_y = x - window_x, y - window_y
    coords_label.config(text=f"Screen coordinates: ({x}, {y}) - Window coordinates: ({relative_x}, {relative_y})")
    root.update_idletasks()

def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass

root = tk.Tk()
root.attributes("-topmost", True)  # Keeps the overlay window on top
root.geometry("350x20")
root.configure(bg="white")
root.overrideredirect(1)  # Removes title bar and border

coords_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
coords_label.pack()

with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    root.mainloop()
