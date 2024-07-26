import customtkinter as ctk
import tkinter as tk
import PIL.Image
from ed import ED
from home import Home

class Main(ctk.CTk):

    FONT = 'Gabriola'
    FONT_COL1 = ('white', 'black')
    FONT_COL2 = ('#222e50', 'orange')
    NAME = 'Ishaan'
    mode = False

    def __init__(self):
        """The main window."""
        # Setup:
        super().__init__(fg_color=self.FONT_COL1)
        self.title('Super spy')
        # self.iconbitmap('h.ico')
        self.home = Home
        self.configure(bg=self.FONT_COL1)
        self.geometry('400x400')

        # Login screen:
        self._login_srn_widgets()
        self._login_place()
        self.pas_var.trace('w', self.check_password)
        
        # ctk.set_appearance_mode('light')
        self.mainloop()

    def _login_srn_widgets(self):
        """"Create the login screen widgets"""
        self.title_lbl = ctk.CTkLabel(self, text='Super Spy', font=(self.FONT, 50), text_color=self.FONT_COL2)

        self.pas_lbl = ctk.CTkLabel(self, text='Enter password', font=(self.FONT, 30), text_color=self.FONT_COL2)

        self.pas_var = tk.StringVar()
        self.pas_ent = ctk.CTkEntry(self, fg_color=self.FONT_COL2, corner_radius=10, border_color=self.FONT_COL1, 
                                    width=200, text_color=self.FONT_COL2, font=(self.FONT, 9), textvariable=self.pas_var)
        
        self.sub_pas = ctk.CTkButton(self, fg_color=self.FONT_COL2, text_color=self.FONT_COL1, corner_radius=10, 
                                     text='Login', width=80, font=(self.FONT, 15), hover_color=('#212d40', '#c68400'), height=20)
        
        self.light_dark = ctk.CTkButton(self, 0, 10, 15, 0, fg_color=self.FONT_COL1, text='', command=self.light_dark,
                                         image=ctk.CTkImage(PIL.Image.open('dark_mode.png'),
                                                             PIL.Image.open('light_mode.png')),
                                        hover_color=self.FONT_COL1)
        
    def _login_place(self):
        """Place the login screen widgets."""
        self.title_lbl.place(relx=0.5, rely=0, anchor='n')
        self.pas_lbl.place(relx=0.5, rely=0.25, anchor='n')
        self.pas_ent.place(relx=0.5, rely=0.4, anchor='n')
        self.sub_pas.place(relx=0.5, rely=0.5, anchor='n')
        self.light_dark.place(relx=0.01, rely=0.99, anchor='sw')
    
    def light_dark(self):
        """Switch between the light and dark modes."""
        if self.mode:
            ctk.set_appearance_mode('dark')
            self.mode = False
        else:
            ctk.set_appearance_mode('light')
            self.mode = True

    def check_password(self, *args):
        """Check if the password is correct."""
        if self.pas_var.get() == ED().decrypt("aslhyzzdahpidcnp@cav4w3u5v"):
            self.home.__init__(self.home, self.FONT_COL1, self.FONT_COL2, self.FONT)


if __name__ == '__main__':
    Main()