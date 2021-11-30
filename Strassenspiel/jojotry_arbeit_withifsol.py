## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython



## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
##                        Garbage Collector might needed.
##    File: 
##         Program (x) 
##         Module  ( )
##    Comments: Hier wurde alles in die play()-Methode ausgelagert, im Gegensatz zur thread-Lösung, wo noch eine game()-Methode
##               investiert wurde. Evt könnte nach Teil 1 in play() noch ein Teil für Spracherkennung investiert werden.



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotic import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading

import random

import time



## 3) Definition Zone---------------------------------------------------------------------------------------------------
##    

class Strassengame(EV3Brick):

    class Straße(threading.Thread):

        def __init__(self, id="default", port=Port.A, test_=False): ################################################################################################FINE
            threading.Thread.__init__(self)
            if type(port)!=String:
                self.mot=Motor(port)
            else:
                pass
            self.id=id #um Thread 2Fakt authentifizieren zu können
            self.tempo=100 #Geschwindigkeit des zugehörigen Motors
            self.hinbeschleunigen={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0. 6: 0} #koeffizienten für polynomielle Beschleunigung
            self.test_=test_ #für print-Ausgaben, um den Ablauf zu überprüfen
            self.run_=True #variable, ob gerade der Motor laufen soll
            self.end_=False #variable, ob beendet werden soll; vorher muss self.run_ auf False gesetzt werden!
            if self.test_==True:
                print("Straße ist betriebsbereit. ")

        def beschleunige_hin(self): ######################################################################################################################FINE
            intime=time.perf_counter()
            if abs(self.mot.speed)>self.tempo:
                while self.mot.speed()!=self.tempo:
                    self.mot.run_speed(abs(-self.hinbeschleunigen[6]*(time.perf_counter-intime)**6+self.hinbeschleunigen[5]*(time.perf_counter-intime)**5-self.hinbeschleunigen[4]*(time.perf_counter-intime)**4+self.hinbeschleunigen[3]*(time.perf_counter-intime)**3-self.hinbeschleunigen[2]*(time.perf_counter-intime)**2+self.hinbeschleunigen[1]*(time.perf_counter-intime)**1-self.hinbeschleunigen[0]*(time.perf_counter-intime)**0))
                    if self.run_==False:
                        self.mot.hold()
            elif abs(self.mot.speed)<self.tempo:
                while self.mot.speed()!=self.tempo:
                    self.mot.run_speed(abs(self.hinbeschleunigen[6]*(time.perf_counter-intime)**6-self.hinbeschleunigen[5]*(time.perf_counter-intime)**5+self.hinbeschleunigen[4]*(time.perf_counter-intime)**4-self.hinbeschleunigen[3]*(time.perf_counter-intime)**3+self.hinbeschleunigen[2]*(time.perf_counter-intime)**2-self.hinbeschleunigen[1]*(time.perf_counter-intime)**1+self.hinbeschleunigen[0]*(time.perf_counter-intime)**0))
                    if self.run_==False:
                        self.mot.hold()
            elif abs(self.mot.speed())=self.tempo:
                return

            if self.test_==True:
                print("Neuer Term zum Hinbeschleunigen wurde erfolgreich geladen. ")
        
        def run(self): ######################################################################################################################FINE
            if self.test_==True:
                print("Thread wurde gestartet, in Kürze wird die Straße wahrscheinlich anfangen zu laufen")

            while True:
                while self.run_==False:
                    pass
                self.run_()
                if self.end_==False:
                    continue
                elif self.end_==True:
                    break
                else:
                    pass

            if self.test_==True:
                print("Thread wurde beendet. Die Straße wird nun in diesem Thread nicht mehr laufen. ")

        def run_(self): ######################################################################################################################FINE
            while self.run_=True:
                self.beschleunige_hin()
                self.mot.run_speed(self.tempo) #angenommen, dass das Signal an den Motor gesendet wird und dann sofort im Programmablauf fortgefahren wird
                if self.run_==False:
                    self.mot.hold()

    def __init__(self, test_=False): ######################################################################################################################FINE
        self.l=Straße(id="l", port=Port.A, test_=test_)
        self.m=Straße(id="m", port=Port.B, test_=test_)
        self.r=Straße(id="r", port=Port.C, test_=test_)
        self.end_=False
        self.test_=test_
        if self.test_==True:
            print("Straßengame wurde betriebsfertig gemacht. ")
    
    def sel_menu_item(self, args=[]): ######################################################################################################################FINE
        self.screen.clear()
        emph=0
        i=0
        while not (Button.CENTER in self.buttons.pressed()):
            for arg in args:
                if emph==i:
                    self.screen.draw_text(x=15, y=10+15*i, text=arg, text_color=Color.WHITE, background_color=Color.BLACK)
                else:
                    self.screen.draw_text(x=15, y=10+15*i, text=arg, text_color=Color.BLACK, background_color=Color.WHITE)
                i=i+1
            if (Button.RIGHT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()):
                emph=(emph+1)%5
            elif (Button.LEFT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()):
                emph=(emph-1)%5
            self.screen.clear()
        return emph

    def anleitung(self): ######################################################################################################################FINE
        texte=["Bei diesem Spiel geht es darum, mit dem Auto möglichst lange den Hindernissen auszuweichen.",
             "Das alleine wäre ja langweilig, doch währrend dem Spiel verändert sich deine Geschwindigkeit!",
             "Mit der Zeit wechselt die Geschwindigkeit öfter, schneller und zufälliger!",
             "Durch einen Druck auf die Mittlere Bricktaste kannst du das Spiel unterbrechen, durch einen zweiten Druck beenden."
             "Lenken kannst du mit dem Lenkrad, aber jetzt viel Spaß dir!"]
        emph=0
        while not (Button.CENTER in self.buttons.pressed()):
            self.screen.clear()
            self.screen.print(texte[emph])
            self.screen.print(" [Hoch/Links=Zurück, Runter/Rechts=Vor, Mitte=Ende] ")
            self.screen.print(emph +" / " +len(texte))
            if (Button.RIGHT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()):
                emph=(emph+1)%len(texte)
            elif (Button.LEFT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()):
                emph=(emph-1)%len(texte)

    def poly_beschl(self, min_polgr=10, max_polgr=0): ######################################################################################################################FINE
        polgr=ranom.randint(min_polgr, max_polgr)
        for koe in range(0, polgr):
            self.l.hinbeschleunigen[koe]=random.randint(1, 10)
            self.m.hinbeschleunigen[koe]=random.randint(1, 10)
            self.r.hinbeschleunigen[koe]=random.randint(1, 10)

    def play(self): ######################################################################################################################FINE
        # Teil 1: Willkommen
        self.screen.draw_text(x=10, y=10, 
        text="Willkommen! Du willst spielen? Dann bist du hier genau richtig! Drücke den Mittleren Knopf, um fortzufahren. ")
        while not (Button.CENTER in self.buttons.pressed()):
            pass
        if self.test_=True:
            print("Teil 1 ist erfolgreich abgelaufen. ")

        # Teil 2: Menü (Anleitung, Spiel beginnen)
        opt=self.sel_menu_item(["Erst Anleitung", "Spiel sofort beginnen"])
        if self.test_=True:
            print("Teil 2 ist erfolgreich abgelaufen. ")

        # Teil 3: Anleitung bzw. Spiel beginnen
        if opt=0:
            self.anleitung()
        else:
            pass
        level=self.sel_menu_item(["Leicht", "Eher Leicht", "Mittel", "Eher Schwer", "Schwer"])

        if self.test_=True:
            print("Teil 3 ist erfolgreich abgelaufen. ")

        # Teil 4: CENTER-Abfrage und Spielstart
        self.screen.draw_text(x=10, y=10, text="Viel Spaß! Drücke den Mittleren Knopf, um fortzufahren. ")
        while not (Button.CENTER in self.buttons.pressed()):
            pass
        self.screen.clear()
        wait(2000)
        if self.test_=True:
            print("Spielvorgang wird jetzt gestartet. ")
        self.game(level=level)

        # Teil 5: Fallunterscheidung zwischen Level; vllt Auslagerung in eigene Methoden?
        #WAS BEDEUTET WELCHES LEVEL?
        # Schwierigkeitsstufe    | Beschleunigen                                                                      | Zielgeschwindigkeit
        # Leicht(0)              | Pol vom Grad 2;              wird per randint am Anfang festgelegt, dann konstant  | Variiert alle 5 Sekunden
        # Eher Leicht(1)         | Pol vom Grad 3;              wird per randint am Anfang festgelegt, dann konstant  | Variiert alle randint(4, 8) Sekunden
        # Mittel(2)              | Pol vom Grad randint(2, 5);  Variiert alle 5 Sekunden                              | Variiert alle randint(3, 7) Sekunden
        # Eher Schwer(3)         | Pol vom Grad randint(2, 6);  Variiert alle randint(4, 8) Sek                       | Variiert alle randint(2, 6) Sekunden
        # Schwer(4)              | Pol vom Grad randint(3, 6);  Variiert alle randint(3, 7) Sek                       | Variiert alle randint(1, 5) Sekunden
        # ----------------------------------------------------------------------------------------------------------------------------------------------
        # 5 Schwierigkeiten      |  Polynomiell;                 fest/(variabel) variierend; KoEs zwischen 1 und 10   | (variabel) variierend; zwischen 1 und 200       (RANDINT-variator)

        #VORSICHT!!!! Rückwärtsgang ist dabei! Da es sonst ziemlich schwer würde...

        if self.test_=True:
            print("Teil 5 ist erfolgreich gestartet. ")
        self.l.run()
        self.r.run()
        self.m.run()
        if level==0:
            tempo=5
            tempo_=1
            self.l.hinbeschleunigen[0]=random.randint(1, 10)
            self.l.hinbeschleunigen[1]=random.randint(1, 10)
            self.l.hinbeschleunigen[2]=random.randint(1, 10)
            self.m.hinbeschleunigen[0]=random.randint(1, 10)
            self.m.hinbeschleunigen[1]=random.randint(1, 10)
            self.m.hinbeschleunigen[2]=random.randint(1, 10)
            self.r.hinbeschleunigen[0]=random.randint(1, 10)
            self.r.hinbeschleunigen[1]=random.randint(1, 10)
            self.r.hinbeschleunigen[2]=random.randint(1, 10)
            self.l.tempo=random(1, 200)
            self.m.tempo=random(1, 200)
            self.r.tempo=random(1, 200)
            global starttime=time.perf_counter()
            while self.end_==False:
                while not (Button.CENTER in self.buttons.pressed()):
                    self.screen.clear()
                    self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                    self.screen.print("[Mitte=Unterbrechung]")
                    if (int(time.perf_counter()-starttime)>=(tempo*tempo_)):
                        self.l.tempo=random(1, 200); self.m.tempo=random(1, 200); self.r.tempo=random(1, 200)
                        tempo_=tempo_+1
                foo=self.sel_menu_item(["- Fortfahren -", "- Zum Hauptmenü -"])
                if foo=0:
                    continue
                elif foo=1:
                    self.end_=True
                    self.l.end_=True
                    self.m.end_=True
                    self.r.end_=True
                    self.beschleuniger.end_=True
                    self.tempo.end_=True
                else:
                    pass
        
        elif level==1:
            tempo=0
            self.l.hinbeschleunigen[0]=random.randint(1, 10)
            self.l.hinbeschleunigen[1]=random.randint(1, 10)
            self.l.hinbeschleunigen[2]=random.randint(1, 10)
            self.l.hinbeschleunigen[3]=random.randint(1, 10)
            self.m.hinbeschleunigen[0]=random.randint(1, 10)
            self.m.hinbeschleunigen[1]=random.randint(1, 10)
            self.m.hinbeschleunigen[2]=random.randint(1, 10)
            self.m.hinbeschleunigen[3]=random.randint(1, 10)
            self.r.hinbeschleunigen[0]=random.randint(1, 10)
            self.r.hinbeschleunigen[1]=random.randint(1, 10)
            self.r.hinbeschleunigen[2]=random.randint(1, 10)
            self.r.hinbeschleunigen[3]=random.randint(1, 10)
            global starttime=time.perf_counter()
            while self.end_==False:
                while not (Button.CENTER in self.buttons.pressed()):
                    self.screen.clear()
                    self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                    self.screen.print("[Mitte=Unterbrechung]")
                    if (int(time.perf_counter()-starttime)>=(tempo)):
                        self.l.tempo=random(1, 200); self.m.tempo=random(1, 200); self.r.tempo=random(1, 200); tempo=randint(4, 8)+int(time.perf_counter()-starttime)
                foo=self.sel_menu_item(["- Fortfahren -", "- Zum Hauptmenü -"])
                if foo=0:
                    continue
                elif foo=1:
                    self.end_=True
                    self.l.end_=True
                    self.m.end_=True
                    self.r.end_=True
                    self.beschleuniger.end_=True
                    self.tempo.end_=True
                else:
                    pass
        
        elif level==2:
            beschl=0
            tempo=5
            beschl_=1
            self.poly_beschl(min_polgr=2, max_polgr=5)
            global starttime=time.perf_counter()
            while self.end_==False:
                while not (Button.CENTER in self.buttons.pressed()):
                    self.screen.clear()
                    self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                    self.screen.print("[Mitte=Unterbrechung]")
                    if (int(time.perf_counter()-starttime)>=(tempo)):
                        self.l.tempo=random(1, 200)
                        self.m.tempo=random(1, 200)
                        self.r.tempo=random(1, 200)
                        tempo=randint(3, 7)+int(time.perf_counter()-starttime)
                    elif (int(time.perf_counter()-starttime)>=(beschl*beschl_)):
                        self.poly_beschl(min_polgr=2, max_polgr=5)
                        beschl_=beschl_+1
                foo=self.sel_menu_item(["- Fortfahren -", "- Zum Hauptmenü -"])
                if foo=0:
                    continue
                elif foo=1:
                    self.end_=True
                    self.l.end_=True
                    self.m.end_=True
                    self.r.end_=True
                    self.beschleuniger.end_=True
                    self.tempo.end_=True
                else:
                    pass
        
        elif level==3:
            beschl=0
            tempo=0
            self.poly_beschl(min_polgr=2, max_polgr=5)
            global starttime=time.perf_counter()
            while self.end_==False:
                while not (Button.CENTER in self.buttons.pressed()):
                    self.screen.clear()
                    self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                    self.screen.print("[Mitte=Unterbrechung]")
                    if (int(time.perf_counter()-starttime)>=(tempo)):
                        self.l.tempo=random(1, 200)
                        self.m.tempo=random(1, 200)
                        self.r.tempo=random(1, 200)
                        tempo=random.randint(2, 6)+int(time.perf_counter()-starttime)
                    elif (int(time.perf_counter()-starttime)>=(tempo)):
                        self.poly_beschl(min_polgr=2, max_polgr=6)
                        beschl=random.randint(4, 8)+int(time.perf_counter()-starttime)
                foo=self.sel_menu_item(["- Fortfahren -", "- Zum Hauptmenü -"])
                if foo=0:
                    continue
                elif foo=1:
                    self.end_=True
                    self.l.end_=True
                    self.m.end_=True
                    self.r.end_=True
                    self.beschleuniger.end_=True
                    self.tempo.end_=True
                else:
                    pass
        
        elif level==4:
            beschl=0
            temp=0
            self.poly_beschl(min_polgr=2, max_polgr=5)
            global starttime=time.perf_counter()
            while self.end_==False:
                while not (Button.CENTER in self.buttons.pressed()):
                    self.screen.clear()
                    self.screen.print("Dein Score ist: " +str(int((time.perf_counter()-starttime)*100)))
                    self.screen.print("[Mitte=Unterbrechung]")
                    if (int(time.perf_counter()-starttime)>=(tempo)):
                        self.l.tempo=random(1, 200)
                        self.m.tempo=random(1, 200)
                        self.r.tempo=random(1, 200)
                        tempo=random.randint(1, 5)+int(time.perf_counter()-starttime)
                    elif (int(time.perf_counter()-starttime)>=(tempo)):
                        self.poly_beschl(min_polgr=3, max_polgr=6)
                        beschl=random.randint(3, 7)+int(time.perf_counter()-starttime)
                self.l.run_=False
                self.m.run_=False
                self.r.run_=False
                foo=self.sel_menu_item(["- Fortfahren -", "- Zum Hauptmenü -"])
                if foo=0:
                    continue
                elif foo=1:
                    self.end_=True
                    self.l.end_=True
                    self.m.end_=True
                    self.r.end_=True
                    self.beschleuniger.end_=True
                    self.tempo.end_=True
                else:
                    pass
        
        else:
            self.screen.print("Hier ist ein Fehler passiert! Hole einen Techniker!")
            self.screen.print(" [False level given - Programming Error] ")
        if self.test_=True:
            print("Teil 5 ist erfolgreich abgelaufen. ")



## 4) Programming Zone--------------------------------------------------------------------------------------------------
##   
game=Strassengame(test_=True)
game.play()


