#Task-1

#Tokanize Using library

from tamil import vaaninlp

#To get Tamil letters
ezhuthu = vaaninlp.char_tokenize("""கைத்தல நிறைகனி அப்பமொடவல்பொரி""")
print(ezhuthu)
print("Eluthu count:",len(ezhuthu))

#lists for 3 types of char
mei_eluthu =['்']
kuril_eluthu=['ெ','ி','ொ','ு','அ', 'இ', 'உ', 'எ', 'ஒ', 'க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள',
                'ற', 'ன']
nedil_eluthu=['ீ','ே','ோ','ௌ','ூ','ா','ஆ','ஈ','ஊ','ஏ','ஐ','ஓ','ௗ','ை']

#intialise the count
ku=0
ned=0
mei=0
#loop through the list
for i in range(len(ezhuthu)):
  #check each char for kuril, nedil, mei
  if ezhuthu[i][-1] in kuril_eluthu:
    ku += 1
  elif ezhuthu[i][-1] in nedil_eluthu:
    ned += 2
  if ezhuthu[i][-1] == mei_eluthu[0]:
    if ezhuthu[i-1][-1] in nedil_eluthu:
      mei +=1 # if previous of mei is nedil then 1
    mei += 0.5 #simply for mei


print("Total_aksharam:",int(ku+ned+mei)) #print the total count
