import bot
import csv
import os
from gtts import gTTS
from playsound import playsound
from datetime import *
from time import *
print(">..hello!! my name is SAAT")
snd = gTTS("hello!! my name is SAAT")
o=0
it=str(o)+".mp3"
snd.save(it)
playsound(it)
os.remove(it)
o+=1
a=bot.per()
while 1:
 vl=a.get()
 sleep(0.5)
 if a.chk("hl"):
    print(">..nice to meet you")
    snd = gTTS(".nice to meet you")
    it = str(o) + ".mp3"
    snd.save(it)
    playsound(it)
    os.remove(it)
    o+=1
 elif a.chk("tell time"):
     now=datetime.now()
     print(now.strftime("%Y-%m-%d %H:%M:%S"))
     snd = gTTS(now.strftime("%Y-%m-%d %H:%M:%S"))
     it = str(o) + ".mp3"
     snd.save(it)
     playsound(it)
     os.remove(it)
     o+=1
 elif a.chk("exit"):
     snd = gTTS("bye")
     it = str(o) + ".mp3"
     snd.save(it)
     playsound(it)
     os.remove(it)
     o+=1
     break
 else:
     c=0
     f1 = open('ai.csv', 'r')
     op2 = csv.reader(f1)
     f1.seek(0)
     for i in op2:
         if i[0]==vl:
             st =i[1]
             snd = gTTS(st)
             it = str(o) + ".mp3"
             snd.save(it)
             playsound(it)
             os.remove(it)
             o+=1
             print('>..{}'.format(i[1]))
             c=1
     f1.close()
     if c==0:
      snd = gTTS(".i m not getting it plz help me to train")
      it = str(o) + ".mp3"
      snd.save(it)
      playsound(it)
      os.remove(it)
      o+=1
      print(">..i m not getting it plz help me to train")
      f = open("ai.csv", 'a', newline="")
      op = csv.writer(f)
      op.writerow(['', ''])
      sg=input("..")
      op.writerow([vl,sg])
      f.close()