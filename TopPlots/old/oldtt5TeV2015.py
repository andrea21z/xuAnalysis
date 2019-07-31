from plotter.TopHistoReader import TopHistoReader, StackPlot, Process, WeightReader
from plotter.DrellYanDataDriven import DYDD
from plotter.NonpromptDataDriven import NonpromptDD
from plotter.CrossSection import CrossSection
from ROOT.TMath import Sqrt as sqrt
from ROOT import *

### Input and output
path = '/nfs/fanae/user/juanr/TOP13TeV/Trees5TeV/jul28/'
outpath = './outputs/'

### Definition of the processes
process = {
'WW+WZ'  : 'WW,WZ',
'Nonprompt': 'TTbar_PowhegSemi, WJetsToLNu_aMCatNLO',
'tW'  : 'WW,  TbarW',
'DY'  : 'DYJetsToLL_M50_aMCatNLO,DYJetsToLL_M10to50_aMCatNLO',
't#bar{t}'  : 'TTbar_Powheg',
'data': 'Data_SingleMu'}
prk = ['WW+WZ', 'Nonprompt', 'tW', 'DY', 't#bar{t}']


#TTbar_Powheg_ScaleDown
#TTbar_Powheg_ScaleUp
#TTbar_Powheg_Herwig


### Definition of colors for the processes
colors ={
'WW+WZ'  : kTeal+5,
'Nonprompt': kGray+2,
'tW'  : kOrange+1,
'DY'  : kAzure+2,
't#bar{t}'  : kRed+1,
'data': 1}

######################################################################################
### Plots
def DrawStack(out, *listOfPlots):
  ''' Draw some stack plots 
      Example:
      DrawStack(['NJets_ElMu_dilepton', 'Jet multiplicity'], ['DYMass_MuMu_dilepton', 'M_{#mu#mu}'])
  '''
  s = StackPlot(path)
  s.SetVerbose(1)
  s.SetOutPath(out)
  s.SetLumi(27.4)
  for pr in prk: s.AddProcess(pr, process[pr], colors[pr])
  s.AddData(process['data'])
  s.AddToSyst('BtagUp, BtagDown, ElecUp, ElecDown, MuonUp, MuonDown, JESUp, JESDown, JER, PUUp, PUDown, MisTagUp, MisTagDown')
  s.SetRatioMin(0.); s.SetRatioMax(2.)
  for p in listOfPlots:
    if not isinstance(p, list): p = [p]
    s.DrawStack(p[0], p[1] if len(p) >= 2 else '', p[2] if len(p) >= 3 else '', p[3] if len(p) >= 4 else 1)

def GetName(var, chan, lev):
  return var + '_' + chan + '_' + lev

levels   = ['dilepton', 'MET','2jets']
channels = ['ElMu','ElEl', 'MuMu']
# Plots
DrawStack(outpath, 
['H_NJets_ElMu_dilepton', 'Jet multiplicity', 'Events', 1], 
['H_HT_ElMu_dilepton'],
['H_InvMass_ElMu_2jets'],
['H_DiLepPt_ElMu_2jets'])
