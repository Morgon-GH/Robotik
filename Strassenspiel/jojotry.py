## 0) Filepath----------------------------------------------------------------------------------------------------------
##    
#!/usr/bin/env pybricks-micropython



## 1) Commentation Zone-------------------------------------------------------------------------------------------------
##    
##    Author: Johannes und Moritz
##    Language: Micropython (Python) v 2.0
##    Important comments: This program requires LEGO EV3 MicroPython v2.0 or higher.
##                        Garbage Collector might needed.
##    File: 
##         Program (x) 
##         Module  ( )



## 2) Import Zone-------------------------------------------------------------------------------------------------------
##    

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotic import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import threading



## 3) Definition Zone---------------------------------------------------------------------------------------------------
##    

class Strassengame(EV3Brick):

    class Straße(threading.Thread):

        def __init__(self, id="default", port=Port.A, test_=False):
            threading.Thread.__init__(self)
            self.id=id
            self.mot=Motor(port)
            self.tempo_=True
            self.tempo=100
            self.hinbeschleunigen={1: 1}
            self.test_=test_
            if self.test_==True:
                print("Straße ist betriebsbereit. ")

        def beschleunige_hin(self):
            pass
        
        def run(self):
            if self.test_==True:
                print("Thread wurde gestartet, in Kürze wird die Straße wahrscheinlich anfangen zu laufen")

            pass

            if self.test_==True:
                print("Thread wurde beendet. Die Straße wird nun in diesem Thread nicht mehr laufen. ")

        def sethinbeschleunigen(self):

            pass

            if self.test_==True:
                print("Neuer Term zum Hinbeschleunigen wurde erfolgreich geladen. ")

    def __init__(self, test_=False):
        self.l=Straße(id="l", port=Port.A, test_=test_)
        self.m=Straße(id="m", port=Port.B, test_=test_)
        self.r=Straße(id="r", port=Port.C, test_=test_)
        self.test_=test_
        if self.test_==True:
            print("Straßengame wurde betriebsfertig gemacht. ")

    def stelleSchnelligkeit(self):
        pass

    def sel_menu_item(self, args=[]):
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
            if (Button.LEFT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()):
                emph=(emph+1)%5
            elif (Button.RIGHT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()):
                emph=(emph-1)%5
            self.screen.clear()
        return emph

    def anleitung(self):
        pass

    def game(self):
        while not (Button.CENTER in self.buttons.pressed()):
            pass

    def advertisement(self):
        pass                        #optional

    def play(self):
        # Teil 1: Willkommen
        self.screen.draw_text(x=10, y=10, text="Willkommen! Du willst spielen? Dann bist du hier genau richtig! Drücke den Mittleren Knopf, um fortzufahren. ")
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

        # Teil 4: CENTER-Abfrage und Spiel
        self.screen.draw_text(x=10, y=10, text="Viel Spaß! Drücke den Mittleren Knopf, um fortzufahren. ")
        while not (Button.CENTER in self.buttons.pressed()):
            pass
        self.screen.clear()
        wait(2000)
        self.game()
        if self.test_=True:
            print("Teil 4 ist erfolgreich abgelaufen. ")



## 4) Programming Zone--------------------------------------------------------------------------------------------------
##    
game=Strassengame(test_=True)
game.play()

