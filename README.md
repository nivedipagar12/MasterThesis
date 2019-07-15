# MasterThesis
This repository contains all the codes and data associated with my Master Thesis titled **"Evaluation and feasibility study of an integrated sensor front-end using BIA for human body composition analysis"**. If you are new to this field, I suggest reading a little about the following topics:

- **BIA** : [Bioelectrical Impedance Analysis](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis)
- **BIS** : [Bioelectrical Impedance Spectroscopy](https://en.wikipedia.org/wiki/Bioelectrical_impedance_analysis)
- **Cole Model** : [Need of cole model and curve fitting for Body Composition Analysis](https://iopscience.iop.org/article/10.1088/0967-3334/34/10/1239)

Here are the details of each folder in this repository:

1) Folder Name: Curve Fitting

This folder contains the main curve fitting algorithm. In the above mentioned cole modelling paper, you will find the formulas used to find the initial values of **x0, y0 and r0 (Equation 5)** and the simplified formula used to implement the **BFGS** algorithm to find the result as a function of **F(x0, y0, r0)** **(Equation 3)**. Upon finding the **center** **(x0,y0)** and **radius** **r0** of the imaginary circle, the **R0** and **Rinf** values can be calculated using distance formula as follows :

Point 1: x0,y0
Point 2: R0 or Rinf,0 .. Since the points R0 and Rinf are on x axis, their y-coordinate will be 0
distance = r0 .. We already know the distance between the two points (r0) 

Reverse engineering the distance formula, we can find R0 and Rinf as follows:
- R_{0} = x_{0} + \sqrt{r_{0}^{2} - y_{0}^{2}} .. to find R0
- R_{\infty}  = x_{0} - \sqrt{r_{0}^{2} - y_{0}^{2}} .. to find Rinf

2) PCB Design:

For the purpose of my Master Thesis, I made a PCB for a bioimpedance measurement device. For efficient separation of graound planes and due to size constraints, the design was divided into two PCBs. PCB1 consists of the visible and digital circuitry whereas PCB2 consists of the analog and mixed signal circuitry. An overview of the component placement can be found in PCBoverview.png and a block overview of the systems can be found in blockoverview.png

Design Considerations:

- Separation of ground planes
- Place for electrode connectors
- Provision for bluetooth communication
- Provision for diplaying data

.... More updates coming soon 
