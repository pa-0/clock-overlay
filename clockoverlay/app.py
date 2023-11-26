import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font


class App():
    def __init__(self) -> None:
        self._app = self._get_app()
        self._clock = self._get_clock()
        self._reset_position()
        self._draw_time()
        return None

    def _get_app(self) -> tk.Tk:
        app = tk.Tk()
        app.rowconfigure(index=0, weight=1)
        app.columnconfigure(index=0, weight=1)
        app.overrideredirect(True)
        app.wm_attributes("-topmost", True)
        app.wm_attributes("-alpha", 0.9)
        return app

    def _get_clock(self) -> ttk.Label:
        font = Font(family="courier 10 pitch", size=11)
        clock = ttk.Label(master=self._app, anchor="center", font=font)
        style = ttk.Style(master=clock.master)
        style.configure("TLabel", foreground="#00FF00", background="black")
        clock.grid(row=0, column=0, sticky="nsew")
        clock.bind("<ButtonRelease-3>", self._reset_position)
        clock.bind("<B1-Motion>", self._move_position)
        clock.bind("<ButtonRelease-2>", self._close)
        return clock

    def _reset_position(self, event: tk.Event | None = None) -> None:
        x, y = self._app.winfo_screenwidth()-56, 5
        self._app.geometry(f"+{x}+{y}")
        return None

    def _move_position(self, event: tk.Event) -> None:
        x, y = self._app.winfo_x() + event.x, self._app.winfo_y() + event.y
        self._app.geometry(f"+{x}+{y}")
        return None

    def _close(self, event: tk.Event | None = None) -> None:
        sys.exit()

    def _draw_time(self) -> None:
        self._clock.configure(text=time.strftime("%H:%M"))
        self._clock.after(1_000, self._draw_time)
        return None

    def mainloop(self) -> None:
        self._app.mainloop()
        return None
