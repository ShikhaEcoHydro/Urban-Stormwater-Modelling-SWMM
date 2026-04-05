# SWMM Stormwater Runoff Analysis – Bargteheide, Germany

Master's thesis project submitted at Technische Hochschule Lübeck 
(Erasmus Mundus Master in Applied Ecohydrology), August 2025.

**Title:** Establishment of a methodology for determining stormwater 
discharges based on hydrodynamic rainfall-runoff sewer network simulations

**Author:** Deepshikha Srivastava  
**Supervisors:** Prof. Dr. Philipp Zantout-Wilfert & Prof. Dr.-Ing. Kai Wellbrock

---

## Overview
This project uses the EPA Storm Water Management Model (SWMM) to simulate 
stormwater runoff quantity and quality in a small commercial urban catchment 
(~21 ha) in Bargteheide, northern Germany. The focus pollutant is Total 
Suspended Solids (TSS).

Two rainfall events were used:
- **PN2** – 5th July 2023 → used for calibration
- **PN1** – 22nd–23rd June 2023 → used for validation

---

## Key Findings
### Runoff quantity sensitivity (ranked):

Impervious surface percentage had the largest effect on peak flow (peak variation: −28% to +14%)
Depression storage of impervious area was the second most sensitive parameter
Manning's n for pervious surfaces showed zero effect on peak flow

### Runoff quality sensitivity:

Maximum buildup (C1) was the most sensitive parameter; a ±50% change caused errors ranging from −21% to +60%
Washoff coefficient (D1) was the second most sensitive parameter
Buildup exponent (C2) showed the least sensitivity among quality parameters

### Limitations observed:

Antecedent dry day uncertainty was the primary reason for poor TSS validation performance — the PN1 event was preceded by a high-intensity rain that reset surface buildup, which could not be represented in the model with ADD = 0
Single-point TSS sampling at the outlet may have missed first-flush peak concentrations
Rainfall measured at a single gauge may not reflect spatial variability across the 21 ha catchment

---

## Repository Structure
```
SWMM_Runoff_Analysis/
│
├── swmm_model/
│   ├── model_initial.inp
│   ├── model_calibrated_PN2.inp
│   └── model_validated_PN1.inp
│
├── data/
│   ├── rainfall_flow_PN1.xlsx
│   ├── rainfall_flow_PN2.xlsx
│   └── tss_observed.xlsx
│
├── scripts/
│   └── plot_results.py
│
├── plots/
│   ├── hydrographs/
│   ├── sensitivity/
│   ├── tss_pollutographs/
│   └── scatter/
│
└── README.md
```
## Model Performance

### Runoff Quantity
| Phase | NSC | R² | RSR | PBIAS |
|------------|------|------|------|--------|
| Calibration| 0.84 | 0.85 | 0.38 | 6.23% |
| Validation | 0.52 | 0.67 | 0.58 | -8.65% |

### Runoff Quality (TSS)
| Phase | NSC | R² | RSR | PBIAS |
|------------|------|------|------|--------|
| Calibration| 0.70 | 0.71 | 0.49 | -0.48% |
| Validation | 0.30 | 0.68 | 0.63 | 30.67% |

---

## Key Findings
- **Impervious percentage** and **depression storage** were the most 
  sensitive parameters for runoff quantity
- **Maximum buildup (C1)** and **washoff coefficient (D1)** were the 
  most sensitive parameters for TSS quality
- Validation performance for TSS was limited due to antecedent 
  dry day uncertainty and single-event calibration

---
## Software Used
### Primary Modelling Tool — EPA SWMM
All rainfall-runoff simulations, calibration, validation, and sensitivity analysis were conducted directly in EPA SWMM 5.x, which is free to download from:https://www.epa.gov/water-research/storm-water-management-model-swmm
### GIS Analysis — QGIS
Subcatchment physical parameters (area, width, slope, impervious %) were derived from DEM and aerial photographs using QGIS (free and open-source):https://qgis.org


## Plot Requirements
pip install pandas matplotlib openpyxl
cd scripts
python plot_results.py

---

## How to Run the Plots
1. Clone the repository:
```bash
git clone https://github.com/ShikhaEcoHydro/SWMM-Stormwater-Analysis.git
```
2. Place your `Data.xlsx` in the `data/` folder
3. Run the script:
```bash
cd script
python Plot.py
```
4. Plots will be saved automatically in the `plots/` subfolders

---

## Study Area
- **Location:** Bargteheide, Schleswig-Holstein, Germany
- **Area:** ~21 ha (commercial/light industrial land use)
- **Average impervious cover:** 61.88%
- **Mean slope:** 0.82%
- **Subcatchments:** 25

---

## SWMM Model Setup
| Parameter | Value |
|----------------------|--------------------------|
| Routing model | Kinematic wave |
| Infiltration model | Modified Green-Ampt |
| Soil type | Sandy loam |
| Buildup function | Power |
| Washoff function | Exponential |
| Pollutant modelled | TSS |

---

## Data Source
Field monitoring data (rainfall, flow, TSS) were collected by:
Wellbrock, K.; Retschko, A.; Marquardt, C.; Hödl, J.; Grottker, M. (2024):
Leistungsfähigkeit von Maßnahmen zur Regenwasserbewirtschaftung im Trennsystem in Schleswig-Holstein (Ma:ReT-SH).
Abschlussbericht, Landesamt für Umwelt Schleswig-Holstein, Lübeck/Kiel.

TSS concentrations were determined following DIN 38409-2 using 0.45 µm polyether sulfone membrane filtration. Flow was measured using an OTT MF Pro magnetic-inductive flow meter.

---

## References
- Rossman, L.A. (2010). Storm Water Management Model User's Manual, Version 5.0. US EPA.
- Moriasi, D.N. et al. (2007). Model Evaluation Guidelines for Systematic Quantification of Accuracy in Watershed Simulations.Transactions of the ASABE, 50(3), 885–900.
- Egodawatta, P., Thomas, E., & Goonetilleke, A. (2009). Understanding the physical processes of pollutant build-up and wash-off on roof surfaces. Science of the Total Environment, 407(6), 1834–1841.

---

## License
This repository is shared for academic reference. Please cite the thesis if you use this work:
Srivastava, D. (2025). Establishment of a methodology for determining stormwater discharges based on hydrodynamic rainfall-runoff sewer network simulations. Master's Thesis, Technische Hochschule Lübeck.
