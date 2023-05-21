import PySimpleGUI as sg
import urllib.request
import core.musicmgr_json
from random import randint
import pygame

class CredimusicMain:
    def __init__(self):
        self.applayout = [
            [sg.Text("No music playing.", key="-MUSICTEXT-", justification="center")],
            [sg.Button("Play"), sg.Button("Stop"), sg.Button("Exit")]
        ]

        self.appwindow = sg.Window("Credimusic", self.applayout)
        self.manualEnd = False
        self.musicList = core.musicmgr_json.readMusicDef()
        print(self.musicList)

    def launch(self):
        while True:
            event, values = self.appwindow.read()

            if event == sg.WIN_CLOSED or event == "Exit":
                break

            elif event == "Play":
                self.playMusic()

            elif event == "Stop":
                self.manualEnd = True
                self.stopMusic()

            for pygameEvents in pygame.event.get():
                if pygameEvents.type == 9395 and self.manualEnd == False:
                    self.playMusic()

        self.appwindow.close()

    def playMusic(self):
        self.manualEnd = False
        self.stopMusic()
        i = randint(0, len(self.musicList) - 1)
        selectedMusic = self.musicList[f"music{str(i)}"]
        print(selectedMusic)
        mp3file = urllib.request.urlopen(selectedMusic[0])

        with open('./temp/test.mp3', 'wb+') as output:
            output.write(mp3file.read())

        self.appwindow["-MUSICTEXT-"].update(selectedMusic[1].replace("\\n", "\n").encode("latin1", "ignore").decode("utf-8"))

        pygame.init() # Initialize all imported pygame modules
        pygame.mixer.music.load("./temp/test.mp3") # Load an audio file into memory
        pygame.mixer.music.play() # Play the audio file in a loop (-1 means infinite loop)

    def stopMusic(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

        except:
            pass

credimusic_class = CredimusicMain()
credimusic_class.launch()