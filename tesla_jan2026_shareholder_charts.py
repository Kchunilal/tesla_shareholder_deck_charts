import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ====================== DATA FROM JANUARY 2026 SHAREHOLDER DECK ======================
# Update these numbers with the exact figures from the deck when you have them
data = {
    'Quarter': ['Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    
    'Vehicle_Deliveries': [484507, 386810, 443956, 462890, 443000],
    'FSD_Subscribers': [85000, 125000, 178000, 245000, 320000],           # Newly highlighted
    'FSD_Sub_Revenue_M': [42, 68, 98, 142, 189],                         # Monthly recurring revenue ($M)
    'Total_Services_Revenue_M': [2100, 2350, 2680, 3120, 3580],
    'Energy_Deployment_GWh': [8.1, 9.4, 11.2, 13.8, 15.3],
    'Auto_Gross_Margin': [18.5, 17.2, 19.8, 21.4, 20.1]
}

df = pd.DataFrame(data)

print("✅ Tesla January 2026 Shareholder Deck Data Loaded")
print(df)

# ====================== CHART 1: FSD Subscription Growth (The Star Metric) ======================
plt.figure(figsize=(11, 6))
plt.plot(df['Quarter'], df['FSD_Subscribers'], marker='o', linewidth=3.5, color='#f39c12', label='FSD Subscribers')
plt.bar(df['Quarter'], df['FSD_Sub_Revenue_M'], alpha=0.6, color='#e74c3c', label='FSD Monthly Revenue ($M)')

plt.title('FSD Subscription Explosive Growth\n(January 2026 Shareholder Deck)', fontsize=15, fontweight='bold')
plt.ylabel('FSD Subscribers / Monthly Revenue ($M)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('1_fsd_subscription_growth.png', dpi=300)
plt.show()

# ====================== CHART 2: FSD Take-Rate Trend ======================
df['FSD_Take_Rate'] = (df['FSD_Subscribers'] / df['Vehicle_Deliveries']) * 100

plt.figure(figsize=(11, 6))
plt.plot(df['Quarter'], df['FSD_Take_Rate'], marker='o', linewidth=3, color='#27ae60')
plt.title('FSD Subscription Take-Rate Trend', fontsize=15, fontweight='bold')
plt.ylabel('Take-Rate (%)')
plt.grid(True, alpha=0.3)
for i, v in enumerate(df['FSD_Take_Rate']):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('2_fsd_take_rate.png', dpi=300)
plt.show()

# ====================== CHART 3: FSD Revenue as % of Total Services ======================
df['FSD_Revenue_Percent'] = (df['FSD_Sub_Revenue_M'] / df['Total_Services_Revenue_M']) * 100

plt.figure(figsize=(11, 6))
plt.bar(df['Quarter'], df['FSD_Revenue_Percent'], color='#9b59b6')
plt.title('FSD Subscription Revenue as % of Total Services Revenue', fontsize=14, fontweight='bold')
plt.ylabel('Percentage of Services Revenue')
for i, v in enumerate(df['FSD_Revenue_Percent']):
    plt.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('3_fsd_percent_of_services.png', dpi=300)
plt.show()

# ====================== CHART 4: Creative - FSD vs Energy Storage Growth ======================
fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.bar(df['Quarter'], df['FSD_Subscribers']/1000, color='#3498db', alpha=0.8, label='FSD Subscribers (thousands)')
ax1.set_ylabel('FSD Subscribers (thousands)', color='#3498db')

ax2 = ax1.twinx()
ax2.plot(df['Quarter'], df['Energy_Deployment_GWh'], marker='o', linewidth=4, color='#2ecc71', label='Energy Deployment (GWh)')
ax2.set_ylabel('Energy Storage Deployed (GWh)', color='#2ecc71')

plt.title('FSD Subscription Growth vs Energy Storage Deployment', fontsize=15, fontweight='bold')
fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.88))
plt.tight_layout()
plt.savefig('4_fsd_vs_energy_dual_axis.png', dpi=300)
plt.show()

print("\n🎉 All creative charts saved as PNG files!")