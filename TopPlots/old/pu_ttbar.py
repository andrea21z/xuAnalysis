from plotter.TopHistoReader import TopHistoReader, CompPlot, Process, WeightReader
from plotter.CrossSection import CrossSection
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet

### Input and output

### Definition of the processes
process = {
't#bar{t} - PU reweighted'  : 'TTbar_Powheg',
't#bar{t} - no PU reweighted'  : 'TTbar_Powheg_noPUreweight',
'data': 'DoubleMuon,MuonEG,DoubleEG,SingleElec,SingleMuon'}

######################################################################################
### Plots

path = '/pool/ciencias/userstorage/juanr/top/2016/forthesis/'
outpath = '/nfs/fanae/user/juanr/www/forThesis/PUreweight/'
s = CompPlot(outpath, 'puWeights', doRatio = False, doNorm = True)
s.SetHistoPadMargins(right = 0.03)
s.SetHistoPadMargins(top = 0.06)
s.SetYtitle("Number of events (normalized)", size = 0.05, offset = 0.75)
s.SetVerbose(1)
s.SetLumi(35850)
s.doSetLogY = False
s.doSystInLeg = True
s.doRatio = False
s.SetTextLumi(texlumi = '%2.1f fb^{-1} (13 TeV)', texlumiX = 0.69, texlumiY = 0.97, texlumiS = 0.05, doinvfb = True)
s.SetTextCMS(cmstex = 'CMS', x = 0.13, y = 0.90, s = 0.05) # 0.18, y = 0.89
s.SetTextCMSmode('', x = 0.225, y = 0.895, s = 0.042)
s.AddTex('e^{#pm}#mu^{#mp}', x = 0.24, y = 0.965, s = 0.05)
s.SetLegendPos(x0 = 0.55, y0 = 0.55, x1 = 0.90, y1 = 0.91, size = 0.05, ncol = 1)

lev = 'dilepton'
ch = 'ElMu'
hname = 'H_Vtx_'+ch+'_'+lev
t = TopHistoReader(path)
t.SetFileNamePrefix('Tree_')
t.doNormalize = True
htt   = t.GetNamedHisto(hname, process['t#bar{t} - PU reweighted'])
hnoPU = t.GetNamedHisto(hname, process['t#bar{t} - no PU reweighted'])
t.isData = True
hdata = t.GetNamedHisto(hname, process['data'])
#s.SetHistoPad(0.1, 0.1, 1, 1)
s.SetXtitle(tit = 'Reconstructed vertices', size = 0.06, offset = 0.8, nDiv = 510, labSize = 0.045)

hdata.SetMarkerStyle(20)
hdata.SetMarkerSize(2.1)
hdata.SetMarkerColor(1)
hdata.SetLineStyle(0)
htt.SetLineWidth(3)
htt.SetLineColor(kAzure+2)
hnoPU.SetLineWidth(3)
hnoPU.SetLineColor(kRed+1)
hnoPU.SetLineStyle(2)
s.AddHisto(hdata, 'pe',   '', 'Data')
s.AddHisto(hnoPU, 'hist', '', 't#bar{t}, no PU reweighted')
s.AddHisto(htt,   'hist', '', 't#bar{t}, PU reweighted')
s.Draw()

print 'cp /nfs/fanae/user/juanr/www/forThesis/PUreweight/puWeights.pdf /home/juanr/cernbox/thesis/thesis/inputs/ttxsec/figures/'
