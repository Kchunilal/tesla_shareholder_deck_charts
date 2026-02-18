# Tesla January 2026 Shareholder Deck Analysis

**Visual Analysis of Tesla's Q4 2025 & Full Year 2025 Results**

This repository contains Python scripts and charts analyzing Tesla's January 2026 Shareholder Deck, with a strong focus on the **newly highlighted FSD Subscription metrics** and how they compare to other key growth areas (Energy Storage, Vehicle Deliveries, Revenue, etc.).

---

### 📊 Charts Included

| Chart | Description |
|-------|-------------|
| `1_fsd_subscription_growth.png` | FSD Subscribers + Monthly Recurring Revenue |
| `2_fsd_take_rate.png` | FSD Take-Rate Trend (Adoption Efficiency) |
| `3_fsd_percent_of_services.png` | FSD Revenue as % of Total Services Revenue |
| `4_fsd_vs_energy_dual_axis.png` | FSD Growth vs Energy Storage Deployment |
| `fsd_energy_take_rate_complex.png` | **Complex Triple-Metric Chart** – FSD Subscribers + Energy Deployment + FSD Take-Rate |

---

### Key Insights

- **FSD Subscription is Tesla’s fastest-growing segment** — Subscribers nearly quadrupled in 2025, showing strong consumer demand for autonomy.
- **Take-Rate is accelerating** — More new buyers are opting for FSD at delivery or shortly after, indicating improving conversion.
- **FSD is becoming a major revenue contributor** — Its share of total Services revenue is rising rapidly.
- **Energy Storage remains a powerhouse** — Steady, high-growth deployment, but FSD is currently scaling faster.
- Tesla is successfully building **two major high-margin platform businesses** at once: Software (FSD/Robotaxi) and Energy Infrastructure.

This analysis highlights Tesla’s strategic shift toward recurring software revenue and energy, even as vehicle delivery growth has moderated.

---

### How to Run

```bash
# 1. Activate environment (if using)
source nhtsa_env/bin/activate

# 2. Install dependencies
pip install pandas matplotlib

# 3. Run the analysis
python tesla_jan2026_shareholder_charts.py
