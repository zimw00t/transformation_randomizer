import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()

frame1 = tk.Frame(window)
frame1.pack(side = tk.BOTTOM)

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - 125
y = (hs/2) - 35

window.title("Randomizer")
window.geometry('%dx%d+%d+%d' % (250, 70, x, y))
window.resizable(width=False, height=False)

def diceroll(numdice, numsides):
	total = 0
	for r in range(0,numdice):
		total = total + random.randint(1,numsides)
	return total

def clicked():
	result = ''
	init = diceroll(3,20)
	if init in [14,15,30,31,32,33,48,49]:
		second = diceroll(1,20)
		if second in [1,5,9,11,15,19]:
			result += 'All your hair and/or fur is died '
			third = diceroll(1,10)
			if third in [1,2,3,5,7,8,9]:
				fourth = diceroll(1,6)
				if fourth == 1:
					result += 'blonde.'
				elif fourth == 2:
					result += 'auburn.'
				elif fourth == 3:
					result += 'brown.'
				elif fourth == 4:
					result += 'black.'
				elif fourth == 5:
					result += 'gray.'
				else:
					result += 'white.'
			else:
				fourth = diceroll(1,7)
				if fourth == 1:
					result += 'bright neon red.'
				elif fourth == 2:
					result += 'orange.'
				elif fourth == 3:
					result += 'bright neon yellow.'
				elif fourth == 4:
					result += 'green.'
				elif fourth == 5:
					result += 'blue.'
				elif fourth == 6:
					result += 'purple.'
				else:
					result += 'pink.'
		elif second in [2,4,6,8,10]:
			result += 'Your skin color changes, becoming '
			third = diceroll(1,10)
			if third in [1,2,3,5,7,8,9]:
				fourth = diceroll(1,5)
				if fourth == 1:
					result += 'white.'
				elif fourth == 2:
					result += 'tanned.'
				elif fourth == 3:
					result += 'olive.'
				elif fourth == 4:
					result += 'brown.'
				else:
					result += 'ebony.'
			else:
				fourth = diceroll(1,9)
				if fourth in [1,5]:
					result += 'red.'
				elif fourth in [2,6]:
					result += 'green.'
				elif fourth == [3,7]:
					result += 'blue.'
				elif fourth in [4,8]:
					result += 'purple.'
				else:
					result += 'clown makeup.'
		elif second in [14,16,18,20]:
			third = diceroll(1,20)
			if third in [1,8,14,18,20]:
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a dog tail or replace tail with dog tail.'
				elif fourth in [2,6,9]:
					result = 'Grow dog ears or replace other animal ears with dog ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with doggy paws.'
				else:
					result = 'Your face changes to become like a dog snout.'
			elif third in [2,9,15,19]:
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a cat tail or replace tail with cat tail.'
				elif fourth in [2,6,9]:
					result = 'Grow cat ears or replace other animal ears with cat ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with cat claws.'
				else:
					result = 'Your face changes to become like a cat, growing whiskers and such.'
			elif third in [3,10,16]:
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a horse tail or replace tail with horse tail.'
				elif fourth in [2,6,9]:
					result = 'Grow horse ears or replace other animal ears with horse ears.'
				elif fourth in [3,7]:
					result = 'Your feet grow into cloven hooves, also growing fur up to the waist.'
				else:
					result = 'Your face changes to becomes like a horse.'
			elif third in [4,11,17]:
				fourth = diceroll(1,2)
				if fourth == 1:
					result = 'Grow a bunny tail or replace tail with bunny tail.'
				else:
					result = 'Grow bunny ears or replace other animal ears with bunny ears.'
			elif third in [5,12]:
				result = 'Your teeth become sharp like a predator.'
			elif third in [6,13]:
				fourth = diceroll(1,10)
				if fourth in [1,2,3,5,7,8,9]:
					fifth = diceroll(1,6)
					if fifth == 1:
						color = 'blonde.'
					elif fifth == 2:
						color = 'auburn.'
					elif fifth == 3:
						color = 'brown.'
					elif fifth == 4:
						color = 'black.'
					elif fifth == 5:
						color = 'gray.'
					else:
						color = 'white.'
				else:
					fifth = diceroll(1,7)
					if fifth == 1:
						color = 'bright neon red.'
					elif fifth == 2:
						color = 'orange.'
					elif fifth == 3:
						color = 'bright neon yellow.'
					elif fifth == 4:
						color = 'green.'
					elif fifth == 5:
						color = 'blue.'
					elif fifth == 6:
						color = 'purple.'
					else:
						color = 'pink.'
				result = 'Your body grows ' + color + ' colored fur all over.'
			else:
				result = 'Grow cow udders under your navel.'
		elif second in [3,7,17]:
			result = 'dragon'
		elif second in [12,13]:
			result = 'slime'
	elif init in [12,13,28,29,34,35,50,51]:
		return
	elif init in [10,11,26,27,36,37,52,53]:
		return
	elif init in [8,9,24,25,38,39,54,55]:
		return
	elif init in [6,7,22,23,40,41,56,57]:
		return
	elif init in [4,5,20,21,42,43,58,59]:
		return
	elif init in [18,19,44,45]:
		return
	else:
		return

	messagebox.showinfo('Transformation Result', result)

btn = tk.Button(frame1, text="Transform Me!", command=clicked)
btn.pack(pady=20)
btn.focus()

window.mainloop()
