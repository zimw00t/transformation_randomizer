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
			return
		elif second in [14,16,18,20]:
			return
		elif second in [3,7,17]:
			return
		elif second in [12,13]:
			return
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
