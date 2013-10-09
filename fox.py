# What does the Fox Say?
#
# For those who have been living under a rock:
# http://www.youtube.com/watch?v=jofNR_WkoCE
import random as rand

FOX_PHRASES = [ "Ring-ding-ding-ding-dingeringeding!",
			    "Gering-ding-ding-ding-dingeringeding!",
			    "Wa-pa-pa-pa-pa-pa-pow!",
			    "Hatee-hatee-hatee-ho!",
			    "Joff-tchoff-tchoffo-tchoffo-tchoff!",
			    "Tchoff-tchoff-tchoffo-tchoffo-tchoff!",
			    "Jacha-chacha-chacha-chow!",
			    "Chacha-chacha-chacha-chow!",
			    "Fraka-kaka-kaka-kaka-kow!",
			    "A-hee-ahee ha-hee!",
			    "A-oo-oo-oo-ooo!", 
			    "Woo-oo-oo-ooo!" ]

def whatDoesTheFoxSay():
	return FOX_PHRASES[int(rand.random()*(len(FOX_PHRASES)-1))]

def main():
	f = open("song.txt", 'r')
	for line in f:
		if line.rstrip('\n') == "FOX":
			print whatDoesTheFoxSay()
		else:
			print line.rstrip('\n')

if __name__ == "__main__":
	main()