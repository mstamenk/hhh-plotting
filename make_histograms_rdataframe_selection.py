# Script to make histograms using rdataframe

import os, ROOT
from utils import labels, binnings, cuts, wps, tags, luminosities, hlt_paths
from array import array


# argument parser
import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--version', default='v21') # version of NanoNN production
parser.add_argument('--year', default='2017') # year
parser.add_argument('--region', default = 'inclusive') # region: nFJ0, nFJ1, nFJ2, inclsuive, nFJ1p(= 1+2+3 fatjets)
parser.add_argument('--tag', default = '0ptag') # n b-tags on AK4 jets using DeepJet
parser.add_argument('--wp', default = 'loose') # b-tagging working point: loose, medium, tight
parser.add_argument('--f_in', default = 'GluGluToHHHTo6B_SM') # input samples
parser.add_argument('--inputs_path', default = '/afs/cern.ch/work/m/mstamenk/public/forPKU/') # path of inputs after NanoNN
parser.add_argument('--outputs_path', help='Please specify output path for histograms / mva inputs location to be stored') # output path for histograms and mva inputs
parser.add_argument('--doMVAInputs', action = 'store_true') # store MVA inputs
parser.add_argument('--doHistograms', action = 'store_true') # store histograms

args = parser.parse_args()

# set batch to speed up the run
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()


# get inputs 
version = args.version
path = args.inputs_path + '/' + 'samples-%s-%s-nanoaod'%(version,args.year) + '/'
f_in = args.f_in

# data frame with all the events 
df = ROOT.ROOT.RDataFrame('Events', path+'/' + f_in + '.root')


lumi = luminosities[args.year]
wp = args.wp
tag = args.tag
region = args.region
typename = 'HLT-selection'

if args.doHistograms:
    print("Running doHistograms: preparing output folder")
    out_path = args.outputs_path + '/' + args.version + '/'  + 'histograms-%s-%s-%s-%s-wp-%s-%s'%(typename,version,region,wp,tag,args.year)
    print("Histograms will be saved at: " + out_path)
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    f_out = ROOT.TFile(out_path + '/' + 'histograms_%s.root'%(f_in), 'recreate')
    print("Writing in %s"%(out_path + '/' + 'histograms_%s.root'%(f_in)))

if args.doMVAInputs:
    mva_training_samples = args.outputs_path + '/' + args.version + '/' + 'mva-inputs-%s-%s-%s-%s-wp-%s-%s'%(typename,version,region,wp,tag,args.year)
    if not os.path.isdir(mva_training_samples):
        os.makedirs(mva_training_samples)

# Tagging selection
if tag == '0ptag':
    cutTag = tags[tag]
    wp = 'noWP'
else:
    cutTag = tags[tag]%(wps[wp], wps[wp], wps[wp], wps[wp], wps[wp], wps[wp])

cutRegion = cuts[region]

if 'JetHT' in f_in:
    cutWeight = '1'
else:
    cutWeight = '(%f * weight * xsecWeight * l1PreFiringWeight * puWeight * genWeight)'%(lumi)

# HLT selection
cutHLT = hlt_paths[args.year]

# cut jets pT and eta
cutJets = '(bcand1Pt > 20 && TMath::Abs(bcand1Eta) < 2.5) && (bcand2Pt > 20 && TMath::Abs(bcand2Eta) < 2.5) && (bcand3Pt > 20 && TMath::Abs(bcand3Eta) < 2.5) && (bcand4Pt > 20 && TMath::Abs(bcand4Eta) < 2.5) && (bcand5Pt > 20 && TMath::Abs(bcand5Eta) < 2.5) && (bcand6Pt > 20 && TMath::Abs(bcand6Eta) < 2.5)'
# AK4 selection on leading jet in Higgs pairs
cutSignalJets = '(bcand1Pt > 40 && bcand3Pt > 40 && bcand5Pt > 40)'


# Event selection
df_hlt = df.Filter(cutHLT, "Pass HLT trigger")
df_jets = df_hlt.Filter(cutJets, "Pt and Eta cuts on b-candidates")
df_region = df_jets.Filter(cutRegion, "Pass region cut")
df_tags = df_region.Filter(cutTag, "Pass b-tagging")
df = df_tags.Filter(cutSignalJets,"Pass leading jet pT > 40")

# Define new variables
df = df.Define('hhh_t3_pt','h1_t3_pt + h2_t3_pt + h3_t3_pt')
df = df.Define('eventWeight',cutWeight)

# Print report on event selection
report = df.Report()
report.Print()

if args.doMVAInputs:
    df.Snapshot('Events', mva_training_samples + '/' + f_in + '.root')

if args.doHistograms:
    # Define histograms to be produced
    histograms = []
    variables = df.GetColumnNames()
    variables = [v for v in labels if 'h_fit_mass' not in v and 'match' not in v and 'Match' not in v] # can be done better
    print("Will produce histograms for following variables:")
    print(variables)

    # Rdataframes require first histogram to be produced and then the rest is nested in the loop of the first one
    binning = binnings['h_fit_mass'].replace('(','').replace(')','').split(',')
    bins = int(binning[0])
    xmin = float(binning[1])
    xmax = float(binning[2])

    h = df.Histo1D(('h_fit_mass','h_fit_mass',bins,xmin,xmax),"h_fit_mass", 'eventWeight') # booking the rdataframe loop
    h.SetTitle('h_fit_mass')
    h.SetName('h_fit_mass')

    histograms.append(h)
    for var in variables: # booking all variables to be produced
        binning = binnings[var].replace('(','').replace(')','').split(',')
        bins = int(binning[0])
        xmin = float(binning[1])
        xmax = float(binning[2])
        h_tmp = df.Histo1D((var,var,bins,xmin,xmax),var, 'eventWeight')
        h_tmp.SetTitle('%s'%(var))
        h_tmp.SetName('%s'%(var))
        histograms.append(h_tmp)
    h.Draw() # run one loop for all variables

    # writing output histograms
    f_out.cd()
    for h in histograms:
        h.Write()
    f_out.Close()

