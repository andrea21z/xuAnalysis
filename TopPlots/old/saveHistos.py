from plotter.TopHistoReader import StackPlot,HistoSaver,TopHistoReader,WeightReader
from plotter.DrellYanDataDriven import DYDD
from plotter.NonpromptDataDriven import NonpromptDD
from plotter.CrossSection import CrossSection
from ROOT.TMath import Sqrt as sqrt
from ROOT import *

### Input and output
path = './tWhistos_jets20GeV/'#'./tWhistos_jets25GeV/'
outpath = './outputs/'

### Definition of the processes
process = {
'VV'  : 'WZTo3LNU,WWTo2L2Nu',
'fake': 'WJetsToLNu,TTsemilep',
'DY'  : 'DYJetsToLL_M_10to50,DYJetsToLL_MLL50',
'tt'  : 'TT',
'tW'  : 'tW_noFullHad,  tbarW_noFullHad'}
datafiles = 'HighEGJet,SingleMuon, DoubleMuon'
prk = ['VV', 'fake', 'DY', 'tt', 'tW']

colors ={
'VV'  : kTeal+5,
'fake': kGray+2,
'tW'  : kOrange+1,
'DY'  : kAzure+2,
'tt'  : kRed+1,
'data': 1}

def DrawStack(out, *listOfPlots):
  ''' Draw some stack plots 
      Example:
      DrawStack(['NJets_ElMu_dilepton', 'Jet multiplicity'], ['DYMass_MuMu_dilepton', 'M_{#mu#mu}'])
  '''
  s = StackPlot(path)
  s.SetVerbose(1)
  s.SetOutPath(out)
  s.SetLumi(296.08)
  for pr in prk: s.AddProcess(pr, process[pr], colors[pr])
  #s.AddData(datafiles)
  s.AddToSyst('ElecEffUp, ElecEffDown, MuonEffUp,MuonEffDown')
  s.SetRatioMin(0.0); s.SetRatioMax(2.0)
  s.SetPlotMaxScale(1.25)
  s.SetLegendPos(0.45, 0.82, 0.9, 0.9,0.055, 5) 
  s.SetLogY(0)
  s.SetBinLabels(['1,1','2,1','2,2'])
  for p in listOfPlots:
    if not isinstance(p, list): p = [p]
    s.DrawStack(p[0], p[1] if len(p) >= 2 else '', p[2] if len(p) >= 3 else '', p[3] if len(p) >= 4 else 1)

def GetName(var, chan, lev):
  return var + '_' + chan + '_' + lev


def GetPDFhisto(chan, level, direc = 'Up', syst = 'PDF', hname = 'tWNBtagNJets', sampleName = 'TT'):
  t = TopHistoReader(path)
  h = t.GetNamedHisto(hname + '_' + chan + '_' + level, sampleName)
  w = WeightReader(path, '',chan, level)
  w.SetSampleName('TT')
  if syst == 'PDF' or syst == 'pdf':
    for i in range(3):
      w.SetPDFhistoName('PDFweights_%i'%i)
      w.SetScaleHistoName('ScaleWeights_%i'%i)
      e = w.GetPDFandAlphaSunc() if (syst == 'PDF' or syst == 'pdf') else w.SetScaleHistoName('')
      y = h.GetBinContent(i+1)
      u = y*(1+e) if (direc == 'Up' or direc == 'UP' or direc == 'up') else y*(1-e)
      h.SetBinContent(i+1, u)
  return h

for chan in ['ElEl', 'MuMu', 'ElMu']:
 hs = HistoSaver(path)
 lev = 'dilepton' if chan == 'ElMu' else 'MET'
 hs.SetHistoName('tWNBtagNJets_'+chan+ '_' + lev)
 hs.SetOutputDir('tW5TeV')
 hs.SetOutName('tWdist_'+chan)
 hs.AddProcess(process)
 hs.AddData(datafiles)
 hs.AddSystematic('MuonEff', 'ElecEff', 'JER','JES', 'PU')
 hs.LoadHisto("TT_hdampUP","tt_hdampUp")
 hs.LoadHisto("TT_hdampDOWN","tt_hdampDown")
 hs.LoadHisto("TT_TuneCP5up","tt_ueUp")
 hs.LoadHisto("TT_TuneCP5down","tt_ueDown")
 hs.AddHisto(GetPDFhisto(chan, lev, 'Up', 'PDF'), 'tt_pdfUp')
 hs.AddHisto(GetPDFhisto(chan, lev, 'Do', 'PDF'), 'tt_pdfDown')
 hs.AddHisto(GetPDFhisto(chan, lev, 'Up', 'ME' ), 'tt_scaleUp')
 hs.AddHisto(GetPDFhisto(chan, lev, 'Do', 'ME' ), 'tt_scaleDown')
 hs.ReadHistos()
 hs.Write()

DrawStack('./tW5TeV/',['tWNBtagNJets_ElMu_dilepton','Jet/Btag bins e#mu'],['tWNBtagNJets_ElEl_MET', 'Jet/Btag bins ee'], ['tWNBtagNJets_MuMu_MET', 'Jet/Btag bins #mu#mu'])
