import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

# Config
LINE_SHEETS = ['MB PN2', 'BE PN2', 'WC PN2', 'WE PN2', 'Impervious PN2',
               'Width', 'Slope', 'N-impervious', 'N-pervious',
               'Dstore Impervious', 'Dstore pervious','TSS_PN2', 'TSS_PN1']


SCATTER_SHEETS = ['TSS_Correlation_PN2', 'TSS_Correlation_PN1']

TSS_SHEETS = ['BE PN2', 'MB PN2', 'WC PN2', 'WE PN2',
              'TSS_PN1', 'TSS_PN2']

PN_FLOW_SHEETS = ['PN1', 'PN2']

EXCEL_PATH = r"D:\SWMM_Runoff_Analysis\Data\Data.xlsx"

# ── Output folders ───────────────────────────────────────────────────────────
HYDRO_FOLDER = Path("D:\SWMM_Runoff_Analysis\Plots\Hydrographs")   # ← PN1, PN2 flow plots
SENSITIVITY_FOLDER  = Path("D:\SWMM_Runoff_Analysis\Plots\Senstivity")   # ← Dstore per., Dstore imper., N-perv., N-imperv., imperv., Slope, Width, MB, BE, WC, WE sensitivity
TSS_FOLDER   = Path("D:\SWMM_Runoff_Analysis\Plots\TSS")           # ← TSS_PN1, TSS_PN2
SCATTER_FOLDER  = Path("D:\SWMM_Runoff_Analysis\Plots\Scatter")       # ← correlation scatter plots


def plot_pn_flow(sheet_name, df):
    # PN1 & PN2 original block unchanged
    plt.rcParams.update({'font.size': 8})
    fig, ax1 = plt.subplots(figsize=(12, 6), dpi=300)
    ax2 = ax1.twiny()
    ax3 = ax1.twinx()

    ax3.bar(df['Rainfall Date & Time'], df['mm/20 mins'],
            color='lightskyblue', alpha=0.6, label='Rainfall',
            width=pd.Timedelta(minutes=15))
    ax3.set_ylabel('Rainfall (mm/20 mins)', color='black', fontsize=9)
    ax3.tick_params(axis='y', labelcolor='black', labelsize=8)
    ax3.invert_yaxis()

    # ax1.plot(df['Date & Time (Elapsed Hours)'], df['Computed Flow (LPS)'],
    #          'b-', label='Computed Flow', marker='o', color='red',
    #          markersize=4, linewidth=1.5)
    ax1.plot(df['Date & Time (Elapsed Hours)'], df['Observed Flow (LPS)'],
             'g-', label='Observed Flow', marker='s', color='green',
             markersize=4, linewidth=1.5)
    ax1.set_xlabel('Date and Time', fontsize=9)
    ax1.set_ylabel('Flow (LPS)', color='black', fontsize=9)
    ax1.tick_params(axis='both', labelsize=8)
    ax1.grid(True, linestyle='--', alpha=0.5, linewidth=0.5)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
    ax2.set_xticklabels([])
    ax2.set_xticks([])
    ax2.spines['top'].set_visible(True)
    ax2.spines['bottom'].set_visible(False)
    ax2.set_xlim(ax1.get_xlim())

    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right', fontsize=8)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax1.legend(lines1 + lines3, labels1 + labels3,
               loc='upper right', fontsize=8,
               markerscale=0.8, framealpha=0.8, edgecolor='none')

    plt.title(f'Flow and Rainfall Time Series - {sheet_name}',
              pad=20, fontsize=10)
    plt.tight_layout()
    plt.savefig(HYDRO_FOLDER / f"{sheet_name}_Hydrograph.png", dpi=300, bbox_inches='tight')
    plt.close(fig)

def plot_line_sheet(sheet_name, df):
    colors = ['green', 'orange']
    plt.figure(figsize=(10, 6))
    
    for i, col in enumerate(df.columns):
        if col == 'Date & Time (Elapsed Hours)':
            continue
        
        x = df['Date & Time (Elapsed Hours)']
        y = df[col]

        if '+' in col and '%' in col:
            # Red line with circular markers
            plt.plot(x, y, label=col, color='red', marker='o', linestyle='-', linewidth=1.5, markersize=5, markerfacecolor='none')
        elif '-' in col and '%' in col:
            # Yellow line with triangle markers (no fill)
            plt.plot(x, y, label=col, color='blue', marker='^', linestyle='-', linewidth=1.5, markersize=5, markerfacecolor='none')
        else:
            # Regular line
            plt.plot(x, y, label=col, color=colors[i % len(colors)], linewidth=1.5)

    plt.title(sheet_name)
    plt.xlabel('Date and Time')
    if sheet_name in TSS_SHEETS:
        plt.ylabel('TSS (mg/L)')
        out = TSS_FOLDER
    else:
        plt.ylabel('Flow (L/s)')
        out = SENSITIVITY_FOLDER
    plt.grid(True, linestyle='--', color='grey', alpha=0.6)
    plt.legend(loc='upper right', fontsize=9, framealpha=1)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b %H:%M'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out / f"{sheet_name}.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_scatter_trendline(sheet_name, df):
    x = df['Simulated (mg/l)'].values
    y = df['Observed (mg/l)'].values

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, label='Data Points', color='blue')

    coeffs = np.polyfit(x, y, 1)
    poly_eq = np.poly1d(coeffs)
    y_fit = poly_eq(x)

    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    plt.plot(x, y_fit, color='red', label='Trendline')
    eq_text = f"y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}\n$R^2$ = {r_squared:.3f}"
        # Set custom date format: e.g., 25-Jul 12:00
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b %H:%M'))
    #plt.xticks(rotation=45)
    plt.text(0.05, 0.95, eq_text, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(facecolor='white', alpha=0.7))

    plt.xlabel("Simulated (mg/l)")
    plt.ylabel("Observed (mg/l)")
    plt.title(sheet_name)
    plt.grid(True, linestyle='--', color='grey')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(SCATTER_FOLDER / f"{sheet_name}.png", dpi=300,
                bbox_inches='tight')
    plt.close()

def main():
    xls = pd.ExcelFile(EXCEL_PATH)
    for sheet in xls.sheet_names:
        print(f"Processing: {sheet}")
        df = pd.read_excel(EXCEL_PATH, sheet_name=sheet)

        # Overwrite datetime columns directly
        if 'Date & Time (Elapsed Hours)' in df.columns:
            df['Date & Time (Elapsed Hours)'] = pd.to_datetime(
                df['Date & Time (Elapsed Hours)'],
                format='%d-%m-%Y %H:%M:%S', errors='coerce'
            )
        if 'Rainfall Date & Time' in df.columns:
            df['Rainfall Date & Time'] = pd.to_datetime(
                df['Rainfall Date & Time'],
                format='%d-%m-%Y %H:%M:%S', errors='coerce'
            )

        if sheet in PN_FLOW_SHEETS:
            req = ['Date & Time (Elapsed Hours)', 'Rainfall Date & Time',
                    'Observed Flow (LPS)', 'mm/20 mins']
            if all(col in df.columns for col in req):
                plot_pn_flow(sheet, df)
            else:
                print(f"Skipping {sheet} — missing PN1/PN2 columns.")

        elif sheet in LINE_SHEETS:
            if 'Date & Time (Elapsed Hours)' in df.columns:
                plot_line_sheet(sheet, df)
            else:
                print(f"Skipping {sheet} — no datetime for line plot.")


 
        elif sheet in SCATTER_SHEETS:
            if 'Simulated (mg/l)' in df.columns and 'Observed (mg/l)' in df.columns:
                plot_scatter_trendline(sheet, df)
            else:
                print(f"Skipping {sheet} — lacking scatter data.")

        else:
            print(f"Skipped: {sheet} — no plotting rule.")

if __name__ == "__main__":
    main()




