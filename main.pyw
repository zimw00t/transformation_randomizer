#init
import tkinter as tk
from tkinter import messagebox
import random
import datetime

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
		seed = str(datetime.datetime.now())
		seed = seed.replace(':','')
		seed = seed.replace('-','')
		seed = seed.replace(' ','')
		print('Radomization seed: ' + seed)
		random.seed(int(seed))
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
	init = diceroll(1,5)
	if init == 1:
		s = 'human'
	elif init ==2:
		s = 'canine'
	elif init == 3:
		s = 'feline'
	elif init == 4:
		s = 'horse'
	else:
		s = 'dragon'
	return s

#this is the main meat of the program
def clicked():
	print('Button clicked!')
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
			third = diceroll(1,21)
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
				
			elif third in [6,13,21]:			#Fur
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
		second = diceroll(1,25)
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
		elif second in [8,18,21,24]:
			result = 'Replace whatever underwear or diaper you currently have with a ' + rUndies.diaper() + '.'
		elif second in [9,19,23,25]:
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
		if second in [1,5,9,13,17]:						#Dicks
			third = diceroll(1,13)
			if third in [1,6,11]:
				result = 'Your cock gets bigger. If you don\'t have one grow a ' + rSpecies() + ' one. If you have multiple just pick one.'
			elif third in [2,7,12]:
				result = 'Your cock gets smaller. If it\'s already small enough you can make it disappear completely instead. If you have mulitple just pick one.'
			elif third in [3,8,13]:
				result = 'Replace your cock with a ' + rSpecies() + ' cock. If you don\'t have any cocks grow one. If you have multiple just pick one.'
			elif third in [4,9]:
				result = 'Replace your cock with an ovipositor tentacle. If you don\'t have any cocks grow one. If you have multiple just pick one.'
			else:
				result = 'Grow a ' + rSpecies() + ' cock in addition to any you already have.'
		
		elif second in [2,6,10,14,18]:						#Bobs
			third = diceroll(1,13)
			if third in [1,6,11]:
				result = 'Your breasts get bigger. If you don\'t have any, grow a pair.'
			elif third in [2,7,12]:
				result = 'Your breasts get smaller, disappearing completely if they\'re already small enough.'
			elif third in [3,8,13]:
				result = 'Your nipples get bigger, longer, and more sensitive.'
			elif third in [4,9]:
				result = 'The tips of your nipples become fuckable.'
			else:
				result = 'Grow an addition row of breasts. If you have none grow a first row of breasts.'
		
		elif second in [3,7,11,15,19]:						#Vagoo
			third = diceroll(1,14)
			if third in [1,6,11]:
				result = 'Your vagina becomes more loose. If you don\'t have one grow one, and a womb to go with it.'
			elif third in [2,7,12]:
				result = 'Your vagina\'s capacity gets deeper, able to take larger insertions more easily. If you don\'t have one grow one, and a womb to go with it.'
			elif third in [3,8,13]:
				result = 'Your vagina gets tighter, or seals up entirely removing your womb with it.'
			elif third in [4,9,14]:
				result = 'Your genitals become more sensitive to pleasure.'
			else:
				result = 'If your vaginal virginity was taken already, your hymen is now restored. (Optionally it becomes self-regenerating so that it gets restored every time from now on.)'
		
		else:									#Ass
			third = diceroll(1,6)
			if third in [1,4]:
				result = 'Your ass hole becomes looser. This may affect continence.'
			elif third in [2,5]:
				result = 'Your ass hole becomes tighter.'
			else:
				result = 'The sensitivity of your ass hole increases, becoming more of a sexual organ.'
#===============================================================================================================#Mind altering
	elif init in [8,9,24,25,38,39,54,55]:
		second = diceroll(1,16)
		if second in [1,9]:
			result = 'You lose some of your maturity, becoming mentally younger.'
		elif second in [2,10]:
			result = 'You become more intelligent.'
		elif second in [3,11]:
			result = 'Your thoughts become more feminine.'
		elif second in [4,12]:
			result = 'Your thoughts become more masculine.'
		elif second in [5,13]:
			result = 'You feel yourself becoming more physically attracted to men.'
		elif second in [6,14]:
			result = 'You feel yourself becoming more physically attracted to women.'
		elif second in [7,15]:
			result = 'You feel yourself becoming more physically attracted to animals.'
		else:
			third = diceroll(1,5)
			if third == 1:
				trigger = 'incontinence.'
			elif third == 2:
				trigger = 'sexual pleasure.'
			elif third == 3:
				trigger = 'master-slave relationships.'
			elif third == 4:
				trigger = 'gender.'
			else:
				trigger = 'furry transformation.'
			result = 'You gain a new trigger word related to ' + trigger
#===============================================================================================================#Physical age
	elif init in [6,7,22,23,40,41,56,57]:
		second = diceroll(1,3)
		if second in [1,2]:
			result = 'You get ' + str(diceroll(1,5)) + ' year(s) younger. Can stop at whatever age minimum you want, or can lead to unbirth if you want.'
		else:
			result = 'You get ' + str(diceroll(1,2)) + ' year(s) older. Can stop at whatever age maximum you want.'
#===============================================================================================================#Pregnancy related
	elif init in [4,5,20,21,42,43,58,59]:
		second = diceroll(1,17)
		if second in [1,7,13]:
			result = 'Your chances to get pregnant or impregnante others increases dramatically.'
		elif second in [2,8,14]:
			result = 'You begin lactating, or increase your milk production if you already are.'
		elif second in [3,9,15]:
			result = 'Your sperm production increases, even if you don\'t have a penis (squirt sperm from vagina.)'
		elif second in [4,10,16]:
			result = 'If you\'re lactating your milk becomes addictive. If not any milk you drink from now on will be addictive to you.'
		elif second in [5,11,17]:
			result = 'You become pregnant, or if you already are your pregnancy is sped along to the next stage. If you have no vagina a pseudo-womb located in your butt is created for the duration of the pregnancy.'
		else:
			result = 'A tentacle appears from a magic portal and lays eggs inside your womb (or colon if you don\'t have a womb.) If you leave them in there too long they might hatch inside you.'
#===============================================================================================================#Bondage/Clothing
	elif init in [18,19,44,45]:
		second = diceroll(1,18)
		if second in [1,10]:
			result = 'You must take off all your clothes, except any diapers you\'re wearing.'
		elif second in [2,11]:
			result = 'You can no longer walk like an adult, and must crawl around like a baby.'
		elif second in [3,12]:
			result = 'Your hands are restrained by a pair of cute mittens, making it harder to grab and hold onto stuff.'
		elif second in [4,13]:
			result = 'A tight leather bondage outfit appears on you, under your clothes if you\'re wearing any. By itself it leaves all your genitals still exposed, and you can\'t seem to take it off.'
		elif second in [5,14]:
			result = 'A pair of cute stockings appear on your legs.'
		elif second in [6,15]:
			result = 'Your hands are bound with cuffs that can only be removed by someone else.'
		elif second in [7,16]:
			result = 'Your legs are bound with cuffs that can only be removed by someone else.'
		elif second in [8,17]:
			result = 'A slave collar appears around your neck, with a leash attached. Whoever holds the leash becomes your owner, and you must obey anything they tell you.'
		else:
			third = diceroll(1,3)
			if third == 1:
				result = 'A ball gag appears in your mouth, it can only be removed by someone else.'
			elif third == 2:
				result = 'A ring gag appears in your mouth, it can only be removed by someone else.'
			else:
				result = 'A pacifier appears in your mouth, it can only be removed by someone else.'	
#===============================================================================================================#Rare
	else:
		second = diceroll(1,22)
		if second in [1,12]:
			result = 'You become a succubus/incubus, able to excite the libido of others and extract their sexual fluids for sustenance.'
		elif second in [2,13]:
			result = 'Your tongue becomes extra long.'
		elif second in [3,14]:
			result = 'A tattoo appears upon your navel. It constantly makes you more aroused, and glows faintly during sex. Upon orgasm the pattern becomes more intricate, taking up more space, and the effect gets stronger.'
		elif second in [4,15]:
			result = 'Your personality is liquified into a gel-like substance, and will come leaking out your ass if you don\'t manage to hold it in, leaving your body a hollow shell and you as a blob of ' + rColor.rainbow() + ' goo.'
		elif second in [5,16]:
			result = 'Your mouth becomes a vagina.'
		elif second in [6,17]:
			result = 'A hole opens in your belly-button, making it fuckable.'
		elif second in [7,18]:
			result = 'Your nipples transform into mini ' + rSpecies() + ' cocks.'
		elif second in [8,19]:
			result = 'Your nipples transform into mini vaginas.'
		elif second in [9,20]:
			result = 'From now on when you cum, your nipples will also shoot out milk. This milk will be much thicker and sweeter than normal as well, more sticky and syrupy.'
		elif second in [10,21]:
			result = 'Your senses become connected with whoever you make physical contact with. You feel everything they feel.'
		else:
			result = 'The next person you have sex with will be absorbed into and become your genitals.'
#===============================================================================================================#End of transformations
	#display the result as a message box
	messagebox.showinfo('Transformation Result', result)

#the button itself
btn = tk.Button(frame1, text="Transform Me!", command=clicked)
btn.pack(pady=20)
btn.focus()

window.mainloop()
