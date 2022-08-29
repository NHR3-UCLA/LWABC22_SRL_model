# LWABC22 SRL model
This repository contains the regression files and datasets for the ``Lavrentiadis G., Wang Y., Abrahamson N. A., Bozorgnia Y., \& Goulet C., A Seismologically Consistent Surface Rupture Length Model for Unbounded and Width-Limited Events.'' paper submitted to Earthquake Spectra

The `Analyses` folder contains the regression scripts and model implementations, and the `Data` folder contains the regression datasets. 
The model results, figures, and conclusions can be reproduced by executing the `Analyses\DevelopLWABC22SRLModel.Rmd` R Markdown notebook:<br>
`Rscript -e "rmarkdown::render('Analyses\DevelopLWABC22SRLModel.Rmd')"`

The folder `Analyses\model_implementations` contains an implementation of the porposed model in MATLAB.
