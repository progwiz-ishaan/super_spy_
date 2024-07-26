from tkinter import *
import customtkinter as ctk
from tkinter import messagebox, Tk
from ed import ED
from cc import CC
from sit import SIT
from pet import start

class Window(ctk.CTk):
    """A class to represent the main window."""

    def __init__(self) -> None:
        super().__init__()
        # Set class vars:
        self.FONT = 'Segoe Script'
        self.BTN_FONT = (self.FONT, 15)
        self.FONT_COL1 = 'black'
        self.FONT_COL2 = 'orange'
        self.NAME = 'Ishaan'
        # Set window settings:
        self.configure(bg=self.FONT_COL1)
        self.geometry('400x400')
        self.ed = ED()
        # Set the labels:
        self._set_lbls()
        # Set the buttons:
        self._set_btns()
        # Call the starting screen:
        self.set_home_screen()

    def _set_lbls(self):
        """Set the labels."""
        # Set main title:
        self.title_lbl = ctk.CTkLabel(self, text='Super Spy', fg_color=self.FONT_COL2, bg_color=self.FONT_COL1, font=(self.FONT, 35))
        # Set password label:
        self.password_lbl = ctk.CTkLabel(self, text='Password:', bg_color=self.FONT_COL1, fg_color=self.FONT_COL2, font=(self.FONT, \
                                                                                                      25))
        # Set password entry:
        self.password_entry = ctk.CTkEntry(self, bg_color=self.FONT_COL2, fg_color=self.FONT_COL2)
        # Set welcome title:
        self.welcome_lbl = ctk.CTkLabel(self, text=f'Welcome, Master {self.NAME}!', font=(self.FONT, 25), bg_color=self.\
                                 FONT_COL1,fg_color=self.FONT_COL2)

    def _set_btns(self):
        """Set the buttons."""
        # Set enter button:
        self.enter_btn = Button(self, text='Enter', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT, command\
	        =self.check_password)
        # Set ed button:
        self.ed_btn = Button(self, text='Encode/Decode', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT, \
                             command=self.ed.encrypt_decrypt)
        # Set cc button:
        self.cc_btn = Button(self, text='Countdown Calander', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT,\
                             command=self.show_cc_screen)
        # Set exit button:
        self.exit_btn = Button(self, text='Exit', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT, \
                               command=self.exit)
        # Set login button:
        self.login_btn = Button(self, text='Login', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT, \
                                command=self.set_login_screen)
        # Set ist button:
        self.sit_btn = Button(self, text='Sacred/Impotant Texts', bg=self.FONT_COL2, fg=self.FONT_COL1,\
                              font=self.BTN_FONT, command=self.show_sit_screen)
        # Set pet button:
        self.pet_btn = Button(self, text='Launch Pet', bg=self.FONT_COL2, fg=self.FONT_COL1, font=self.BTN_FONT\
	                          , command=start)
    
    def set_home_screen(self):
        """Sets The Main Screen"""
        # Set window title:
        self.wm_title('SS')
        # Display main title:
        self.title_lbl.pack(fill=X, expand=True)
        # Display login button:
        self.login_btn.pack(ipadx=40, ipady=5, pady=100, expand=True)
        # Hide unesessery widgets:
        self.password_lbl.pack_forget()
        self.password_entry.pack_forget()
        self.enter_btn.pack_forget()
        self.welcome_lbl.pack_forget()
        
    def set_login_screen(self):
        """Sets the login screen."""
        # Set window title:
        self.wm_title('SS - Enter Password')
        # Display password label:
        self.password_lbl.pack(expand=True, fill=X)
        # Display password entry:
        self.password_entry.pack(expand=True, ipadx=0, ipady=0, pady=0)
        # Display password button:
        self.enter_btn.pack(ipadx=40, ipady=5, pady=100, expand=True)
        # Hide unnesessry widgets:
        self.login_btn.pack_forget()
        self.title_lbl.pack_forget()

    def set_loged_in_screen(self):
        """Sets the loged in screen."""
        # Set window title:
        self.wm_title('SS - Welcome!')
        # Maximize the window (Because of space problems):
        self.state('zoomed')
        # Display welcome title:
        self.welcome_lbl.pack(anchor='n', pady=10, fill=X, expand=True)
        # Display ed button:
        self.ed_btn.pack(ipadx=40, ipady=5, expand=True)
        # Display cc button:
        self.cc_btn.pack(ipadx=40, ipady=5, pady=25, expand=True)
        # Display ist button:
        self.sit_btn.pack(ipadx=40, ipady=5, pady=25, expand=True)
        # Display pet button:
        self.pet_btn.pack(ipadx=40, ipady=5, pady=25, expand=True)
        # Display exit button:
        self.exit_btn.pack(ipadx=40, ipady=5, pady=25, expand=True)
        # Hide unnessary widgets:
        self.password_lbl.pack_forget()
        self.password_entry.pack_forget()
        self.enter_btn.pack_forget()

    def check_password(self):
        """Checks the password and acts accorndily."""
        if self.password_entry.get().lower().replace(' ', '') == self.ed.decrypt('uxftnannmnydmkev@jem2i1g3l'):
            self.set_loged_in_screen()
        else:
            messagebox.showinfo('Idiot!', 'Haha! Good luck trying to hack into this application!')
            self.destroy()

    def show_cc_screen(self):
        """Show the cc screen."""
        self.cc = CC(self.FONT_COL1, self.FONT_COL2, self.FONT)

    def show_sit_screen(self):
        """Show the SIT screen."""
        self.sit = SIT(self.FONT_COL1, self.FONT_COL2, self.FONT)

    def exit(self):
        """Exit the application."""
        messagebox.showinfo('Bye!', f'Have a good day, Master {self.NAME}!')
        try:
            self.cc.destroy()
        except:
            pass
        try:
            self.sit.destroy()
        except:
            pass
        self.destroy()


class Packer():
    """The class that handles the layout"""


if __name__ == '__main__':
    # Excecute:
    root = Window()
    root.mainloop()
