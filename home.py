import tkinter as tk
import customtkinter as ck

class Home(ck.CTk):

    def __init__(self, f1:str, f2:str, f3:str):
        super().__init__(fg_color=f1)
        # Setup:
        self.title('Super spy - Home')
        self.geometry('800x600+250+50')
        self.configure(bg=self.FONT_COL1)
        self.FONT_COL1 = f1
        self.FONT_COL2 = f2
        self.FONT = f3

        # Widgets:
        self._create_wdgs()
        self._grid_wdgs()

        self.mainloop()

    def _create_wdgs(self):
        """Create the widgets."""
        self.title_lbl = ck.CTkLabel(self, text='Super Spy', font=(self.FONT, 50), text_color=self.FONT_COL2)

    def _grid_wdgs(self):
        """Grid the widgets."""
        # Configure the rows and columns:
        self.columnconfigure((0, 2), weight=1, uniform='a')
        self.columnconfigure(1, weight=5, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=5, uniform='a')

        # Grid the widgets:
        self.title_lbl.grid(row=0, column=1, sticky='n')


if __name__ == "__main__":
    Home()