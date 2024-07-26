from tkinter import messagebox, simpledialog

from pyperclip import copy

from random import choice


class ED:
    """A class for encrypting and decrypting"""

    def is_even(self, num: int) -> bool:
        """Return true if num is even; false if not."""
        return num % 2 == 0

    def get_task(self) -> (bool| None):
        """Get the task."""
        task = messagebox.askyesnocancel('E or D?', "'Yes' for Encrypt, 'No' for Decrypt and 'Cancel' for cancel.")
        return task
    
    def get_even_letters(self, message: str) -> list:
        """Return the even indexed letters from message."""
        # Make a list for the even letters:
        even_letters = []
        # Start the loop for list ammendment:
        for c in range(0, len(message)):
            if self.is_even(c):
                even_letters.append(message[c])
        # Return final version of the list
        return even_letters

    def get_odd_letters(self, message: str) -> list:
        """Return the odd indexed letters from message."""
        # Make a list for the even letters:
        odd_letters = []
        # Start the loop for list ammendment:
        for c in range(0, len(message)):
            if not self.is_even(c):
                odd_letters.append(message[c])
        # Return final version of the list
        return odd_letters

    def encrypt(self, plaintext: str) -> str:
        """"Encrypts"""
        # Variables:
        plaintext = self._swap_letters(plaintext)
        fake_letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
        ciphertext = ''
        # Loop for adding the fake letters:
        for i in range(0, len(plaintext)):
            ciphertext += plaintext[i]
            ciphertext += choice(fake_letters)
	    # Return the ciphertext
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """"Decrypts"""
        # Conversion:
        plaintext = ''.join(self.get_even_letters(ciphertext))
        plaintext = self._swap_letters(plaintext)
        # Return the plaintext
        return plaintext

    def _swap_letters(self, mes: str) -> str:
        """Swaps the letters of the message."""
        even = None
        # Make the char list:
        letter_list = []
        # Add an extra 'x' if the length of plaintext is not divisible by 2:
        if not self.is_even(len(mes)):
            even = False
            mes = mes + 'x'
        # Make the lists:
        even_let = self.get_even_letters(mes)
        odd_let = self.get_odd_letters(mes)
        # For loop for char list ammemdment:
        for c in range(0, int(len(mes) / 2)):
            letter_list.append(odd_let[c])
            letter_list.append(even_let[c])
        # Create a str for the cipher/plaintext:
        new_mes = ''.join(letter_list)
        new_mes = self._remove_x(even, new_mes)
        # Return the str:
        return new_mes

    def _remove_x(self, is_even: bool, mes: str) -> str:
        """Remove the 'x' if is_even is false."""
        # Variable
        new_mes = ''
        if is_even is False:
	        # Variables:
            d = list(mes)
            j = 0
	        # Loop for removing x
            for i in d:
                j += 1
                if not j == len(d)-1:
                    new_mes += i
        else:
            new_mes = mes
	    # Return the new message
        return new_mes
    
if __name__ == "__main__":
    print(ED().encrypt('lazypanda@345'))