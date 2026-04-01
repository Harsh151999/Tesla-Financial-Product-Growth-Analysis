"""
Tesla Financial & Product Growth Analysis (2012–2020)
======================================================
BBA Final Project — BIT Mesra, Department of Management

Run:
    python scripts/generate_charts.py

Outputs four charts to the charts/ directory.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# ── Ensure output folder exists ──────────────────────────────────────────────
OUT = os.path.join(os.path.dirname(__file__), '..', 'charts')
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

YEARS = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
X = np.arange(len(YEARS))

DARK_BLUE  = '#1C3C6B'
MID_BLUE   = '#4A90D9'
ORANGE     = '#E05C2A'
GREEN      = '#2E8B57'
RED        = '#D94F3D'

# ════════════════════════════════════════════════════════════════════════════
# CHART 1 – Revenue & Net Income / (Loss)
# ════════════════════════════════════════════════════════════════════════════
def chart1_revenue_netincome():
    revenue    = [413, 2013, 3200, 4046, 7000, 11759, 21461, 24578, 31536]
    net_income = [-396, -74, -294, -889, -675, -1962, -976, -862, 690]

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.bar(X, revenue, color=DARK_BLUE, alpha=0.85, label='Total Revenue ($M)')
    ax1.set_xlabel('Year', fontsize=11)
    ax1.set_ylabel('Revenue (USD Millions)', color=DARK_BLUE, fontsize=11)
    ax1.tick_params(axis='y', labelcolor=DARK_BLUE)
    ax1.set_xticks(X)
    ax1.set_xticklabels(YEARS, fontsize=10)
    ax1.yaxis.set_major_formatter(
        mtick.FuncFormatter(lambda v, _: f'${v:,.0f}M'))

    ax2 = ax1.twinx()
    dot_colors = [RED if v < 0 else GREEN for v in net_income]
    ax2.plot(X, net_income, color=ORANGE, marker='o', linewidth=2.2,
             markersize=7, label='Net Income/(Loss) ($M)', zorder=5)
    for i, v in enumerate(net_income):
        ax2.scatter(X[i], v, color=dot_colors[i], s=60, zorder=6)
    ax2.set_ylabel('Net Income / (Loss) (USD Millions)', color=ORANGE, fontsize=11)
    ax2.tick_params(axis='y', labelcolor=ORANGE)
    ax2.yaxis.set_major_formatter(
        mtick.FuncFormatter(lambda v, _: f'${v:,.0f}M'))
    ax2.axhline(0, color='#888', linewidth=0.8, linestyle='--')

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)

    plt.title('Tesla Annual Revenue & Net Income/(Loss) (2012–2020)',
              fontsize=13, fontweight='bold', pad=12)
    fig.tight_layout()
    path = os.path.join(OUT, 'chart1_revenue_netincome.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Saved: {path}')


# ════════════════════════════════════════════════════════════════════════════
# CHART 2 – Vehicle Production & Deliveries
# ════════════════════════════════════════════════════════════════════════════
def chart2_production_deliveries():
    production = [3100, 22500, 35000, 51095, 83922, 100757, 254530, 365232, 509737]
    deliveries = [2650, 22477, 31655, 50580, 76295, 103097, 245240, 367550, 499550]

    fig, ax = plt.subplots(figsize=(10, 5))
    w = 0.38
    ax.bar(X - w/2, production, width=w, color=DARK_BLUE, alpha=0.85,
           label='Annual Production')
    ax.bar(X + w/2, deliveries, width=w, color=MID_BLUE, alpha=0.85,
           label='Annual Deliveries')
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Number of Vehicles', fontsize=11)
    ax.set_xticks(X)
    ax.set_xticklabels(YEARS, fontsize=10)
    ax.yaxis.set_major_formatter(
        mtick.FuncFormatter(lambda v, _: f'{v:,.0f}'))
    ax.legend(fontsize=10)
    ax.set_title('Tesla Vehicle Production & Deliveries (2012–2020)',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    fig.tight_layout()
    path = os.path.join(OUT, 'chart2_production_deliveries.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Saved: {path}')


# ════════════════════════════════════════════════════════════════════════════
# CHART 3 – 2020 Revenue Composition
# ════════════════════════════════════════════════════════════════════════════
def chart3_revenue_composition():
    labels = [
        'Automotive\n($27.2B | 86.4%)',
        'Services & Other\n($2.3B | 7.3%)',
        'Energy Gen. & Storage\n($2.0B | 6.3%)',
    ]
    sizes   = [27236, 2306, 1994]
    colors  = [DARK_BLUE, MID_BLUE, ORANGE]
    explode = (0.03, 0.03, 0.03)

    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=140, pctdistance=0.65,
        textprops={'fontsize': 10},
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'},
    )
    for at in autotexts:
        at.set_color('white')
        at.set_fontsize(9)
        at.set_fontweight('bold')
    ax.set_title('Tesla 2020 Revenue Composition (Total: $31.5B)',
                 fontsize=13, fontweight='bold', pad=16)
    fig.tight_layout()
    path = os.path.join(OUT, 'chart3_revenue_composition.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Saved: {path}')


# ════════════════════════════════════════════════════════════════════════════
# CHART 4 – Comparable Company EV/EBITDA
# ════════════════════════════════════════════════════════════════════════════
def chart4_comps():
    companies  = ['Tesla', 'Ford', 'GM', 'Volkswagen', 'NIO']
    ev_ebitda  = [157.2, 36.9, 13.3, 12.7, None]
    bar_colors = [DARK_BLUE, MID_BLUE, MID_BLUE, MID_BLUE, ORANGE]
    vals = [v if v is not None else 0 for v in ev_ebitda]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(companies, vals, color=bar_colors, alpha=0.85,
                  edgecolor='white', linewidth=1.2)
    for bar, val in zip(bars, ev_ebitda):
        if val is not None:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 1.5,
                    f'{val}x', ha='center', va='bottom',
                    fontsize=10, fontweight='bold')
        else:
            ax.text(bar.get_x() + bar.get_width() / 2, 2,
                    'Neg.\nEBITDA', ha='center', va='bottom',
                    fontsize=9, color=ORANGE)
    ax.set_ylabel('EV / EBITDA Multiple (2020)', fontsize=11)
    ax.set_title('EV/EBITDA Comparable Company Analysis (2020)',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_ylim(0, 180)
    fig.tight_layout()
    path = os.path.join(OUT, 'chart4_comps.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Saved: {path}')


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Generating Tesla analysis charts...\n')
    chart1_revenue_netincome()
    chart2_production_deliveries()
    chart3_revenue_composition()
    chart4_comps()
    print('\nAll charts generated successfully!')

