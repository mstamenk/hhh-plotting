# Instructions

Clone this framework directly in the `src` directory where NanoAODTools and NanoNN are.

# From Trees outputted from NanoAODTools to histograms for plotting
```
python make_histograms_rdataframe_selection.py --version v17-6jets-BDT --region inclusive --tag 0ptag --wp loose --f_in GluGluToHHHTo6B_SM
```

This script is where the event selection is defined and the framework is used to process histograms defined in lables of `utils.py`. 

This is a simple maccro i use but any script to process TTrees can be used. You can also use this for inspiration only.

The condor-run repository contains a script to prepare jobs to run them on condor:
```
python prepare_jobs.py
chmod + x submit_all.sh # done only once
./submit_all.sh
```

There's two additional scripts to plot overlays of histograms produced from the previous step:
```
python draw_data_mc_categories.py # plot data / mc
python draw_signal_bkg_categories.py # compare shapes
```
