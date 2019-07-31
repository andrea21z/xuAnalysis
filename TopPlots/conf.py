import os, sys
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)
from framework.functions import GetLumi
from plotter.TopHistoReader import TopHistoReader
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow

### Input and output
path = {
  2016 : '/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2016_new/',#/nfs/fanae/user/juanr/test/PAFnanoAOD/temp2016/', #'/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2016/',
  2015 : '/pool/ciencias/userstorage/juanr/top/2016/nov15/',  #TOP-17-001
  2017 : '/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2017_new/', #'/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2017_PUSF2/',# '/nfs/fanae/user/juanr/legacy/PAFnanoAOD/histograms/2017',
  2018 : '/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2018_new/'#'/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2018_PUSF2/' #'/nfs/fanae/user/juanr/legacy/PAFnanoAOD/histograms/2018/',
}

### Definition of the processes
processDic = {
       2018 : {
          'VV'        : 'WZTo3LNu, WZTo2L2Q, WZTo1L3Nu, ZZTo2L2Q, ZZTo2L2Nu, ZZTo4L, ZZTo2Q2Nu,WWTo2L2Nu',
          'Nonprompt' : 'TTToSemiLeptonic, WJetsToLNu_MLM',
          'ttV'       : 'TTWJetsToLNu, TTWJetsToQQ, TTZToQQ, TTZToLL_M_1to10, TTZToLLNuNu_M_10_a',
          'DY'        : 'DYJetsToLL_M_10to50_MLM, DYJetsToLL_M_50_a',
          'tW'        : 'tW_noFullHad,tbarW_noFullHad',
          't#bar{t}'  : 'TTTo2L2Nu',
          'data'      : 'DoubleMuon_2018,SingleMuon_2018,EGamma_2018,MuonEG_2018',
          'VV + ttV'  : 'WZTo3LNu, WZTo2L2Q, WZTo1L3Nu, ZZTo2L2Q, ZZTo2L2Nu, ZZTo4L, ZZTo2Q2Nu,WWTo2L2Nu,TTWJetsToLNu, TTWJetsToQQ, TTZToQQ, TTZToLL_M_1to10, TTZToLLNuNu_M_10_a',
          },
        
        2017 : {
          'VV'        : 'WWTo2L2Nu,WZTo3LNu,WZTo2L2Q,ZZTo2L2Nu,ZZTo4L,ZZTo2L2Q,ZZTo2Q2Nu',
          'Nonprompt' : 'TTToSemiLeptonic,WJetsToLNu_MLM',
          'ttV'       : 'TTWJetsToLNu,TTZToLLNuNu_M_10_a,TTZToQQ,TTWJetsToQQ,TTZToLL_M_1to10',
          'DY'        : 'DYJetsToLL_M_50_a,DYJetsToLL_M_10to50_MLM',
          'tW'        : 'tbarW_noFullHad,tW_noFullHad',
          't#bar{t}'  : 'TTTo2L2Nu',
          'data'      : 'MuonEG_2017,DoubleMuon_2017,DoubleEG_2017,SingleElectron_2017,SingleMuon_2017',
          'VV + ttV'  : 'WWTo2L2Nu,WZTo3LNu,WZTo2L2Q,ZZTo2L2Nu,ZZTo4L,ZZTo2L2Q,TTWJetsToLNu,TTZToLLNuNu_M_10_a,TTZToQQ,TTWJetsToQQ,TTZToLL_M_1to10',
        },
		2016 : {
          
          #'VV'        : 'WZ,WW, ZZ',
          'VV'        : 'WWTo2L2Nu,WZTo3LNu,WZTo2L2Q,ZZTo2L2Nu,ZZTo4L,ZZTo2L2Q,ZZTo2Q2Nu', #andrea
          
          'Nonprompt' : 'TTToSemiLeptonic,WJetsToLNu_MLM',
		  
		  'ttV'       : 'TTZToLLNuNu_M_10_a,TTZToQQ,TTWJetsToQQ,TTWJetsToLNu,TTZToLL_M_1to10_MLM',
         
          'DY'        : 'DYJetsToLL_M_50_a,DYJetsToLL_M_10to50',
          
          'tW'        : 'tW_noFullHad,tbarW_noFullHad',
		  
		  't#bar{t}'  : 'TT',#'TTTo2L2Nu',
		  
		  'data'      : 'DoubleMuon_2016,DoubleEG_2016,MuonEG_2016, SingleMuon_2016,SingleElectron_2016',
		  'VV + ttV'  : 'TTZToLLNuNu_M_10_a,TTZToLL_M_1to10_MLM,TTZToQQ,WWTo2L2Nu,WZTo3LNu,WZTo2L2Q,ZZTo2L2Nu,ZZTo4L,ZZTo2L2Q,TTWJetsToQQ,TTWJetsToLNu'
		},
		2015 : {#paper
			'VV'        : 'WZ,WW, ZZ',#'WW',#,WW, ZZ',
			'Nonprompt' : 'TTbar_Powheg_Semilep,WJetsToLNu_MLM',
			'ttV'       : 'TTZToLLNuNu,TTWToLNu,TTZToQQ,TTWToQQ',
			'DY'        : 'DYJetsToLL_M50_aMCatNLO,DYJetsToLL_M10to50_aMCatNLO', 
			'tW'        : 'TW,TbarW', 
			't#bar{t}'  : 'TTbar_Powheg',
			'data'      : 'DoubleEG,MuonEG,SingleElec,SingleMuon,DoubleMuon'
			
		}
}
processes = ['VV + ttV', 'Nonprompt','DY', 'tW','t#bar{t}']
#processes= ['DY']

### Definition of colors for the processes
colors ={
'VV'        : kTeal+2,
'Nonprompt' : kGray+1,
'VV + ttV'  : kYellow-4,
'ttV'       : kYellow-4,
'DY'        : kAzure,
'tW'        : kOrange+1,
't#bar{t}'  : kRed+1,
'data': 1}

systematics='MuonEff, ElecEff, PU, Btag, Mistag'

def GetName(var, chan, lev):
  return 'H_' + var + '_' + chan + '_' + lev

def GetAllCh(var, lev):
  return [GetName(var,'eee',lev), GetName(var,'emm',lev), GetName(var,'mee',lev), GetName(var,'mmm',lev)]

