# 🌱 Environmental Impact of Diets – Radar Chart Visualization

This project visualizes the environmental impact of different diet groups using a radar chart. It is part of the coursework for the **COMP4037 Research Methods** module at the University of Nottingham.

## 📌 Objective

To answer the research question:

> **Do different diet types show consistent advantages or disadvantages across multiple environmental impact indicators? Which diet is the most environmentally balanced?**

This visualization aims to provide a multi-dimensional comparison of diets such as **Vegan**, **Vegetarian**, **Fish-eater**, and **Meat-eater** across various ecological impact metrics.

## 📊 Dataset

The dataset used in this project is based on:

> Scarborough, P., Clark, M., Cobiac, L. et al. *Vegans, Vegetarians, Fish-eaters and Meat-eaters in the UK Show Discrepant Environmental Impacts*. Nature Food 4, 565–574 (2023).  
> [Download link from ORA](https://ora.ox.ac.uk/objects/uuid:a127a08b-5eb5-4b42-9435-c7162d73ff41)

### Key columns used:
- `mean_ghgs`: Greenhouse gas emissions (kg CO2-eq)
- `mean_land`: Agricultural land use (m²)
- `mean_watscar`: Water scarcity footprint
- `mean_eut`: Eutrophication potential (g PO₄-eq)
- `mean_ghgs_ch4`: Methane emissions (CH₄)
- `mean_ghgs_n2o`: Nitrous oxide emissions (N₂O)
- `mean_bio`: Biodiversity impact
- `mean_watuse`: Water usage (m³)
- `mean_acid`: Acidification potential

## 🛠️ Methodology

1. **Data Cleaning**  
   Missing values were dropped to ensure accurate grouping and normalization.

2. **Data Aggregation**  
   The dataset was grouped by `diet_group`, and the mean value for each environmental indicator was calculated.

3. **Log Transformation**  
   To reduce extreme differences in scale, a `log1p` (log(1+x)) transformation was applied to each indicator.

4. **Min-Max Normalization**  
   All indicators were normalized to a [0, 1] scale for comparability on the radar chart.

5. **Radar Chart Creation**  
   The radar chart was plotted using `matplotlib` in polar coordinates, one line per diet group.

## 📈 Visualization Output

The radar chart shows how each diet performs across nine environmental indicators. A balanced diet would appear as a small and even polygon, while uneven or environmentally intensive diets stretch further from the center on multiple axes.

## 🧠 Insight

> **Vegan diets consistently show the lowest environmental impact across all metrics, forming the most compact and balanced shape on the radar chart.**  
> In contrast, meat-eaters exhibit higher values across nearly all indicators, particularly in GHG emissions and land use.

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/diet-impact-visualisation.git
   cd diet-impact-visualisation
