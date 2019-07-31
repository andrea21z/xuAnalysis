import os, sys
from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis/',1)[0]+'/xuAnalysis/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow, TCanvas, TLegend


######################################################################################
### Plots
def DrawStack(out, year, *listOfPlots):
  ''' Draw some stack plots 
      Example:
      DrawStack(path, year, ['NJets_ElMu_dilepton', 'Jet multiplicity'], ['DYMass_MuMu_dilepton', 'M_{#mu#mu}'])
  '''
  s = StackPlot(path[year])
  s.SetHistoPadMargins(right = 0.03)
  s.SetRatioPadMargins(right = 0.03)
  s.SetYtitle(offset = 0.6)
  s.SetXtitle(offset = 1.1)
  s.SetVerbose(1)
  s.SetOutPath(out)
  #s.SetLumi(GetLumi(2016)*1000)
  s.SetLumi(GetLumi(year)*1000)
  s.doSetLogY = False
  s.doSystInLeg = False
  s.doSystInLeg = True
  s.SetPlotMaxScale(1.5)
  s.SetHistoName(listOfPlots[0][0])
  s.SetTextLumi(texlumi = '%2.1f fb^{-1} (13 TeV)', texlumiX = 0.69, texlumiY = 0.97, texlumiS = 0.05, doinvfb = True)
  s.SetTextCMS(cmstex = 'CMS', x = 0.13, y = 0.90, s = 0.05) # 0.18, y = 0.89
  s.SetTextCMSmode('Preliminary', x = 0.225, y = 0.895, s = 0.042)
  s.SetTextChan(texch = 'Elec',lev='', x = 0.19, y = 0.96, s = 0.04)
  #s.AddTex('#mu^{#pm}#mu^{#mp}, #geq 2 jets', x = 0.19, y = 0.96, s = 0.04) #muon
  #s.AddTex('e^{#pm}#mu^{#mp}, #geq 2 jets', x = 0.19, y = 0.96, s = 0.04) #elmu
  #s.AddTex('e^{#pm}e^{#mp}, #geq 2 jets', x = 0.19, y = 0.96, s = 0.04) #elec
  s.SetRatioMin(0.8); s.SetRatioMax(1.2);
  s.SetStackOverflow(1)
  s.SetYratioTitle('Data/Pred')
  for pr in prk: s.AddProcess(pr, process[year][pr], colors[pr])
  s.AddData(process[year]['data'])

  
  for p in listOfPlots:
    if not isinstance(p, list): p = [p]
    s.DrawStack(p[0], p[1] if len(p) >= 2 else '', p[2] if len(p) >= 3 else '', p[3] if len(p) >= 4 else 1)


def GetName(var, chan, lev):
  return 'H_' + var + '_' + chan + '_' + lev

def GetAllCh(var, lev):
  #return [GetName(var,'eee',lev), GetName(var,'emm',lev), GetName(var,'mee',lev), GetName(var,'mmm',lev)]
  return [GetName(var,'Elec',lev), GetName(var,'Muon',lev), GetName(var,'ElMU',lev)]

#######################################################################################
outpath = '/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/probando/'
lev = 'dilepton' #'dilepton'
ch = 'ElMu'
year = 2016

#graficos para presentar
####ELMu
'''
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'ElMu','dilepton'),  'Number of jets',   'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'ElMu','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'ElMu','2jets'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'ElMu','2jets'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])

DrawStack(outpath+'/%i/'%year, year,
			['H_Yields_ElMu',  'Number of yields',   'Events',1])
'''
####Elec

'''
DrawStack(outpath, 2016,
			['H_Yields_Elec',  'Number of yields',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Elec_dilepton',  'mass',   'Events',1])
		
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Elec','dilepton'),  'Number of jets',   'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Elec','2jets'),  'Number of b jets',   'Events',1])
'''
####Muon
'''
DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Muon_dilepton',  'mass',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Muon','dilepton'),  'Number of jets',   'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Muon','2jets'),  'Number of b jets',   'Events',1])	

DrawStack(outpath,2016,
			['H_Yields_Muon',  'Number of yields',   'Events',1])

'''
'''		
DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Elec_dilepton',  'mass',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Muon_dilepton',  'mass',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Elec','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Muon','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'ElMu','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'ElMu','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Muon','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Elec','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'ElMu','2jets'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'ElMu','2jets'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath, year,
			['H_Yields_Muon',  'Number of yields',   'Events',1])
DrawStack(outpath, year,
			['H_Yields_Elec',  'Number of yields',   'Events',1])

DrawStack(outpath, year,
			['H_Yields_ElMu',  'Number of yields',   'Events',1])



DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Elec_dilepton',  'mass',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Muon_dilepton',  'mass',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Elec','dilepton'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'ElMu','dilepton'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Muon','1btag'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','ElMu','dilepton'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Elec','dilepton'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Muon','dilepton'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Muon','1btag'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'ElMu','dilepton'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Elec','dilepton'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','ElMu','dilepton'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Elec','dilepton'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Muon','dilepton'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'ElMu','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'ElMu','dilepton'),  'Number of b jets',   'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Muon','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Muon','dilepton'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Elec','dilepton'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Elec','dilepton'),  'Number of b jets',   'Events',1])


DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Elec','1btag'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'ElMu','1btag'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Muon','1btag'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'ElMu','1btag'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Elec','1btag'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Muon','1btag'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','ElMu','1btag'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Elec','1btag'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Muon','1btag'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','ElMu','1btag'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Elec','1btag'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Muon','1btag'),  'Leading jet |#eta|', 'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Elec_dilepton',  'mass',   'Events',1])

DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'ElMu','1btag'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'ElMu','1btag'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Muon','1btag'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Muon','1btag'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Elec','1btag'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Elec','1btag'),  'Number of b jets',   'Events',1])
			
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Elec','2jets'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'ElMu','2jets'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Pt' ,'Muon','2jets'),  'Leading jet p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'ElMu','2jets'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Elec','2jets'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Pt' ,'Muon','2jets'),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','ElMu','2jets'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Elec','2jets'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Lep0Eta','Muon','2jets'),  'Leading lepton |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','ElMu','2jets'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Elec','2jets'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('Jet0Eta','Muon','2jets'),  'Leading jet |#eta|', 'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'ElMu','2jets'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'ElMu','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Muon','2jets'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Muon','2jets'),  'Number of b jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NJets',   'Elec','2jets'),  'Number of jets',   'Events',1])
DrawStack(outpath+'/%i/'%year, year,
			[GetName('NBtagJets',   'Elec','2jets'),  'Number of b jets',   'Events',1])

'''

'''
for lev in ['1btag','dilepton','ZVeto','MET','2jets']:
	for ch in ['ElMu','Muon', 'Elec']:

		DrawStack(outpath+'/%i/'%year, year,
			['H_InvMass2_Elec_dilepton',  'yields',   'Events',1],
			['H_InvMass2_Muon_dilepton',  'yields',   'Events',1],
			[GetName('Lep0Pt' ,ch,lev),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100],
			[GetName('Lep0Eta',ch,lev),  'Leading lepton |#eta|', 'Events',1])
			[GetName('Jet0Pt' ,ch,lev),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100],
			[GetName('Jet0Eta',ch,lev),  'Leading lepton |#eta|', 'Events',1],
			#[GetName('MET',ch,lev),  'Leading lepton |#eta|', 'Events',1],
			#['H_Yields_ElMu',  'yields',   'Events',1],
			#['H_Yields_Elec',  'yields',   'Events',1],
			#['H_Yields_Muon',  'yields',   'Events',1],
			[GetName('NBtagJets',   ch,lev),  'Number of b jets',   'Events',1],
			[GetName('NJets',   ch,lev),  'Number of jets',   'Events',1],
			 #[GetName('InvMass', 'Muon',lev),  'm_{#mu#mu} (GeV)',   'Events',1],
			#[GetName('InvMass', 'Elec',lev),  'm_{ee} (GeV)',   'Events',1],
			#[GetName('InvMass', 'ElMu',lev),  'm_{e#mu} (GeV)',   'Events',1])


'''
'''
lev = 'met' #lep, met
ch  = ''
DrawStack(outpath, [GetAllCh('m3l', lev),  'm_{3l} (GeV)','Events / 10 GeV',10])
DrawStack(outpath, [GetAllCh('mtw', lev),  'm_{T}^{W} (GeV)',   'Events',6])
DrawStack(outpath, [GetAllCh('mz' , lev),  'm_{Z} (GeV)','Events / 10 GeV',10])
DrawStack(outpath, [GetAllCh('MET' , lev), 'p_{T}^{miss} (GeV)','Events / 10 GeV',1])

DrawStack(outpath, [GetAllCh('LepWPt' ,  lev), 'p_{T}(lepW) (GeV)','Events / 40 GeV',4])
DrawStack(outpath, [GetAllCh('LepWEta' , lev), '#eta (lepW)','Events',10])
DrawStack(outpath, [GetAllCh('LepWPhi' , lev), '#phi (lepW) (rad/#pi)','Events',5])
DrawStack(outpath, [GetAllCh('LepZ0Pt' ,  lev), 'p_{T}(lep0Z) (GeV)','Events / 40 GeV',4])
DrawStack(outpath, [GetAllCh('LepZ0Eta' , lev), '#eta (lep0Z)','Events',10])
DrawStack(outpath, [GetAllCh('LepZ0Phi' , lev), '#phi (lep0Z) (rad/#pi)','Events',5])
DrawStack(outpath, [GetAllCh('LepZ1Pt' ,  lev), 'p_{T}(lep1Z) (GeV)','Events / 40 GeV',4])
DrawStack(outpath, [GetAllCh('LepZ1Eta' , lev), '#eta (lep1Z)','Events',10])
DrawStack(outpath, [GetAllCh('LepZ1Phi' , lev), '#phi (lep1Z) (rad/#pi)','Events',5])
DrawStack(outpath, [GetAllCh('TrilepPt' , lev), 'Trilep p_{T} (GeV)','Events',8])
DrawStack(outpath, [GetAllCh('ZPt' ,      lev), 'Z p_{T} (GeV)','Events',8])
DrawStack(outpath, [GetAllCh('MaxDeltaPhi' , lev), 'max(#Delta#phi (ll)) (rad/#pi)','Events',2])
DrawStack(outpath, [GetAllCh('NJets' , lev), 'Jet multiplicity','Events',1])


'''
