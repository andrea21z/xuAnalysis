from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)

from ttxsec.DrellYanDataDriven import DYDD
from ttxsec.NonpromptDataDriven import NonpromptDD
from ttxsec.CrossSection import CrossSection
from framework.functions import GetLumi
year=2016
process = processDic

outpath='/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver5/xsec/'%year

DYsamples   = processDic[year]['DY']
datasamples = processDic[year]['data']
def xsec(chan = 'ElMu', lev = '2jets', doDD = False):
  x = CrossSection(outpath, chan, lev)
  x.SetTextFormat("tex")
  bkg = []
  bkg.append(['tW',            process[year]['tW'],   0.30])
  if not doDD:
    bkg.append(['DY',            process[year]['DY'],   0.15])
    bkg.append(['Nonprompt lep', process[year]['Nonprompt'], 0.50])
  bkg.append(['VV',            process[year]['VV'],   0.30])
  signal   = ['tt',            process[year]['t#bar{t}']]
  data     = process[year]['data']
  expunc = "MuonEff, ElecEff, PU, Btag, Mistag, TrigEff" # JER
  modunc = "pdf, scale, isr, fsr"

  x.ReadHistos(path[year], chan, lev, bkg = bkg, signal = signal, data = data, expUnc = expunc, modUnc = modunc)
  x.SetLumi(GetLumi(year)*1000)
  x.SetLumiUnc(0.026)
  x.AddModUnc('Underlying Event','TT_TuneCUETP8M2T4down','TT_TuneCUETP8M2T4up')
  x.AddModUnc('hdamp','TT_hdampUp','TT_hdampDown')

  if doDD:
    d = DYDD(path,outpath,chan,lev, DYsamples=DYsamples, DataSamples=datasamples, lumi=Lumi, histonameprefix='', hname = 'DYHistoElMu')
    DYy, DYerr = d.GetDYDD()
    x.AddBkg('DYDD', DYy, 0, 0.15, DYerr)

    f = NonpromptDD(path, chan=chan, level=lev, process=processDic[year] , lumi=Lumi, histonameprefix='',yieldsSSname='YieldsSS')
    fy, fe = f.GetNonpromptDD(chan)
    x.AddBkg('Nonprompt lep', fy, 0, 0.30, fe)

  suf = '_'+chan+'_'+lev+'_'+('DD' if doDD else 'MC')
  x.PrintYields('Yields'+suf)
  x.PrintSystTable('Systematics'+suf)
  x.PrintXsec('CrossSection'+suf)

lev = '2jets'
xsec('ElMu',lev,1)
#xsec('MuMu',lev)
