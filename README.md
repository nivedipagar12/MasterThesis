# MasterThesis
This repository contains all the codes and data associated with my Master Thesis titled **"Evaluation and feasibility study of an integrated sensor front-end using BIA for human body composition analysis"**. If you are new to this field, I suggest reading a little about the following topics:

1) **BIA** : [Bioelectrical Impedance Analysis](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis)
2) **BIS** : [Bioelectrical Impedance Spectroscopy](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis)
3) **Cole Model** : [Need of cole model and curve fitting for Body Composition Analysis](https://iopscience.iop.org/article/10.1088/0967-3334/34/10/1239)

Folder Name: Curve Fitting

This folder contains the main curve fitting algorithm. In the above mentioned cole modelling paper, you will find the formulas used to find the initial values of **x0, y0 and r0 (Equation 5)** and the simplified formula used to implement the **BFGS** algorithm to find the result as a function of **f(x0, y0, r0)**. Upon finding the **center** **(x0,y0)** and **radius** **r0** of the imaginary circle, the **R0** and **Rinf** values can be calculated using distance formula as follows :

Point 1: x0,y0
Point 2: R0 or Rinf,0

Since the points R0 and Rinf are on x axis, their y-coordinate will be 0
distance = r0

We already know the distance between the two points, so reverse engineering the distance formula, we can find R0 and Rinf as follows:

R_{0} = x_{0} + \sqrt{r_{0}^{2} - y_{0}^{2}} .. to find R0
R_{\infty}  = x_{0} - \sqrt{r_{0}^{2} - y_{0}^{2}} .. to find Rinf
