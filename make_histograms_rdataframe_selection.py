# Script to make histograms using rdataframe

import os, ROOT
from utils import labels, binnings, cuts, wps, tags
from array import array

import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--version', default='v17-6jets-BDT')
parser.add_argument('--region', default = 'inclusive')
parser.add_argument('--tag', default = '6tag')
parser.add_argument('--wp', default = 'loose')
parser.add_argument('--f_in', default = 'GluGluToHHHTo6B_SM')
parser.add_argument('--match', default='Inclusive')
parser.add_argument('--addBDT', action = 'store_true')

args = parser.parse_args()

ROOT.gROOT.SetBatch(ROOT.kTRUE)


ROOT.ROOT.EnableImplicitMT()



def add_bdt(df, xmlpath):
    #ROOT.gInterpreter.ProcessLine('''TMVA::Experimental::RReader model("{}");'''.format(xmlpath))
    #nvars = ROOT.model.GetVariableNames().size()
    #ROOT.gInterpreter.ProcessLine('''auto computeModel = TMVA::Experimental::Compute<{}, float>(model);'''.format(nvars))
    #l_expr = ROOT.model.GetVariableNames()
    #l_varn = ROOT.std.vector['std::string']()
    #for i_expr, expr in enumerate(l_expr):
    #    varname = 'v_{}'.format(i_expr)
    #    l_varn.push_back(varname)

    #    df=df.Define(varname, '(float)({})'.format(expr) )
    #reader = ROOT.TMVA.Reader()
    #l_varn = []
    #varnames= ["h_fit_mass","h1_t3_mass","h2_t3_mass","h3_t3_mass","h1_t3_dRjets","h2_t3_dRjets","h3_t3_dRjets","bcand1Pt","bcand2Pt","bcand3Pt","bca    nd4Pt","bcand5Pt","bcand6Pt", "bcand1Eta","bcand2Eta","bcand3Eta","bcand4Eta","bcand5Eta","bcand6Eta","bcand1Phi","bcand2Phi","bcand3Phi","bcand4Phi","bcand5Phi","bcand6Phi"]
    #vrs = []
    #for varname in varnames:
    #    l_varn.append(varname)
    #    vrs.append(array('f',[0]))
    #    reader.AddVariable(varname,vrs[-1])
    ROOT.gInterpreter.Declare('''
    float computeBDTScore(float& h_fit_mass,float& h1_t3_mass,float& h2_t3_mass,float& h3_t3_mass,float& h1_t3_dRjets,float& h2_t3_dRjets,float& h3_t3_dRjets,float& bcand1Pt,float& bcand2Pt,float& bcand3Pt,float& bcand4Pt,float& bcand5Pt,float& bcand6Pt,float& bcand1Eta,float& bcand2Eta,float& bcand3Eta,float& bcand4Eta,float& bcand5Eta,float& bcand6Eta,float& bcand1Phi,float& bcand2Phi,float& bcand3Phi,float& bcand4Phi,float& bcand5Phi,float& bcand6Phi){

    TMVA::Reader *reader = new TMVA::Reader( "!V:Color:Silent" );   
    reader->AddVariable("h_fit_mass",&h_fit_mass);
    reader->AddVariable("h1_t3_mass",&h1_t3_mass);
    reader->AddVariable("h2_t3_mass",&h2_t3_mass);
    reader->AddVariable("h3_t3_mass",&h3_t3_mass);
    reader->AddVariable("h1_t3_dRjets",&h1_t3_dRjets);
    reader->AddVariable("h2_t3_dRjets",&h2_t3_dRjets);
    reader->AddVariable("h3_t3_dRjets",&h3_t3_dRjets);
    reader->AddVariable("bcand1Pt",&bcand1Pt);
    reader->AddVariable("bcand2Pt",&bcand2Pt);
    reader->AddVariable("bcand3Pt",&bcand3Pt);
    reader->AddVariable("bcand4Pt",&bcand4Pt);
    reader->AddVariable("bcand5Pt",&bcand5Pt);
    reader->AddVariable("bcand6Pt",&bcand6Pt);
    reader->AddVariable("bcand1Eta",&bcand1Eta);
    reader->AddVariable("bcand2Eta",&bcand2Eta);
    reader->AddVariable("bcand3Eta",&bcand3Eta);
    reader->AddVariable("bcand4Eta",&bcand4Eta);
    reader->AddVariable("bcand5Eta",&bcand5Eta); 
    reader->AddVariable("bcand6Eta",&bcand6Eta);
    reader->AddVariable("bcand1Phi",&bcand1Phi);
    reader->AddVariable("bcand2Phi",&bcand2Phi);
    reader->AddVariable("bcand3Phi",&bcand3Phi);
    reader->AddVariable("bcand4Phi",&bcand4Phi);
    reader->AddVariable("bcand5Phi",&bcand5Phi);
    reader->AddVariable("bcand6Phi",&bcand6Phi);

    reader->BookMVA("BDT","/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_11_1_0_pre5_PY3/src/hhh-bdt/dataset/weights/TMVAClassification_BDT.weights.xml");

    return reader->EvaluateMVA("BDT");
    
    }
    ''')
                                                             
    df = df.Define('BDT', "computeBDTScore( h_fit_mass, h1_t3_mass, h2_t3_mass, h3_t3_mass, h1_t3_dRjets, h2_t3_dRjets, h3_t3_dRjets, bcand1Pt, bcand2Pt, bcand3Pt, bcand4Pt,bcand5Pt, bcand6Pt, bcand1Eta, bcand2Eta, bcand3Eta, bcand4Eta, bcand5Eta, bcand6Eta, bcand1Phi, bcand2Phi, bcand3Phi, bcand4Phi, bcand5Phi, bcand6Phi)")
    return df


version = args.version
path = '/isilon/data/users/mstamenk/eos-triple-h/samples-%s-nanoaod/'%version
#f_in = 'GluGluToHHHTo6B_SM'
f_in = args.f_in

df = ROOT.ROOT.RDataFrame('Events', path+'/' + f_in + '.root')

lumi = 41480.0


wp = args.wp
tag = args.tag
region = args.region
typename = 'v17-6jets-BDT'

out_path = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_11_1_0_pre5_PY3/src/plottting/histo-root-%s-%s-%s-%s-wp-%s'%(typename,version,region,wp,tag)
if not os.path.isdir(out_path):
    os.mkdir(out_path)

mva_training_samples = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_11_1_0_pre5_PY3/src/hhh-bdt/samples-%s-%s-%s-%s-wp-%s'%(typename,version,region,wp,tag)
if not os.path.isdir(mva_training_samples):
    os.mkdir(mva_training_samples)

cutMatch = '1'
append = ''

if args.match == 'H1':
    cutMatch = 'h1_t3_match == 1'
    append = '_H1Matched'
elif args.match == 'H2':
    cutMatch = 'h2_t3_match == 1'
    append = '_H2Matched'
elif args.match == 'H3':
    cutMatch = 'h3_t3_match == 1'
    append = '_H3Matched'



f_out = ROOT.TFile(out_path + '/' + 'histograms_%s.root'%(f_in+append), 'recreate')
print("Writing in %s"%(out_path + '/' + 'histograms_%s.root'%(f_in+append)))


if tag == '0ptag':
    cutTag = '1'
else:
    cutTag = tags[tag]%(wps[wp], wps[wp], wps[wp], wps[wp], wps[wp], wps[wp])
cutRegion = cuts[region]

if 'JetHT' in f_in:
    cutWeight = '1'
else:
    cutWeight = '(%f * weight * xsecWeight * l1PreFiringWeight * puWeight * genWeight)'%(lumi)

cutHLT = "(HLT_PFJet450 || HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550 || HLT_AK8PFJet360_TrimMass30 || HLT_AK8PFJet380_TrimMass30 || HLT_AK8PFJet400_TrimMass30 || HLT_AK8PFHT800_TrimMass50 || HLT_AK8PFHT750_TrimMass50 || HLT_AK8PFJet330_PFAK8BTagCSV_p17 || HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0)"
#cutHLT = "(HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550 || HLT_AK8PFJet360_TrimMass30 || HLT_AK8PFJet380_TrimMass30 || HLT_AK8PFJet400_TrimMass30 || HLT_AK8PFHT800_TrimMass50 || HLT_AK8PFHT750_TrimMass50 || HLT_AK8PFJet330_PFAK8BTagCSV_p17 || HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0)"
#cutHLT = "(HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550 )"
#cutHLT = "(HLT_PFJet500)"

cutJets = '(bcand1Pt > 20 && TMath::Abs(bcand1Eta) < 2.5) && (bcand2Pt > 20 && TMath::Abs(bcand2Eta) < 2.5) && (bcand3Pt > 20 && TMath::Abs(bcand3Eta) < 2.5) && (bcand4Pt > 20 && TMath::Abs(bcand4Eta) < 2.5) && (bcand5Pt > 20 && TMath::Abs(bcand5Eta) < 2.5) && (bcand6Pt > 20 && TMath::Abs(bcand6Eta) < 2.5)'

cutSignalJets = '(bcand1Pt > 40 && bcand3Pt > 40 && bcand5Pt > 40)'
cutHiggsPt = '(h1_t3_pt < 300 && h2_t3_pt < 300 && h3_t3_pt < 300)'


#cut = '(%s) && (%s) && (%s) && (%s)'%(cutHLT, cutRegion, cutTag, cutJets)


#print(cutWeight)
#print(cut)

histograms = []
variables = df.GetColumnNames()
variables = [v for v in labels if 'h_fit_mass' not in v and 'match' not in v and 'Match' not in v]
print(variables)

df_hlt = df.Filter(cutHLT, "Pass HLT trigger")
df_jets = df_hlt.Filter(cutJets, "Pt and Eta cuts on b-candidates")
df_region = df_jets.Filter(cutRegion, "Pass region cut")
df_tags = df_region.Filter(cutTag, "Pass b-tagging")
df_signalJets = df_tags.Filter(cutSignalJets,"Pass leading jet pT > 40")
df = df_signalJets.Filter(cutMatch, "Pass Higgs matching (none for bkg)")
#df = df_signalJets.Filter(cutHiggsPt,"Pass H1 pT, H2 pT, H3 pT < 300")

if args.addBDT:
    xml = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_11_1_0_pre5_PY3/src/hhh-bdt/dataset/weights/TMVAClassification_BDT.weights.xml'
    df = add_bdt(df,xml)
    variables.append('bdt')


report = df.Report()

binning = binnings['h_fit_mass'].replace('(','').replace(')','').split(',')
bins = int(binning[0])
xmin = float(binning[1])
xmax = float(binning[2])

df = df.Define('hhh_t3_pt','h1_t3_pt + h2_t3_pt + h3_t3_pt')
df = df.Define('eventWeight',cutWeight)
h = df.Histo1D(('h_fit_mass','h_fit_mass',bins,xmin,xmax),"h_fit_mass", 'eventWeight')
h.SetTitle('h_fit_mass')
h.SetName('h_fit_mass')

histograms.append(h)
for var in variables:
    binning = binnings[var].replace('(','').replace(')','').split(',')
    bins = int(binning[0])
    xmin = float(binning[1])
    xmax = float(binning[2])
    h_tmp = df.Histo1D((var,var,bins,xmin,xmax),var, 'eventWeight')
    h_tmp.SetTitle('%s'%(var))
    h_tmp.SetName('%s'%(var))
    histograms.append(h_tmp)
h.Draw()

report.Print()


f_out.cd()
for h in histograms:
    h.Write()
f_out.Close()

df.Snapshot('Events', mva_training_samples + '/' + f_in + '.root')
