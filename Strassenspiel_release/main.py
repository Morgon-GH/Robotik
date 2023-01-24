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
ev3.screen.print("<!EV3Brick 'ev3dev'> is booting")
motor_links=Motor(Port.A)
motor_mitte=Motor(Port.B)
motor_rechts=Motor(Port.C)
auto_sensor=TouchSensor(Port.S1)
fortfahren=TouchSensor(Port.S2)
ausgabekonfigurationen={"sprache": "DE"}
ev3.screen.set_font(Font('Lucida', 14))


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

def zeit_in_millisekunden():
    return int(time.time()*1000)

def zeige_warte(texte: list):
    for text in texte:
        ev3.screen.clear()
        gebe_aus(text, x=5, y=5)
        ev3.screen.draw_text(text="[Roter Knopf]", x=45, y=110)
        halter()

def gebe_formatierten_text_aus(x: int, y: int, text: str, text_color: Color=Color.BLACK, background_color: Color=Color.WHITE, zeilenlaenge: int =21, zeilenhoehe: int =10):
    zaehler=0
    for i in text:
        spalte = (zaehler)%zeilenlaenge
        zeile = zaehler//zeilenlaenge
        ev3.screen.draw_text(x=x+spalte*8, y=y+zeile*zeilenhoehe, text=i, text_color=text_color, background_color=background_color)
        zaehler = zaehler + 1
        wait(50) 

def gebe_aus(text: str ="default", x: int =0, y: int =0, text_color: Color =Color.BLACK, background_color: Color =Color.WHITE, bubble_: bool =True, zeilenlaenge: int =22, zeilenhoehe: int =16):
    if bubble_==True:
        gebe_formatierten_text_aus(x=y, y=y, text=text, text_color=text_color, background_color=background_color, zeilenlaenge = zeilenlaenge, zeilenhoehe = zeilenhoehe)
    else:
        ev3.screen.draw_text(x=x, y=y, text=text, text_color=text_color, background_color=background_color)

def gebe_name():
    y=0
    x=0
    name=[" "]
    ausgewaehlt=""
    tastatur=["Q", "W", "E", "R", "T", "Z", "U", "I", "O",
              "P", "A", "S", "D", "F", "G", "H", "J", "K",
              "L", "Y", "X", "C", "V", "B", "N", "M", "<"]
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
                    gebe_aus(x=8, y=100, text="Maximale Länge erreicht!")
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
            sortierte_liste[i][0]=int(sortierte_liste[i][int(0)])

        for i in range(555):
            for i in range(len(sortierte_liste)-1):
                if abs(sortierte_liste[i][0]) < abs(sortierte_liste[i+1][0]): # ordnet die Plaetze an
                    change=sortierte_liste[i]
                    sortierte_liste[i]=sortierte_liste[i+1]
                    sortierte_liste[i+1]=change
    
        for i in range(len(sortierte_liste)):
            sortierte_liste[i][0]=str(sortierte_liste[i][int(0)])

    ausgewaehlter_menuepunkt=0
    position=0
    while (not Button.CENTER in ev3.buttons.pressed()) and (not fortfahren.pressed()):
        ev3.screen.clear()
        gebe_aus(text="Highscore", x=30, y=5, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
        for i in range(ausgewaehlter_menuepunkt*7, 7*(ausgewaehlter_menuepunkt+1)):
            try:
                rang=ausgewaehlter_menuepunkt+position+1
                line=str(rang)+". "+"".join(sortierte_liste[i])
                gebe_aus(x=15, y=15+15*position, text=line)
                position=position+1
            except:
                pass
        while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()) or (fortfahren.pressed())):
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

# Begrüßung (3)
lese_texte_aus()
ev3.screen.clear()
zeige_warte([texte[0][0]])


# Menü (4)
while True:
    ausgewaehlter_menuepunkt=0
    while True:
        wait(200)
        ev3.screen.clear()
        gebe_aus(text="Hauptmenü", x=30, y=5, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
        for i in range(0, len(texte[1])):
            if ausgewaehlter_menuepunkt==i:
                gebe_aus(text=texte[1][i], x=30, y=28+23*i, text_color=Color.WHITE, background_color=Color.BLACK, bubble_=False)
            else:
                gebe_aus(text=texte[1][i], x=30, y=28+23*i, text_color=Color.BLACK, background_color=Color.WHITE, bubble_=False)
        while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
            pass
        if (Button.DOWN in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt+1)%len(texte[2])
            continue
        elif (Button.UP in ev3.buttons.pressed()):
            ausgewaehlter_menuepunkt=(ausgewaehlter_menuepunkt-1)%len(texte[2])
            continue
        elif (Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed()):
            if (ausgewaehlter_menuepunkt==0) or (ausgewaehlter_menuepunkt==1):
                for text in texte[2+ausgewaehlter_menuepunkt]:
                    zeige_warte([text])
                ausgewaehlter_menuepunkt=0
                continue
            elif ausgewaehlter_menuepunkt==2:
                ausgewaehlter_menuepunkt=0
                wait(1000)
                bestenliste()
                continue
            elif ausgewaehlter_menuepunkt==3:
                ausgewaehlter_menuepunkt=0
                wait(500)
                break


    # Hauptprogramm (5)
    ## Die Durchschnittsgeschwindigkeit durchschnittsgeschwindigkeit ist die Wurzel der Zeit plus 200, die seit startzeit verstrichen ist.
    wait(500)
    ev3.speaker.beep()
    startgeschwindigkeit=-200
    durchschnittsgeschwindigkeit=200
    ges=[startgeschwindigkeit, startgeschwindigkeit, startgeschwindigkeit]
    timetoreset=randint(1, 5)
    nicht_verloren=True
    startzeit=zeit_in_millisekunden()
    while nicht_verloren==True:
        motor_links.run(-(int(ges[randint(0, 1)])))
        motor_mitte.run(-(int(ges[randint(0, 2)])))
        motor_rechts.run(-(int(ges[randint(1, 2)])))
        foo=int(zeit_in_millisekunden()-startzeit)
        if auto_sensor.pressed()==True:
            nicht_verloren=False
            motor_links.hold()
            motor_mitte.hold()
            motor_rechts.hold()
            motor_links.run_angle(100, 360)
            motor_mitte.run_angle(100, 360)
            motor_rechts.run_angle(100, 360)
        while int(zeit_in_millisekunden()-startzeit)%timetoreset!=0:
            if (fortfahren.pressed()):
                b=zeit_in_millisekunden()
                motor_links.hold()
                motor_mitte.hold()
                motor_rechts.hold()
                ev3.screen.clear()
                ev3.screen.print("Spiel unterbrochen!")
                ev3.screen.print("Roter Knopf zum Fortfahren")
                wait(500)
                halter()
                a=zeit_in_millisekunden()
                startzeit=startzeit+(a-b)
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
        ges[0]=randint(1, int(durchschnittsgeschwindigkeit))
        ges[1]=randint(int(durchschnittsgeschwindigkeit/2), int(2*durchschnittsgeschwindigkeit))
        ges[2]=(int(durchschnittsgeschwindigkeit)-(int(ges[0])+int(ges[1]))/3)*3
        timetoreset=randint(1, 5)

    # Programmende (6)
    zeige_warte(["Du hast verloren! Das Auto ist gegen ein Hindernis gedonnert...", "Aber lass uns doch mal schauen, ob du vielleicht den Highscore geknackt hast!"])
    ev3.screen.clear()
    gebe_aus("Gleich kannst du deinen Namen eingeben, danach wird dieser mit deinem Score in der Bestenliste gespeichert und diese angezeigt. Willst du das, drücke eine Steintaste, die nicht die Mitte ist.")
    while not ((Button.CENTER in ev3.buttons.pressed()) or (Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or fortfahren.pressed()):
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

    # TODO