#init
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

#diceroll function to implement randomization a little neater
def diceroll(numdice, numsides):
	total = 0
	for r in range(0,numdice):
		total = total + random.randint(1,numsides)
	print('Dice result: ' + str(total))
	return total

#random color function
class rColor():
	def hair():
		second = diceroll(1,6)
		if second == 1:
			color = 'blonde'
		elif second == 2:
			color = 'auburn'
		elif second == 3:
			color = 'brown'
		elif second == 4:
			color = 'black'
		elif second == 5:
			color = 'gray'
		else:
			color = 'white'
		return color
	
	def rainbow():
		second = diceroll(1,11)
		if second == 1:
			color = 'red'
		elif second == 2:
			color = 'orange'
		elif second == 3:
			color = 'yellow'
		elif second == 4:
			color = 'green'
		elif second == 5:
			color = 'blue'
		elif second == 6:
			color = 'purple'
		elif second == 7:
			color = 'pink'
		elif second == 8:
			color = 'brown'
		elif second == 9:
			color = 'black'
		elif second == 10:
			color = 'gray'
		else:
			color = 'white'
		return color

class rUndies():
	def panties():
		init = diceroll(1,5)
		if init == 1:
			p = rColor.rainbow()
		elif init == 2:
			p = 'striped'
		elif init == 3:
			p = 'animal print'
		elif init == 4:
			p = 'disney princess'
		else:
			p = 'magical girl'
		return p + ' panties'

	def diaper():
		init = diceroll(1,5)
		if init == 1:
			d = 'pair of thick training panties'
		elif init == 2:
			d = 'pullup'
		elif init == 3:
			d = 'stark white medical looking incontinence diaper'
		elif init == 4:
			d = 'baby diaper'
		else:
			d = 'cutesy ABDL diaper'
		return d

def rSpecies():
	init = diceroll(1,4)
	if init == 1:
		s = 'canine'
	elif init == 2:
		s = 'feline'
	elif init == 3:
		s = 'equine'
	else:
		s = 'dragon'
	return s

#this is the main meat of the program
def clicked():
	result = ''
	init = diceroll(3,20)
#===============================================================================================================#Animal Transformation
	if init in [14,15,30,31,32,33,48,49]:
		second = diceroll(1,20)
#---------------------------------------------------------------------------------------------------------------#Fur color
		if second in [1,5,9,11,15,19]:
			third = diceroll(1,10)
			if third in [1,2,3,5,7,8,9]:
				color = rColor.hair()
			else:
				color = rColor.rainbow()
			result = 'All your hair and/or fur is died ' + color + '.'
#---------------------------------------------------------------------------------------------------------------#Skin color
		elif second in [2,4,6,8,10]:
			result = 'Your skin color changes, becoming '
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
#---------------------------------------------------------------------------------------------------------------#Furry features
		elif second in [14,16,18,20]:
			third = diceroll(1,20)
			if third in [1,8,14,18,20]:		#Dog
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a dog tail or replace tail with dog tail.'
				elif fourth in [2,6,9]:
					result = 'Grow dog ears or replace other animal ears with dog ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with doggy paws.'
				else:
					result = 'Your face changes to become like a dog snout.'
					
			elif third in [2,9,15,19]:		#Cat
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a cat tail or replace tail with cat tail.'
				elif fourth in [2,6,9]:
					result = 'Grow cat ears or replace other animal ears with cat ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with cat claws.'
				else:
					result = 'Your face changes to become like a cat, growing whiskers and such.'
					
			elif third in [3,10,16]:		#Horse
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a horse tail or replace tail with horse tail.'
				elif fourth in [2,6,9]:
					result = 'Grow horse ears or replace other animal ears with horse ears.'
				elif fourth in [3,7]:
					result = 'Your feet grow into cloven hooves, also growing fur up to the waist.'
				else:
					result = 'Your face changes to becomes like a horse.'
					
			elif third in [4,11,17]:		#Bunny
				fourth = diceroll(1,2)
				if fourth == 1:
					result = 'Grow a bunny tail or replace tail with bunny tail.'
				else:
					result = 'Grow bunny ears or replace other animal ears with bunny ears.'
					
			elif third in [5,12]:			#Teeth
				result = 'Your teeth become sharp like a predator.'
				
			elif third in [6,13]:			#Fur
				fourth = diceroll(1,10)
				if fourth in [1,2,3,5,7,8,9]:
					color = rColor.hair()
				else:
					color = rColor.rainbow()
				result = 'Your body grows ' + color + ' colored fur all over.'
				
			else:							#Cow udders
				result = 'Grow cow udders under your navel.'
#---------------------------------------------------------------------------------------------------------------#Scaley features
		elif second in [3,7,17]:
			color = rColor.rainbow()
			third = diceroll(1,20)
			if third in [1,8,15,20]:
				result = 'Grow a dragon tail or replace tail with dragon tail. The scales are ' + color + ' colored.'
			elif third in [2,9,16]:
				result = 'Grow a pair of horns on your head.'
			elif third in [3,10,17]:
				result = 'Sprout demon/dragon wings from your back.'
			elif third in [4,11,18]:
				result = 'Replace current hands with lizard/dragon claws.'
			elif third in [5,12,19]:
				result = 'Your face changes to becomes like a lizard/dragon.'
			elif third in [6,13]:
				result = 'Grow a pattern of ' + color + ' colored lizard/dragon scales all across your body. Doesn\'t necessarily have to replace any fur.'
			else:
				result = 'Reptilian hair loss. Either body fur or the hair on your head falls out.'
#---------------------------------------------------------------------------------------------------------------#Slime
		elif second in [12,13]:
			color = rColor.rainbow()
			third = diceroll(1,7)
			if third in [1,5]:
				result = 'Your apendages become slimified, transforming into a ' + color + ' goo-like substance.'
			elif third in [2,6]:
				result = 'Your torso becomes slimified, transforming into a ' + color + ' goo-like substance.'
			elif third in [3,7]:
				result = 'Your head becomes slimified, transforming into a ' + color + ' goo-like substance.'
			else:
				result = 'Your entire body becomes slimified, transforming into a ' + color + ' goo-like substance.'
#===============================================================================================================#Diapers and incontinence
	elif init in [12,13,28,29,34,35,50,51]:
		second = diceroll(1,20)
		if second in [1,11]:
			result = 'Your bladder becomes full.'
		elif second in [2,12]:
			result = 'Your bowels become full.'
		elif second in [3,13]:
			result = 'Your bladder gets permanently weaker.'
		elif second in [4,14]:
			result = 'Your bowels and sphincter muscles get permanently weaker.'
		elif second in [5,15]:
			result = 'You become afraid of using the toilet.'
		elif second in [6,16]:
			result = 'Replace whatever underwear or diaper you currently have with a pair of ' + rUndies.panties() + '.'
		elif second in [7,17]:
			result = 'Layer on a pair of ' + rUndies.panties() + ' over whatever other underwear or diaper you\'ve got on.'
		elif second in [8,18]:
			result = 'Replace whatever underwear or diaper you currently have with a ' + rUndies.diaper() + '.'
		elif second in [9,19]:
			result = 'Layer on a ' + rUndies.diaper() + ' over whatever other underwear or diaper you\'ve got on.'
		else:
			third = diceroll(1,6)
			if third == 1:
				time = 'for 1 hour'
			elif third == 2:
				time = 'for the next 3 hours.'
			elif third == 3:
				time = 'for the next 6 hours.'
			elif third == 4:
				time = 'for the next 12 hours.'
			elif third == 5:
				time = 'for the next 24 hours.'
			else:
				time = 'until it has been used at least 4 times.'
			result = 'You are locked in a ' + rUndies.diaper() + ' ' + time + ' If you\'re already wearing a diaper just use that one.'
#===============================================================================================================#Gender and genitalia
	elif init in [10,11,26,27,36,37,52,53]:
		second = diceroll(1,20)
		if seceond in [1,5,9,13,17]:
			third = diceroll(1,13)
			if third in [1,6,11]:
			elif third in [2,7,12]:
			elif third in [3,8,13]:
			elif third in [4,9]:
			else:
		elif second in [2,6,10,14,18]:
			
		elif second in [3,7,11,15,19]:
			
		else:
			
#===============================================================================================================#Mind altering
	elif init in [8,9,24,25,38,39,54,55]:
		result = 'mind'
	
#===============================================================================================================#Physical age
	elif init in [6,7,22,23,40,41,56,57]:
		result = 'age'
	
#===============================================================================================================#Pregnancy related
	elif init in [4,5,20,21,42,43,58,59]:
		result = 'preg'
	
#===============================================================================================================#Bondage
	elif init in [18,19,44,45]:
		result = 'bonds'
	
#===============================================================================================================#Rare
	else:
		result = 'other'

	#display the result as a message box
	messagebox.showinfo('Transformation Result', result)

#the button itself
btn = tk.Button(frame1, text="Transform Me!", command=clicked)
btn.pack(pady=20)
btn.focus()

window.mainloop()

		elif second == 3:
			color = 'yellow'
		elif second == 4:
			color = 'green'
		elif second == 5:
			color = 'blue'
		elif second == 6:
			color = 'purple'
		elif second == 7:
			color = 'pink'
		elif second == 8:
			color = 'brown'
		elif second == 9:
			color = 'black'
		elif second == 10:
			color = 'gray'
		else:
			color = 'white'
		return color

#this is the main meat of the program
def clicked():
	result = ''
	init = diceroll(3,20)
#===============================================================================================================#Animal Transformation
	if init in [14,15,30,31,32,33,48,49]:
		second = diceroll(1,20)
#---------------------------------------------------------------------------------------------------------------#Fur color
		if second in [1,5,9,11,15,19]:
			third = diceroll(1,10)
			if third in [1,2,3,5,7,8,9]:
				color = randomcolor.hair()
			else:
				color = randomcolor.rainbow()
			result = 'All your hair and/or fur is died ' + color + '.'
#---------------------------------------------------------------------------------------------------------------#Skin color
		elif second in [2,4,6,8,10]:
			result = 'Your skin color changes, becoming '
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
#---------------------------------------------------------------------------------------------------------------#Furry features
		elif second in [14,16,18,20]:
			third = diceroll(1,20)
			if third in [1,8,14,18,20]:		#Dog
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a dog tail or replace tail with dog tail.'
				elif fourth in [2,6,9]:
					result = 'Grow dog ears or replace other animal ears with dog ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with doggy paws.'
				else:
					result = 'Your face changes to become like a dog snout.'
					
			elif third in [2,9,15,19]:		#Cat
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a cat tail or replace tail with cat tail.'
				elif fourth in [2,6,9]:
					result = 'Grow cat ears or replace other animal ears with cat ears.'
				elif fourth in [3,7]:
					result = 'Replace current hands with cat claws.'
				else:
					result = 'Your face changes to become like a cat, growing whiskers and such.'
					
			elif third in [3,10,16]:		#Horse
				fourth = diceroll(1,9)
				if fourth in [1,5,8]:
					result = 'Grow a horse tail or replace tail with horse tail.'
				elif fourth in [2,6,9]:
					result = 'Grow horse ears or replace other animal ears with horse ears.'
				elif fourth in [3,7]:
					result = 'Your feet grow into cloven hooves, also growing fur up to the waist.'
				else:
					result = 'Your face changes to becomes like a horse.'
					
			elif third in [4,11,17]:		#Bunny
				fourth = diceroll(1,2)
				if fourth == 1:
					result = 'Grow a bunny tail or replace tail with bunny tail.'
				else:
					result = 'Grow bunny ears or replace other animal ears with bunny ears.'
					
			elif third in [5,12]:			#Teeth
				result = 'Your teeth become sharp like a predator.'
				
			elif third in [6,13]:			#Fur
				fourth = diceroll(1,10)
				if fourth in [1,2,3,5,7,8,9]:
					color = randomcolor.hair()
				else:
					color = randomcolor.rainbow()
				result = 'Your body grows ' + color + ' colored fur all over.'
				
			else:							#Cow udders
				result = 'Grow cow udders under your navel.'
#---------------------------------------------------------------------------------------------------------------#Scaley features
		elif second in [3,7,17]:
			color = randomcolor.rainbow()
			third = diceroll(1,20)
			if third in [1,8,15,20]:
				result = 'Grow a dragon tail or replace tail with dragon tail. The scales are ' + color + ' colored.'
			elif third in [2,9,16]:
				result = 'Grow a pair of horns on your head.'
			elif third in [3,10,17]:
				result = 'Sprout demon/dragon wings from your back.'
			elif third in [4,11,18]:
				result = 'Replace current hands with lizard/dragon claws.'
			elif third in [5,12,19]:
				result = 'Your face changes to becomes like a lizard/dragon.'
			elif third in [6,13]:
				result = 'Grow a pattern of ' + color + ' colored lizard/dragon scales all across your body. Doesn\'t necessarily have to replace any fur.'
			else:
				result = 'Reptilian hair loss. Either body fur or the hair on your head falls out.'
#---------------------------------------------------------------------------------------------------------------#Slime
		elif second in [12,13]:
			color = randomcolor.rainbow()
			third = diceroll(1,7)
			if third in [1,5]:
				'Your apendages become slimified, transforming into a ' + color + ' goo-like substance.'
			elif third in [2,6]:
				'Your torso becomes slimified, transforming into a ' + color + ' goo-like substance.'
			elif third in [3,7]:
				'Your head becomes slimified, transforming into a ' + color + ' goo-like substance.'
			else:
				'Your entire body becomes slimified, transforming into a ' + color + ' goo-like substance.'
#===============================================================================================================#Diapers and incontinence
	elif init in [12,13,28,29,34,35,50,51]:
		result = 'diaper'
	
#===============================================================================================================#Gender and genitalia
	elif init in [10,11,26,27,36,37,52,53]:
		result = 'genitalia'
	
#===============================================================================================================#Mind altering
	elif init in [8,9,24,25,38,39,54,55]:
		result = 'mind'
	
#===============================================================================================================#Physical age
	elif init in [6,7,22,23,40,41,56,57]:
		result = 'age'
	
#===============================================================================================================#Pregnancy related
	elif init in [4,5,20,21,42,43,58,59]:
		result = 'preg'
	
#===============================================================================================================#Bondage
	elif init in [18,19,44,45]:
		result = 'bonds'
	
#===============================================================================================================#Rare
	else:
		result = 'other'

	#display the result as a message box
	messagebox.showinfo('Transformation Result', result)

#the button itself
btn = tk.Button(frame1, text="Transform Me!", command=clicked)
btn.pack(pady=20)
btn.focus()

window.mainloop()
