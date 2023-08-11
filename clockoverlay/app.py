import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font


class App():
    def __init__(self) -> None:
        self._app = self._get_app()
        self._root = self._get_root()
        self._clock = self._get_clock()
        self._draw_time()
        return None

    def _get_app(self) -> tk.Tk:
        app = tk.Tk()
        x, y = app.winfo_screenwidth()-50, 5
        app.geometry(f"+{x}+{y}")
        app.rowconfigure(index=0, weight=1)
        app.columnconfigure(index=0, weight=1)
        app.overrideredirect(True)
        app.wm_attributes("-topmost", True)
        app.bind_all("<ButtonRelease-2>", lambda e: sys.exit())
        return app

    def _get_root(self) -> ttk.Frame:
        root = ttk.Frame(master=self._app)
        root.grid(row=0, column=0, sticky="nsew")
        root.rowconfigure(index=0, weight=1)
        root.columnconfigure(index=0, weight=1)
        return root

    def _get_clock(self) -> ttk.Label:
        font = Font(family="Consolas", size=11)
        label = ttk.Label(master=self._root, anchor="center", font=font)
        label.grid(row=0, column=0, sticky="nsew")
        style = ttk.Style(master=label.master)
        style.configure("TLabel", foreground="#00FF00", background="black")
        return label

    def _draw_time(self) -> None:
        self._clock.configure(text=time.strftime("%H:%M"))
        self._clock.after(60_000, self._draw_time)

    def mainloop(self) -> None:
        self._app.mainloop()
        return None
