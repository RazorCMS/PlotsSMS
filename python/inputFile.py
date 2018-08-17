import sys
import ROOT as rt

class inputFile():

    def __init__(self, fileName):
        self.HISTOGRAM = self.findHISTOGRAM(fileName)
        self.EXPECTED = self.findEXPECTED(fileName)
        self.EXPECTEDEXTRA = self.findEXPECTEDEXTRA(fileName)
        self.EXPECTED2 = self.findEXPECTED2(fileName)
        self.OBSERVED = self.findOBSERVED(fileName)
        self.OBSERVEDEXTRA = self.findOBSERVEDEXTRA(fileName) # hack for T2qq
        self.LUMI = self.findATTRIBUTE(fileName, "LUMI")
        self.ENERGY = self.findATTRIBUTE(fileName, "ENERGY")
        self.PRELIMINARY = self.findATTRIBUTE(fileName, "PRELIMINARY")
        self.BOXES = self.findATTRIBUTE(fileName, "BOXES")

    def findATTRIBUTE(self, fileName, attribute):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != attribute: continue
            fileIN.close()
            return tmpLINE[1]

    def findHISTOGRAM(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "HISTOGRAM": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])
            hist = rootFileIn.Get(tmpLINE[2])
            hist.SetDirectory(rt.gROOT)
            return {'histogram': hist}
            
    def findEXPECTED(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "EXPECTED": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])
            nominal = rootFileIn.Get(tmpLINE[2])
            plus = rootFileIn.Get(tmpLINE[3])
            minus = rootFileIn.Get(tmpLINE[4])
            return {'nominal': nominal,
                    'plus': plus,
                    'minus': minus,
                    'colorLine': tmpLINE[5],
                    'colorArea': tmpLINE[6]}

    def findEXPECTED2(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "EXPECTED2": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])            
            nominal = rootFileIn.Get(tmpLINE[2])
            plus2 = rootFileIn.Get(tmpLINE[3])
            minus2 = rootFileIn.Get(tmpLINE[4])
            return {'nominal': nominal,
                    'plus2': plus2,
                    'minus2': minus2,
                    'colorLine': tmpLINE[5],
                    'colorArea': tmpLINE[6]}
        
    def findOBSERVED(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "OBSERVED": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])
            nominal = rootFileIn.Get(tmpLINE[2])
            plus = rootFileIn.Get(tmpLINE[3])
            minus = rootFileIn.Get(tmpLINE[4])
            return {'nominal': nominal,
                    'plus': plus,
                    'minus': minus,
                    'colorLine': tmpLINE[5],
                    'colorArea': tmpLINE[6]}

    def findOBSERVEDEXTRA(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "OBSERVEDEXTRA": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])
            if not rootFileIn:
                return None
            nominal = rootFileIn.Get(tmpLINE[2])
            plus = rootFileIn.Get(tmpLINE[3])
            minus = rootFileIn.Get(tmpLINE[4])
            return {'nominal': nominal,
                    'plus': plus,
                    'minus': minus,
                    'colorLine': tmpLINE[5],
                    'colorArea': tmpLINE[6]}

    def findEXPECTEDEXTRA(self, fileName):
        fileIN = open(fileName)        
        for line in fileIN:
            tmpLINE =  line[:-1].split(" ")
            if tmpLINE[0] != "EXPECTEDEXTRA": continue
            fileIN.close()
            rootFileIn = rt.TFile.Open(tmpLINE[1])
            if not rootFileIn:
                return None
            nominal = rootFileIn.Get(tmpLINE[2])
            plus = rootFileIn.Get(tmpLINE[3])
            minus = rootFileIn.Get(tmpLINE[4])
            return {'nominal': nominal,
                    'plus': plus,
                    'minus': minus,
                    'colorLine': tmpLINE[5],
                    'colorArea': tmpLINE[6]}

