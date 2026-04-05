# Urban Stormwater Modelling using EPA SWMM – Bargteheide, Germany

Master's thesis submitted at **Technische Hochschule Lübeck**  
Erasmus Mundus Master in Applied Ecohydrology (MAEH) — Summer Term 2025

**Title:** Establishment of a methodology for determining stormwater discharges based on hydrodynamic rainfall-runoff sewer network simulations  
**Author:** Deepshikha Srivastava (Matriculation No. 384001)  
**Main Supervisor:** Prof. Dr. Philipp Zantout-Wilfert  
**Co-Supervisor:** Prof. Dr.-Ing. Kai Wellbrock

---

## About This Repository

This repository documents the modelling work conducted as part of my Master's thesis. All hydrodynamic simulations were performed using the **EPA Storm Water Management Model (SWMM 5.x)** — a free, open-source tool developed by the US Environmental Protection Agency. Python was used only for post-processing and visualisation of simulation outputs.

The study simulates stormwater runoff **quantity and quality** (Total Suspended Solids, TSS) in a small commercial urban catchment (~21 ha) in Bargteheide, northern Germany. Field data were collected by Wellbrock et al. (2024) as part of the Ma:ReT-SH research programme.

---

## Study Area

| Parameter | Value |
|---|---|
| Location | Bargteheide, Schleswig-Holstein, Germany |
| Catchment area | ~21.087 ha |
| Land use | Commercial / light industrial |
| Mean impervious cover | 61.88% |
| Mean slope | 0.82% |
| Elevation range | 36.73 m (NE) to 41.78 m (SW) |
| Average annual rainfall | ~64.1 mm/month |
| Number of subcatchments | 25 |

---

## Rainfall Events Used

| Event ID | Date | Duration | Peak Flow (L/s) | Rainfall (mm) | Antecedent Dry Days | Role in Study |
|---|---|---|---|---|---|---|
| PN2 | 5 July 2023 | 3h 25min | 156.76 | 13.0 | 0 | Calibration |
| PN1 | 22–23 June 2023 | 5h 45min | 121.43 | 20.3 | 0 | Validation |

---

## Repository Structure

```
Urban-Stormwater-Modelling-SWMM/
│
├── Data/                        ← Observed rainfall, flow and TSS data
│
├── SWMM_Files/                  ← SWMM .inp model files (initial, calibrated, validated)
│
├── Script/                      ← Python script for post-processing and plotting
│
├── Plots/                       ← All output figures (hydrographs, TSS, sensitivity, scatter)
│
├── Thesis/                      ← Full thesis PDF (TH Lübeck, 2025)
│
└── README.md
```

---

## SWMM Model Configuration

| Component | Choice / Value |
|---|---|
| Routing model | Kinematic Wave |
| Infiltration model | Modified Green-Ampt |
| Soil type | Sandy loam |
| Suction head | 4.33 inches |
| Hydraulic conductivity | 0.43 inches/hr |
| Evaporation | 3 mm/day (constant) |
| Pollutant modelled | TSS (Total Suspended Solids) |
| Buildup function | Power function |
| Washoff function | Exponential function |
| Land uses defined | Commercial area, Road |

Physical parameters (area, width, slope, impervious %) were extracted from the Digital Elevation Model (DEM) and aerial photographs using **QGIS**. Pipe network geometry was obtained from municipal sewer network maps.

---

## Calibration Parameters — Runoff Quantity

| Rank | Parameter | Initial Value | Calibrated Value | Variation Range |
|---|---|---|---|---|
| 1 | Impervious % | Calculated from DEM | Adjusted | ±20% |
| 2 | Depression storage – impervious (mm) | 1.78 | 1.27 | ±40% |
| 3 | Width (m) | Calculated from DEM | Adjusted | ±30% |
| 4 | Manning's n – impervious | 0.010 | 0.012 | ±20% |
| 5 | % Zero-impervious | 25 | 25 | ±45% |
| 6 | Slope (%) | Calculated from DEM | Adjusted | ±30% |
| 7 | Manning's n – pervious | 0.13 | 0.13 | ±10% |
| 8 | Depression storage – pervious (mm) | 3.56 | 2.54 | ±40% |

## Calibration Parameters — Runoff Quality (TSS)

| Land Use | Buildup C1 (kg/100m) | Buildup C2 (kg/day/100m) | Washoff D1 | Washoff D2 |
|---|---|---|---|---|
| Commercial | 1.5 | 1.2 | 0.055 | 0.7 |
| Road | 1.4 | 1.1 | 0.004 | 4.5 |

---

## Model Performance Results

### Runoff Quantity

| Phase | NSC | R² | RSR | PBIAS | Rating |
|---|---|---|---|---|---|
| Calibration (PN2) | 0.84 | 0.85 | 0.38 | 6.23% | Good |
| Validation (PN1) | 0.52 | 0.67 | 0.58 | −8.65% | Satisfactory |

### Runoff Quality (TSS)

| Phase | NSC | R² | RSR | PBIAS | Rating |
|---|---|---|---|---|---|
| Calibration (PN2) | 0.70 | 0.71 | 0.49 | −0.48% | Good |
| Validation (PN1) | 0.30 | 0.68 | 0.63 | 30.67% | Unsatisfactory |

Performance ratings follow Moriasi et al. (2007): NSC > 0.65 = Good, > 0.50 = Satisfactory, ≤ 0.50 = Unsatisfactory.

---

## Key Findings

**Runoff quantity sensitivity (ranked):**
- Impervious surface percentage had the largest effect on peak flow (peak variation: −28% to +14%)
- Depression storage of impervious area was the second most sensitive parameter
- Manning's n for pervious surfaces showed zero effect on peak flow

**Runoff quality sensitivity:**
- Maximum buildup (C1) was the most sensitive parameter; a ±50% change caused errors ranging from −21% to +60%
- Washoff coefficient (D1) was the second most sensitive parameter
- Buildup exponent (C2) showed the least sensitivity among quality parameters

**Limitations observed:**
- Antecedent dry day uncertainty was the primary reason for poor TSS validation — the PN1 event was preceded by a high-intensity rain that reset surface buildup, which could not be represented with ADD = 0
- Single-point TSS sampling at the outlet may have missed first-flush peak concentrations
- Rainfall measured at a single gauge may not reflect spatial variability across the 21 ha catchment

---

## Software Used

### Primary Modelling Tool — EPA SWMM
All rainfall-runoff simulations, calibration, validation, and sensitivity analysis were conducted in **EPA SWMM 5.x** (free download):  
https://www.epa.gov/water-research/storm-water-management-model-swmm

### GIS Analysis — QGIS
Subcatchment parameters were derived from DEM and aerial photographs using **QGIS** (free download):  
https://qgis.org

### Post-processing Plots (optional)
To reproduce thesis plots from SWMM-exported output data:
```bash
pip install pandas matplotlib openpyxl
cd Script
python Plot.py
```
> No Python installation is needed to run the SWMM model itself.

---

## Data Source

Field monitoring data (rainfall, flow, TSS) were collected by:

> Wellbrock, K.; Retschko, A.; Marquardt, C.; Hödl, J.; Grottker, M. (2024):
> *Leistungsfähigkeit von Maßnahmen zur Regenwasserbewirtschaftung im Trennsystem in Schleswig-Holstein (Ma:ReT-SH).*
> Abschlussbericht, Landesamt für Umwelt Schleswig-Holstein, Lübeck/Kiel.

TSS concentrations were determined following **DIN 38409-2** using 0.45 µm polyether sulfone membrane filtration. Flow was measured using an OTT MF Pro magnetic-inductive flow meter.

---

## References

- Moriasi, D.N. et al. (2007). Model Evaluation Guidelines for Systematic Quantification of Accuracy in Watershed Simulations. *Transactions of the ASABE*, 50(3), 885–900.
- Rossman, L.A. (2010). *Storm Water Management Model User's Manual, Version 5.0.* US EPA.
- Egodawatta, P., Thomas, E., & Goonetilleke, A. (2009). Understanding the physical processes of pollutant build-up and wash-off on roof surfaces. *Science of the Total Environment*, 407(6), 1834–1841.
- Temprano, J. et al. (2006). Stormwater quality calibration by SWMM: A case study in Northern Spain. *Water SA*, 32(1), 55–63.

---

## License

This repository is shared for academic reference. Please cite the thesis if you use this work:

> Srivastava, D. (2025). *Establishment of a methodology for determining stormwater discharges based on hydrodynamic rainfall-runoff sewer network simulations.* Master's Thesis, Technische Hochschule Lübeck.
---
