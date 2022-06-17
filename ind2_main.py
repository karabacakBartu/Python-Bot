from logging import exception
from ind1_excelread import excelcek
import random
import pyautogui
from time import sleep
try:
    kacbas=int(input("kaçtan başlansın:"))
    kacmes=int(input("kaç mesaj atlsın:"))
    col=int(input("sütun gir:"))
    mb=["m1.txt","m2.txt","m3.txt"]
    list2=[]
    list2=excelcek(kacbas,kacmes,col)
    print(list2,len(list2))
#mouse yönetim
    i=0
    say=0
    while i<len(list2):
        icerik=""
        x=736
        y=162
        f = open(mb[random.randint(0,2)],'r')
        oku=f.readlines()
        for j, v in enumerate(oku):
            icerik+=v.strip()
        sleep(3)
        pyautogui.click(x,y)
        sleep(1)
        pyautogui.click(x+150,y)
        sleep(1)
        pyautogui.write(list2[i])
        
        say+=1
        print(list2[i]," sıra:",list2.index(list2[i])," kalan:",len(list2)-(say))

        yaz=open("sonnumara.txt","a")
        yaz.write(list2[i])
        yaz.close()
        sleep(1)
        pyautogui.click(x+150,y+760)
        sleep(2)
        pyautogui.write(icerik,0.01)
        sleep(1)
        pyautogui.press("enter")
        sleep(20)
    
        i+=1


except Exception as e:
    print(e)
    ext=input('press any key to exit')
    if ext: 
        exit(0)

