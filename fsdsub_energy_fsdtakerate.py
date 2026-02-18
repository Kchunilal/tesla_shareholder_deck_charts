import pandas as pd
import matplotlib.pyplot as plt

# ====================== DATA FROM JANUARY 2026 SHAREHOLDER DECK ======================
# Update these with the exact numbers from the deck
data = {
    'Quarter': ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    'FSD_Subscribers': [85000, 125000, 178000, 245000, 320000],
    'Energy_GWh': [8.1, 9.4, 11.2, 13.8, 15.3],
    'FSD_Take_Rate': [17.5, 32.3, 40.1, 52.9, 72.2]   # % of deliveries subscribing to FSD
}

df = pd.DataFrame(data)

# ====================== COMPLEX TRIPLE-METRIC CHART ======================
fig, ax1 = plt.subplots(figsize=(13, 7.5))

# Bar: FSD Subscribers
ax1.bar(df['Quarter'], df['FSD_Subscribers']/1000, color='#3498db', alpha=0.85, width=0.6, label='FSD Subscribers (thousands)')
ax1.set_ylabel('FSD Subscribers (thousands)', color='#3498db', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#3498db')

# Line 1: Energy Deployment (right axis)
ax2 = ax1.twinx()
ax2.plot(df['Quarter'], df['Energy_GWh'], marker='o', linewidth=4, color='#2ecc71', label='Energy Deployment (GWh)')
ax2.set_ylabel('Energy Storage Deployed (GWh)', color='#2ecc71', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#2ecc71')

# Line 2: FSD Take-Rate % (second right axis)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))   # Move third axis outward
ax3.plot(df['Quarter'], df['FSD_Take_Rate'], marker='s', linewidth=3, color='#e67e22', label='FSD Take-Rate %')
ax3.set_ylabel('FSD Take-Rate (%)', color='#e67e22', fontsize=12)
ax3.tick_params(axis='y', labelcolor='#e67e22')

plt.title('FSD Subscription Growth vs Energy Storage & Adoption Efficiency\nTesla January 2026 Shareholder Deck', 
          fontsize=15, fontweight='bold', pad=25)
fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.88), fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('fsd_energy_take_rate_complex.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Complex chart saved as 'fsd_energy_take_rate_complex.png'")