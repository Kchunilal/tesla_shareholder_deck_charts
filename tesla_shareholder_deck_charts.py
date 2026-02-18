import pandas as pd
import matplotlib.pyplot as plt

# ====================== DATA FROM JANUARY 2026 SHAREHOLDER DECK ======================
data = {
    'Year': ['2021', '2022', '2023', '2024', '2025'],
    'Deliveries': [936172, 1313851, 1808581, 1789226, 1636129],
    'Production': [930422, 1369611, 1845985, 1773443, 1654667],
    'Revenue_B': [53.8, 81.5, 96.8, 97.7, 94.8],
    'GAAP_Net_Income_B': [5.5, 12.6, 15.0, 7.1, 3.8],
    'Energy_Storage_GWh': [3.99, 6.5, 14.7, 31.4, 46.7]
}

df = pd.DataFrame(data)

print("✅ Tesla 2025 Shareholder Deck Data Loaded")
print(df)

# ====================== CHART 1: Vehicle Deliveries Trend (2021-2025) ======================
plt.figure(figsize=(11, 6))
plt.bar(df['Year'], df['Deliveries'], color='#3498db', alpha=0.85)
plt.title('Tesla Annual Vehicle Deliveries (2021–2025)\nFirst Decline Since 2020', fontsize=15, fontweight='bold')
plt.ylabel('Deliveries')
plt.xlabel('Year')
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(df['Deliveries']):
    plt.text(i, v + 30000, f'{v:,}', ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('tesla_deliveries_2021_2025.png', dpi=300)
plt.show()

# ====================== CHART 2: Energy Storage Growth (Explosive) ======================
plt.figure(figsize=(11, 6))
plt.plot(df['Year'], df['Energy_Storage_GWh'], marker='o', linewidth=4, color='#2ecc71')
plt.title('Tesla Energy Storage Deployment (GWh) – Massive Growth', fontsize=15, fontweight='bold')
plt.ylabel('Gigawatt-Hours Deployed')
plt.xlabel('Year')
plt.grid(True, alpha=0.3)

for i, v in enumerate(df['Energy_Storage_GWh']):
    plt.text(i, v + 2, f'{v}', ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('tesla_energy_storage_growth.png', dpi=300)
plt.show()

# ====================== CHART 3: Revenue & Net Income Trend ======================
fig, ax1 = plt.subplots(figsize=(11, 6))

ax1.bar(df['Year'], df['Revenue_B'], color='#3498db', alpha=0.7, label='Revenue ($B)')
ax1.set_ylabel('Revenue ($ Billion)', color='#3498db')

ax2 = ax1.twinx()
ax2.plot(df['Year'], df['GAAP_Net_Income_B'], marker='o', color='#e74c3c', linewidth=3, label='GAAP Net Income ($B)')
ax2.set_ylabel('GAAP Net Income ($ Billion)', color='#e74c3c')

plt.title('Tesla Revenue vs Net Income (2021–2025)', fontsize=15, fontweight='bold')
fig.tight_layout()
plt.savefig('tesla_revenue_vs_profit.png', dpi=300)
plt.show()

# ====================== CHART 4: Production vs Deliveries (2025 Focus) ======================
years = ['2024', '2025']
prod = [1773443, 1654667]
deliv = [1789226, 1636129]

x = range(len(years))
plt.figure(figsize=(9, 6))
plt.bar(x, prod, width=0.4, label='Production', color='#3498db', alpha=0.8)
plt.bar([i+0.4 for i in x], deliv, width=0.4, label='Deliveries', color='#e67e22', alpha=0.8)

plt.xticks([i+0.2 for i in x], years)
plt.title('Tesla Production vs Deliveries\n2024 vs 2025', fontsize=14, fontweight='bold')
plt.ylabel('Vehicles')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('tesla_prod_vs_deliveries.png', dpi=300)
plt.show()

print("\n🎉 All charts saved as PNG files in your folder!")