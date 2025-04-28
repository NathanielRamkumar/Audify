import os
import time
import extractText
import speak
import playSound

class terminalGUI:
    def __init__(self):
        print("Welcome to Audify\n")
        print("Select an Option:\n[0] Scan PDF\n[1] View Audio File")
        x = int(input())
        print('')
        if not x:
            self.scanPdf()
        else:
            self.listenToFile()

    def scanPdf(self):
        print("Select PDF to Scan")
        self.showPdfFolder()
        x = int(input())
        print('')
        extractText.copyToTxt(self.pdfEntryList[x], self.pdfEntryList[x].replace('.pdf',''),1)
        speak.tts(self.pdfEntryList[x].replace('.pdf','.txt'),self.pdfEntryList[x].replace('.pdf','.mp3'))

        print("Select an Option:\n[0] Scan Another\n[1] View Audio File\n[2] Exit")
        x = int(input())
        if x == 0:
            self.scanPdf()
        elif x == 1:
            self.listenToFile()
        elif x == 2:
            os._exit()
    
    def listenToFile(self):
        print("Select Audio Book to Listen to:")
        self.showAudioFolder()
        x = int(input())
        print('')
        playSound.playMp3(self.mp3EntryList[x])

        
        
    def showPdfFolder(self):
        folder_path = f'{os.path.dirname(__file__)}/PDF Files'
        self.pdfEntryList = []
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    self.pdfEntryList.append(entry.name)
        for i in range(len(self.pdfEntryList)):
            print(f"[{i}] {self.pdfEntryList[i]}")

    
    def showTxtFolder(self):
        folder_path = f'{os.path.dirname(__file__)}/Txt Files'
        self.txtEntryList = []
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    self.txtEntryList.append(entry.name)
        for i in range(len(self.txtEntryList)):
            print(f"[{i}] {self.txtEntryList[i]}")

    def showAudioFolder(self):
        folder_path = f'{os.path.dirname(__file__)}/Audio Files'
        self.mp3EntryList = []
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    self.mp3EntryList.append(entry.name)
        for i in range(len(self.mp3EntryList)):
            print(f"[{i}] {self.mp3EntryList[i]}")


if __name__ == "__main__":
    x = terminalGUI()

