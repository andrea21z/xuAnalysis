import os, sys
from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader, HistoManager
from plotter.Plotter import HistoComp
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from ROOT import TCanvas, gROOT
gROOT.SetBatch(1)


year=2018

systdic = {
 't#bar{t}': {
   'hdampUp'   : 'TTTo2L2Nu_hdampUp',
   'hdampDown' : 'TTTo2L2Nu_hdampDown',
   'TuneUp'    : 'TTTo2L2Nu_TuneCP5Up',
   'TuneDown'  : 'TTTo2L2Nu_TuneCP5Down'
   }
}
path = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver4/'%year
systematics = 'MuonEff, ElecEff, PU, Btag, Mistag, hdamp, Tune, Trig'
hm = HistoManager(['t#bar{t}'], systematics, '', path = path, processDic=processDic[year], lumi = GetLumi(year)*1000, systdic = systdic)

def DrawHisto(hname = 'H_NJets_ElMu_1btag', syst = 'ElecEff', systname = 'Electron Efficiency',  out = '',rebin = 1, Ymax='',ytit='Events', xtit = 'Jet Multiplicity'):
  hm.SetHisto(hname, rebin)
  #hm.SetRebin(rebin)
  histo    = hm.GetUncHist(syst, includeStat = True).Clone("nom")
  histoUnc = histo.Clone("syst")
  histo.SetFillStyle(0)
  histoUnc.SetFillStyle(1000)
  histoUnc.SetFillColorAlpha(kAzure+2, 0.5)
  histoUnc.SetLineWidth(0)
  hratio = hm.GetRatioHistoUnc(syst, includeStat = True)
  s = HistoComp(outpath = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver4/plots_syst/'%year, doNorm = False, doRatio = True)
  s.SetLumi(GetLumi(year))
  s.AddHisto(     histo,  'hist', '', 't#bar{t}')
  s.AddHisto(  histoUnc,  '', 'e2', systname)
  s.AddRatioHisto(hratio, 'e2')
  s.SetOutName(out)
  s.SetLegendPos(ncol = 1)
  s.SetPlotMaximum(Ymax)
  s.SetRatioMax(1.05)
  s.SetRatioMin(0.95)
  s.SetYratioTitle("Uncertainty")
  s.SetXtitle(xtit)
  s.SetYtitle(ytit)
  
  s.Draw()

DrawHisto('H_NJets_ElMu_dilepton', 'ElecEff', 'Electron efficiency', 'NJets_ElecEff_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'MuonEff', 'Muon efficiency', 'NJets_MuonEff_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'Trig', 'Trigger efficiency', 'NJets_Trig_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'PU', 'PU', 'NJets_PU_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'Btag', 'b-tagging efficiency', 'NJets_Btag_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'hdamp', 'hdamp', 'NJets_hdamp_dilepton')
DrawHisto('H_NJets_ElMu_dilepton', 'Tune', 'Tune', 'NJets_Tune_dilepton')

DrawHisto('H_MT2_ElMu_dilepton', 'ElecEff', 'Electron efficiency', 'MT2_ElecEff_dilepton', rebin = 50,ytit= 'Events / 5 GeV', xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'MuonEff', 'Muon efficiency', 'MT2_MuonEff_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'Trig', 'Trigger efficiency', 'MT2_Trig_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'PU', 'PU', 'MT2_PU_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'Btag', 'b-tagging efficiency', 'MT2_Btag_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'hdamp', 'hdamp', 'MT2_hdamp_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')
DrawHisto('H_MT2_ElMu_dilepton', 'Tune', 'Tune', 'MT2_Tune_dilepton',rebin=50, ytit= 'Events / 10 GeV',xtit ='MT2 (GeV)')




#DrawHisto('H_NJets_ElMu_dilepton', 'Tune', 'Tune', 'temp')
