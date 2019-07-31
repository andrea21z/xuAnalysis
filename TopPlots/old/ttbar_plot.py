from plotter.TopHistoReader import TopHistoReader, StackPlot, Process, WeightReader
from plotter.CrossSection import CrossSection
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet

### Input and output
path = '/pool/ciencias/userstorage/juanr/top/2016/forthesis/'
outpath = '~/www/temp/'

### Definition of the processes
process = {
'VV+t#bar{t}V'  : 'WW,WZ,ZZ,TTWToLNu,TTWToQQ,TTZToLLNuNu,TTZToQQ',
'Nonprompt': 'WJetsToLNu_MLM,TTbar_Powheg_Semilep',
'DY'  : 'DYJetsToLL_M10to50_aMCatNLO,DYJetsToLL_M50_aMCatNLO',
'Other': 'WW,WZ,ZZ,TTWToLNu,TTWToQQ,TTZToLLNuNu,TTZToQQ,WJetsToLNu_MLM,TTbar_Powheg_Semilep,DYJetsToLL_M10to50_aMCatNLO,DYJetsToLL_M50_aMCatNLO',
#'Other': 'WW,WZ,ZZ,TTWToLNu,TTWToQQ,TTZToLLNuNu,TTZToQQ,WJetsToLNu_MLM,TTbar_Powheg_Semilep,TW,TbarW',
'tW'  : 'TW,TbarW',
't#bar{t}'  : 'TTbar_Powheg',
'data': 'DoubleMuon,MuonEG,DoubleEG,SingleElec,SingleMuon'}
prk = ['VV+t#bar{t}V', 'Nonprompt', 'DY', 'tW','t#bar{t}']
#prk = ['Other','DY','t#bar{t}']
prk = ['Other','tW','t#bar{t}']

### Definition of colors for the processes
colors ={
'VV+t#bar{t}V'  : kOrange+1,
'Nonprompt': kGray+2,
'tW'  : kViolet-5,#kOrange+1,
'DY'  : kAzure-8,
't#bar{t}'  : kRed+1,
'Other' : kSpring-2,
'data': 1}

######################################################################################
### Plots
def DrawStack(out, *listOfPlots):
  ''' Draw some stack plots 
      Example:
      DrawStack(['NJets_ElMu_dilepton', 'Jet multiplicity'], ['DYMass_MuMu_dilepton', 'M_{#mu#mu}'])
  '''
  s = StackPlot(path)
  s.SetHistoPadMargins(right = 0.03)
  s.SetRatioPadMargins(right = 0.03)
  s.SetYtitle(offset = 0.6)
  s.SetXtitle(offset = 1.1)
  s.SetVerbose(1)
  s.SetOutPath(out)
  s.SetLumi(35850)
  s.doSetLogY = False
  s.doSystInLeg = True
  s.SetHistoName(listOfPlots[0][0])
  s.SetTextLumi(texlumi = '%2.1f fb^{-1} (13 TeV)', texlumiX = 0.69, texlumiY = 0.97, texlumiS = 0.05, doinvfb = True)
  s.SetTextCMS(cmstex = 'CMS', x = 0.13, y = 0.90, s = 0.05) # 0.18, y = 0.89
  s.SetTextCMSmode('', x = 0.225, y = 0.895, s = 0.042)
  #s.AddTex('#mu^{#pm}#mu^{#mp}', x = 0.19, y = 0.96, s = 0.04)
  s.SetRatioMin(0.5); s.SetRatioMax(1.5);
  s.SetStackOverflow(0)
  s.SetYratioTitle('Data/Pred')
  for pr in prk: s.AddProcess(pr, process[pr], colors[pr])

  # Uncertianties
  s.AddData(process['data'])
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_fsrDown', 'fsrDown')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_fsrUp',   'fsrUp')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_isrDown', 'isrDown')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_isrUp',   'isrUp')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_ueDown', 'ueDown')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_ueUp',   'ueUp')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_hdampUp', 'hdampUp')
  s.AddSystematic('t#bar{t}', 'TTbar_Powheg_hdampDown', 'hdampDown')
  s.AddToSyst('ElecEffUp, ElecEffDown, MuonEffUp,MuonEffDown,PUUp, PUDown')#,JESUp,JESDown,JERUp,TrigUp, TrigDown,BtagUp,BtagDown,MistagUp,MistagDown')
  for p in listOfPlots:
    if not isinstance(p, list): p = [p]

    lp = p[0].split('_')
    pname = lp[1]
    pch   = lp[2]
    plev  = lp[3]
    tch = ''
    if   pch == 'Elec' : tch = 'e^{+}e^{-}'
    elif pch == 'Muon' : tch = '#mu^{+}#mu^{-}'
    else               : tch = 'e^{#pm}#mu^{#mp}'
    if  plev == '1btag': tch += ', #geq 2 jet, #geq 1 b tag'
    s.Tex = []
    s.AddTex(tch, x = 0.19, y = 0.965, s = 0.05)
    if pch == 'ElMu': s.SetRatioMin(0.6); s.SetRatioMax(1.4);
    if pname == 'Lep0Pt' or pname == 'Lep1Pt':
      s.SetLegendPos(0.45, 0.3, 0.9, 0.88, size = 0.08, ncol = 1)
      if pch == 'ElMu' and pname == 'Lep0Pt':  s.SetLegendPos(0.62, 0.32, 0.9, 0.88, size = 0.06, ncol = 1)
    elif pname == 'Lep0Eta' or pname == 'Lep1Eta':
      if   pch == 'Elec': s.SetPlotMaxScale(1.4)
      elif pch == 'Muon': s.SetPlotMaxScale(1.4)
      s.SetLegendPos(0.35, 0.72, 0.9, 0.88, size = 0.06, ncol = 2)
      if pch == 'ElMu': 
        s.SetLegendPos(0.62, 0.45, 0.9, 0.88, size = 0.05, ncol = 1)
        s.SetPlotMaxScale(1.25)
    elif pname == 'InvMass2':
      s.SetPlotMaxScale(1.15)
      s.SetLegendPos(0.69, 0.3, 0.88, 0.82, size = 0.05, ncol = 1)
    elif pname == 'InvMass':
      s.SetStackOverflow(0)
      s.SetPlotMaxScale(1.15)
      s.SetLegendPos(0.69, 0.4, 0.88, 0.88, size = 0.05, ncol = 1)
    elif pname == 'Jet0Eta' or pname == 'Jet1Eta':
      s.SetPlotMaxScale(1.15)
      s.SetLegendPos(0.66, 0.53, 0.88, 0.88, size = 0.05, ncol = 1)
    elif pname == 'Jet0Pt' or pname == 'Jet1Pt':
      s.SetPlotMaxScale(1.15)
      s.SetLegendPos(0.62, 0.3, 0.88, 0.88, size = 0.05, ncol = 1) 
    elif pname == 'NJets':
      s.SetLegendPos(0.66, 0.3, 0.88, 0.88, size = 0.05, ncol = 1)
      if not pch == "ElMu": 
        s.SetLegendPos(0.71, 0.5, 0.88, 0.88, size = 0.05, ncol = 1)
        s.doSetLogY = True
        s.SetPlotMaxScale(4)
    elif pname == 'NBtagJets':
      s.SetLegendPos(0.66, 0.35, 0.88, 0.88, size = 0.055, ncol = 1)
    elif pname == 'NBtagsNJets':
      s.SetLegendPos(0.66, 0.25, 0.88, 0.88, size = 0.06, ncol = 1)
      

    s.DrawStack(p[0], p[1] if len(p) >= 2 else '', p[2] if len(p) >= 3 else '', p[3] if len(p) >= 4 else 1)



def GetName(var, chan, lev):
  return 'H_' + var + '_' + chan + '_' + lev

#######################################################################################
outpath = '/nfs/fanae/user/juanr/www/forThesis/'
lev = 'dilepton'
#for ch in ['Muon', 'Elec']
'''
DrawStack(outpath+'SFdilep/',
  [GetName('Lep0Pt' ,'Elec',lev),  'Leading electron p_{T} (GeV)','Events / 10 GeV',100],
  [GetName('Lep0Pt' ,'Muon',lev),  'Leading muon p_{T} (GeV)','Events / 10 GeV',100],
  [GetName('Lep0Eta','Elec',lev),  'Leading electron |#eta|', 'Events',1],
  [GetName('Lep0Eta','Muon',lev),  'Leading muon |#eta|',     'Events',1],
  [GetName('InvMass2','Elec',lev),  'm_{ee} (GeV)',       'Events / 0.2 GeV',2],
  [GetName('InvMass2','Muon',lev),  'm_{#mu#mu} (GeV)',   'Events / 0.2 GeV',2],
  [GetName('NJets',   'Elec',lev),  'Jet multiplicity',   'Events',1],
  [GetName('NJets',   'Muon',lev),  'Jet multiplicity',   'Events',1],
  )
'''
lev = '1btag'
ch = 'ElMu'
DrawStack(outpath,
  [GetName('Lep0Pt' , ch,lev),  'Leading lepton p_{T} (GeV)','Events / 10 GeV',100],
  [GetName('Lep0Eta', ch,lev),  'Leading lepton |#eta|', 'Events',1],
  [GetName('Lep1Pt' , ch,lev),  'Subeading lepton p_{T} (GeV)','Events / 10 GeV',100],
  [GetName('Lep1Eta', ch,lev),  'Subeading lepton |#eta|', 'Events',1],
  [GetName('Jet0Pt'  ,ch,lev),  'Leading jet p_{T} (GeV)',    'Events / 10 GeV',100],
  [GetName('InvMass', ch,lev),  'm_{e#mu} (GeV)',       'Events / 5 GeV',5],
  [GetName('Jet0Pt'  ,ch,lev),  'Leading jet p_{T} (GeV)',    'Events / 10 GeV',100],
  [GetName('Jet1Pt'  ,ch,lev),  'Subleading jet p_{T} (GeV)', 'Events / 10 GeV',100],
  [GetName('Jet0Eta' ,ch,lev),  'Leading jet |#eta|',         'Events',2],
  [GetName('Jet1Eta' ,ch,lev),  'Subleading jet |#eta|',      'Events',2],
  [GetName('HT'      ,ch,lev),  'H_{T} (GeV)',  'Events',100],
  )
'''
DrawStack(outpath, 
  [GetName('NJets', 'ElMu','dilepton'),  'Jet multiplicity', 'Events',1],
  [GetName('NBtagJets', 'ElMu','dilepton'),  'b tag multiplicity', 'Events',1],
  [GetName('NBtagsNJets', 'ElMu','dilepton'),  'Jet and b tag multiplicity', 'Events',1])
'''
