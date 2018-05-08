import io
import tkinter as tk
from .dictionary import T2SDictionary


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self._t2s_dictionary = T2SDictionary()

        self._text_left = None
        self._btn_translate = None
        self._text_right = None

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self._text_left = tk.Text(self)
        self._text_left.pack(side='left')

        self._btn_translate = tk.Button(self)
        self._btn_translate['text'] = 'Translate'
        self._btn_translate['command'] = self._t2s
        self._btn_translate.pack(side='left')

        self._text_right = tk.Text(self)
        self._text_right.pack(side='left')

    def _t2s(self):
        tranditional_text = self._text_left.get(1., tk.END)
        simplified_text = io.StringIO()

        for t_char in tranditional_text:
            try:
                simplified_text.write(self._t2s_dictionary.lookup(t_char))
            except ValueError:
                simplified_text.write(t_char)
                continue

        self._text_right.delete(1., tk.END)
        self._text_right.insert(tk.END, simplified_text.getvalue())


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
