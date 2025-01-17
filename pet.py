from tkinter import HIDDEN, NORMAL, Tk, Canvas
import customtkinter as ct

root = ct.CTk()
root.withdraw()
root.title('Roxy Jr.')
c = ct.CTkCanvas(root, width=400, height=400)
c.configure(bg='black', highlightthickness=0)
c.body_colour = 'blue'
c.eyes_crossed = False
c.happy = 10
c.tongue_out = False

body = c.create_oval(35, 20, 365, 350, outline=c.body_colour, fill=c.body_colour)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_colour, fill=c.body_colour)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_colour, fill=c.body_colour)
foot_left = c.create_oval(65, 320,  145, 360, outline=c.body_colour, fill=c.body_colour)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_colour, fill=c.body_colour)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
left_pupil = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
right_pupil = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

def toggle_eyes():
	cc = c.itemcget(eye_left, 'fill')
	nc = c.body_colour if cc == 'white' else 'white'
	cs = c.itemcget(left_pupil, 'state')
	ns = NORMAL if cs == HIDDEN else HIDDEN
	c.itemconfigure(left_pupil, state=ns)
	c.itemconfigure(right_pupil, state=ns)
	c.itemconfigure(eye_left, fill=nc)
	c.itemconfigure(eye_right, fill=nc)
	
def blink():
	toggle_eyes()
	root.after(250, toggle_eyes)
	root.after(3000, blink)
	
def show_happy(event):
	if 20 <= event.x <= 350 and 20 <= event.y <= 350:
		c.itemconfigure(cheek_left, state=NORMAL)
		c.itemconfigure(cheek_right, state=NORMAL)
		c.itemconfigure(mouth_happy, state=NORMAL)
		c.itemconfigure(mouth_normal, state=HIDDEN)
		c.itemconfigure(mouth_sad, state=HIDDEN)
		c.happy = 10
		
	return


def hide_happy(event):
	c.itemconfigure(cheek_left, state=HIDDEN)
	c.itemconfigure(cheek_right, state=HIDDEN)
	c.itemconfigure(mouth_happy, state=HIDDEN)
	c.itemconfigure(mouth_normal, state=NORMAL)
	c.itemconfigure(mouth_sad, state=HIDDEN)

	return

def toggle_tongue():
	if not c.tongue_out:
		c.itemconfigure(tongue_tip, state=NORMAL)
		c.itemconfigure(tongue_main, state=NORMAL)
		c.tongue_out = True
	else:
		c.itemconfigure(tongue_tip, state=HIDDEN)
		c.itemconfigure(tongue_main, state=HIDDEN)
		c.tongue_out = False
		
def toggle_pupils():
	if not c.eyes_crossed:
		c.move(left_pupil, 10, -5)
		c.move(right_pupil, -10, -5)
		c.eyes_crossed = True
	else:
		c.move(left_pupil, -10, 5)
		c.move(right_pupil, 10, 5)
		c.eyes_crossed = False
		
def cheeky(event):
	toggle_tongue()
	toggle_pupils()
	hide_happy(event)
	root.after(1000, toggle_tongue)
	root.after(1000, toggle_pupils)
	return 

def sad():
	if c.happy == 0:
		c.itemconfigure(mouth_happy, state=HIDDEN)
		c.itemconfigure(mouth_sad, state=NORMAL)
		c.itemconfigure(mouth_normal, state=HIDDEN)
	else:
		c.happy -= 1
	root.after(5000, sad)

def start():
	root.deiconify()
	c.pack()
	c.bind('<Motion>', show_happy)
	c.bind('<Leave>', hide_happy)
	c.bind('<Double-1>', cheeky)
	root.after(1000, blink)
	root.after(5000, sad)
	root.mainloop()
	
def end():
	root.destroy()
	
if __name__ == '__main__':
	start()