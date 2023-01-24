#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

import time
from random import randint
from math import sqrt


# Objects (1)
ev3=EV3Brick()
ev3.screen.print("<!EV3Brick 'ev3dev'>")
ev3.screen.print("is booting now.")
motor_links=Motor(Port.A)
motor_mitte=Motor(Port.A)
motor_rechts=Motor(Port.C)
auto_sensor=TouchSensor(Port.S1)
fortfahren=TouchSensor(Port.S2)
ausgabekonfigurationen={"sprache": "DE"}
ev3.screen.set_font(Font('Lucida', 11))


# Definitions (2)
def lese_texte_aus():
    dateiname=str(ausgabekonfigurationen["sprache"]) +".txt"
    dateizugriff=open(dateiname, "r")
    inhalt=dateizugriff.read()
    exec(inhalt)
    dateizugriff.close()

def halter():
    while not (fortfahren.pressed()):
        wait(20)
    wait(500)

def zeit_in_millisekunden() -> int:
    return int(time.time()*1000)

def zeige_warte(texte: list):
    for text in texte:
        ev3.screen.clear()
        gebe_aus(text, x=5, y=5)
        ev3.screen.draw_text(text="Roter Knopf", x=50, y=100)
        halter()

def gebe_formatierten_text_aus(x: int, y: int, text: str, text_color: Color=Color.BLACK, background_color: Color=Color.WHITE, zeilenlaenge=21, zeilenhoehe=11): #ab 15 Zeilen grob ein Problem
    zaehler=0
    for i in text:
        spalte=(zaehler)%zeilenlaenge
        zeile=(zaehler-(zaehler % zeilenlaenge))/zeilenlaenge
        ev3.screen.draw_text(x=x+spalte*7, y=y+3+int(zeile)*zeilenhoehe, text=i, text_color=text_color, background_color=background_color)
        zaehler=zaehler+1
        wait(50) 

def gebe_aus(text=" ", x=0, y=0, text_color: Color =Color.BLACK, background_color: Color =Color.WHITE, bubble_=True, zeilenlaenge:int =25, zeilenhoehe:int =10):
    if bubble_==True:
        gebe_formatierten_text_aus(x=y, y=y, text=text, text_color=text_color, background_color=background_color, zeilenlaenge = zeilenlaenge, zeilenhoehe = zeilenhoehe)
    else:
        ev3.screen.draw_text(x=x, y=y, text=text, text_color=text_color, background_color=background_color)

def gebe_name() -> str:
    y=0
    x=0
    name=[" "]
    ausgewaehlt=""
    tastatur=["Q", "W", "E", "R", "T", "Z", "U", "I", "O",
              "P", "A", "S", "D", "F", "G", "H", "J", "K",
              "L", "Y", "X", "C", "V", "zeit_des_stopps", "N", "M", "<"]
    while not fortfahren.pressed():
        ev3.screen.clear()
        name_bis_jetzt=""
        for i in name:
            name_bis_jetzt=name_bis_jetzt+"".join(i)
        gebe_aus(x=15, y=10, text=name_bis_jetzt)
        pos=0
        for letter in tastatur:
            if (x==pos//9) and (y==pos%9):
                ev3.screen.draw_text(x=25+15*(pos%9), y=35+25*(pos//9), text=letter, text_color=Color.WHITE, background_color=Color.BLACK)
                ausgewaehlt=letter
            else:
                ev3.screen.draw_text(x=25+15*(pos%9), y=35+25*(pos//9), text=letter, text_color=Color.BLACK, background_color=Color.WHITE)
            pos=pos+1
        wait(500)
        while not (fortfahren.pressed() or (Button.CENTER in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.RIGHT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed())):
            pass
        if fortfahren.pressed():
            return name_bis_jetzt
        if (Button.CENTER in ev3.buttons.pressed()):
            if ((x==2) and (y==8)):
                try:
                    del name[int(len(name)-1)]
                except:
                    pass
            else:
                if len(name)>=20:
                    gebe_aus(x=8, y=100, text=texte[0][1])
                    wait(2000)
                else:
                    name.append(ausgewaehlt)
        if (Button.DOWN in ev3.buttons.pressed()):
            if x>1:
                x=x-2
            else:
                x=x+1
        if (Button.UP in ev3.buttons.pressed()):
            if x<1:
                x=x+2
            else:
                x=x-1
        if (Button.RIGHT in ev3.buttons.pressed()):
            if y>7:
                y=y-8
            else:
                y=y+1
        if (Button.LEFT in ev3.buttons.pressed()):
            if y<1:
                y=y+8
            else:
                y=y-1

def schreibe_bestenliste(score: int, username: str):
    with open("highscore.txt", "a") as file:
            file.write(str(score)+";"+username+";")

def bestenliste():
    with open("highscore.txt", "r") as file:
        sortierte_liste=[]
        bestenliste_eintraege=[]
        bestenliste_ganzer_inhalt=file.read()
        bestenliste_eintraege=bestenliste_ganzer_inhalt.split(";")
        for i in range(0, len(bestenliste_eintraege)-1):
            if i%2!=0:  
                sortierte_liste.append([bestenliste_eintraege[i-1], bestenliste_eintraege[i]])

        for i in range(len(sortierte_liste)):
            sortierte_liste[i][0]; int =int(sortierte_liste[i][int(0)])

        for i in range(555):
            for i in range(len(sortierte_liste)-1):
                if abs(sortierte_liste[i][0]) < abs(sortierte_liste[i+1][0]): # ordnet die Plaetze an    HIER SIND DATENTYPEN FRAGLICH
                    change=sortierte_liste[i]
                    sortierte_liste[i]=sortierte_liste[i+1]
                    sortierte_liste[i+1]=change
    
        for i in range(len(sortierte_liste)):
            sortierte_liste[i][0]=str(sortierte_liste[i][int(0)])

    ausgewaehlter_menuepunkt=0
    position=0
    while not Button.CENTER in ev3.buttons.pressed():
        ev3.screen.clear()
        gebe_aus(text=texte[0][2], x=30, y=5, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
        for i in range(ausgewaehlter_menuepunkt*7, 7*(ausgewaehlter_menuepunkt+1)):
            try:
                rang=ausgewaehlter_menuepunkt+position+1
                line=str(rang)+". "+"".join(sortierte_liste[i])
                gebe_aus(x=15, y=15+15*position, text=line)
                position=position+1
            except:
                pass
        while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
            pass
        if (Button.RIGHT in ev3.buttons.pressed() or Button.DOWN in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt+7)%(len(sortierte_liste)//7+1)
            position=0
            wait(200)
        elif (Button.LEFT in ev3.buttons.pressed() or Button.UP in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt-7)%(len(sortierte_liste)//7+1)
            position=0
            wait(200)
    wait(500)

def menu_anzeiger(ueberschrift: str, auswaehlbarer_inhalt: str, x=30, y=5, einrueck=20) -> int:
    ausgewaehlter_menuepunkt=1
    while True:
    wait(200)
    ev3.screen.clear()
    gebe_aus(text=ueberschrift, x=x, y=y, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
    for i in range(1, len(auswaehlbarer_inhalt)):
        if ausgewaehlter_menuepunkt==i:
            gebe_aus(text=auswaehlbarer_inhalt[i-1], x=x, y=y+einrueck*i, text_color=Color.WHITE, background_color=Color.BLACK, bubble_=False)
        else:
            gebe_aus(text=auswaehlbarer_inhalt[i-1], x=x, y=y+einrueck*i, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
        while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
            pass
        if (Button.DOWN in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt+1)%(len(auswaehlbarer_inhalt)-1)
            if ausgewaehlter_menuepunkt==0:
                ausgewaehlter_menuepunkt=1
            continue
        elif (Button.UP in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt-1)%(len(auswaehlbarer_inhalt)-1)
            if ausgewaehlter_menuepunkt==0:
                ausgewaehlter_menuepunkt=1
            continue
        else:
            return ausgewaehlter_menuepunkt


# Begrüßung (3)
lese_texte_aus()
ev3.screen.clear()
zeige_warte([texte[0][5]])


# Menü (4)
while True:
    ausgewaehlter_menuepunkt=menu_anzeiger(ueberschrift=texte[1][0], auswaehlbarer_inhalt=[texte[1][1], texte[1][2], texte[1][3], texte[1][4]])
    if (Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()):
        if (ausgewaehlter_menuepunkt==1) or (ausgewaehlter_menuepunkt==2):
            for text in texte[1+ausgewaehlter_menuepunkt]:
                zeige_warte([text])
            ausgewaehlter_menuepunkt=0
            continue
        elif ausgewaehlter_menuepunkt==3:
            ausgewaehlter_menuepunkt=0
            wait(1000)
            bestenliste()
            continue
        elif ausgewaehlter_menuepunkt==4:
            break


    # Hauptprogramm (5)
    ## Die Durchschnittsgeschwindigkeit durchschnittsgeschwindigkeit ist die Wurzel der Zeit plus 200, die seit startzeit verstrichen ist.
    wait(500)
    ev3.speaker.beep()
    startgeschwindigkeit=-200
    durchschnittsgeschwindigkeit=200
    alle_geschwindigkeiten=[startgeschwindigkeit, startgeschwindigkeit, startgeschwindigkeit]
    zeit_fuer_neue_geschwindigkeit=randint(1, 5)
    nicht_verloren=True
    startzeit=zeit_in_millisekunden()
    while nicht_verloren==True:
        motor_links.run(-(int(alle_geschwindigkeiten[randint(0, 1)])))
        motor_mitte.run(-(int(alle_geschwindigkeiten[randint(0, 2)])))
        motor_rechts.run(-(int(alle_geschwindigkeiten[randint(1, 2)])))
        punktzahl=int(zeit_in_millisekunden()-startzeit)
        if auto_sensor.pressed()==True:
            nicht_verloren=False
            motor_links.hold()
            motor_mitte.hold()
            motor_rechts.hold()
            motor_links.run_angle(100, 360)
            motor_mitte.run_angle(100, 360)
            motor_rechts.run_angle(100, 360)
        while int(zeit_in_millisekunden()-startzeit)%zeit_fuer_neue_geschwindigkeit!=0:
            if (fortfahren.pressed()):
                zeit_des_stopps=zeit_in_millisekunden()
                motor_links.hold()
                motor_mitte.hold()
                motor_rechts.hold()
                ev3.screen.clear()
                ev3.screen.print(texte[0][3])
                ev3.screen.print(texte[0][4])
                wait(500)
                halter()
                zeit_des_weiterspielens=zeit_in_millisekunden()
                startzeit=startzeit+(zeit_des_weiterspielens-zeit_des_stopps)
            if (auto_sensor.pressed()):
                nicht_verloren=False
                motor_links.hold()
                motor_mitte.hold()
                motor_rechts.hold()
                motor_links.run_angle(100, 360)
                motor_mitte.run_angle(100, 360)
                motor_rechts.run_angle(100, 360)
            punktzahl=int(zeit_in_millisekunden()-startzeit)
            ev3.screen.print(str(punktzahl))
            wait(10)
            ev3.screen.clear()
        durchschnittsgeschwindigkeit=int(sqrt(int(zeit_in_millisekunden()-startzeit)))+200
        alle_geschwindigkeiten[0]=randint(1, int(durchschnittsgeschwindigkeit))
        alle_geschwindigkeiten[1]=randint(int(durchschnittsgeschwindigkeit/2), int(2*durchschnittsgeschwindigkeit))
        alle_geschwindigkeiten[2]=(int(durchschnittsgeschwindigkeit)-(int(alle_geschwindigkeiten[0])+int(alle_geschwindigkeiten[1]))/3)*3
        zeit_fuer_neue_geschwindigkeit=randint(1, 5)

    # Programmende (6)
    zeige_warte([texte[0][6], texte[0][7]])
    gebe_aus(texte[0][8])
    while not (Button.CENTER in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()):
        pass
    if Button.CENTER in ev3.buttons.pressed():
        continue
    wait(1000)
    name=gebe_name()
    wait(1000)
    schreibe_bestenliste(score=punktzahl, username=name)
    bestenliste()

    # Bestenlistenupdate (7)
    # Immer nur die letzte Partie wird überspielt - es wird also von gemeinsamen Start ausgegangen, und dass beide an sowie gepaired sind.