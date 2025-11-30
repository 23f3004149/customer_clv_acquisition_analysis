import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
acquisition_cost = np.random.uniform(20, 300, 200)
clv_multiplier = np.random.uniform(10, 20)
noise = np.random.normal(0, 300, 200)
customer_lifetime_value = acquisition_cost * clv_multiplier + noise

df = pd.DataFrame({
    'Acquisition_Cost': acquisition_cost,
    'Customer_Lifetime_Value': customer_lifetime_value
})

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# EXACT 512 × 512 px (8 inches * 64 dpi)
plt.figure(figsize=(8, 8), dpi=64)

# Scatterplot
sns.scatterplot(
    data=df,
    x='Acquisition_Cost',
    y='Customer_Lifetime_Value',
    s=80,
    alpha=0.7,
    color=sns.color_palette("viridis", 10)[5]
)

plt.title("Customer Lifetime Value vs Acquisition Cost", pad=20)
plt.xlabel("Customer Acquisition Cost ($)")
plt.ylabel("Customer Lifetime Value ($)")

# Save EXACT 512px without any scaling or cropping
plt.savefig("customer_clv_acquisition_analysis\chart.png", dpi=64)
plt.close()

