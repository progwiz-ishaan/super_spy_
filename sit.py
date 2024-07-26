from tkinter import *
from tkinter import simpledialog, messagebox
from ed import ED as e

class SIT(Tk):
    """A class to represent the sit window."""

    def __init__(self, fc1, fc2, f):
        super().__init__()
	# Set class vars:
        self.FONT = f
        self.FONT_COL1 = fc1
        self.FONT_COL2 = fc2
        self.file = ""
        self.encode_decode = e()
        # Set window settings:
        self.geometry('800x800')
        self.title('SS - S/I Texts')
        self.configure(bg=self.FONT_COL1)
        # Set the file:
        self._set_file_name()
        # Set editing text area:
        self.editing_ta = Text(self, height=30, width=67, bg=self.FONT_COL2, fg=self.FONT_COL1, \
                               font=(self.FONT, 10))
        self.editing_ta.pack()
        self.editing_ta.insert(END, self.get_file_text())
        # Set save button:
        self.save_btn = Button(self, text='Save', fg=self.FONT_COL1, bg=self.FONT_COL2, font=(self.FONT, 15),\
                               command=self.save)
        self.save_btn.pack(ipadx=40, ipady=5, pady=5)

    def get_file_text(self) -> str:
        """Get the text from sit.txt and decrypt it finally return it."""
        with open(self.file, 'r') as f:
            text = self.encode_decode.decrypt(f.read())
        return text

    def save(self):
        """Encrypt the text in self.editing_ta and save it to sit.txt."""
        with open(self.file, 'w') as f:
            text_to_add = self.encode_decode.encrypt(self.editing_ta.get('1.0', END))
            f.write(text_to_add)

    def _set_file_name(self):
        """Clarify the file name."""
        create_new_file = messagebox.askyesno('Create new file', 'Do you want to create a new file?')
        name_of_file = 'Txt_files\ '.replace(' ', '') + simpledialog.askstring('Name', 'Enter the name of file to create/open:').lower() + '.txt'
        if create_new_file is True:
            f = open(name_of_file, 'x')
            f.close()
        self.file = name_of_file



if __name__ == '__main__':
    s = SIT('black', 'orange', 'Segoe Script')
    s.mainloop()
