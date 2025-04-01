Environmental Impact of Diets – Radar Chart Visualization
This project is part of the COMP4037 Research Methods coursework. It investigates the environmental impact of various diet groups using a radar chart. The aim is to present clearer and more comprehensive insights than traditional visualizations such as pie charts or bar graphs.

Project Objective
The objective of this project is to explore the question:
Do different diet types consistently show advantages or disadvantages across multiple environmental indicators? Which diet appears to be the most environmentally balanced?

This is addressed by comparing Vegan, Vegetarian, Fish-eater, and Meat-eater groups across nine environmental impact indicators.

Data Source
The dataset is based on the following study:

Scarborough, P., Clark, M., Cobiac, L. et al. (2023). Vegans, Vegetarians, Fish-eaters and Meat-eaters in the UK Show Discrepant Environmental Impacts. Nature Food 4, 565–574.
Dataset: https://ora.ox.ac.uk/objects/uuid:a127a08b-5eb5-4b42-9435-c7162d73ff41

The indicators used include:

Greenhouse gas emissions

Agricultural land use

Water scarcity

Eutrophication potential

CH₄ emissions

N₂O emissions

Biodiversity impact

Agricultural water use

Acidification potential

Methodology
Data Cleaning – Removed rows with missing values.

Grouping – Calculated mean values for each environmental indicator per diet group.

Log Transformation – Applied log1p(x) to reduce scale differences.

Normalization – Scaled all values between 0 and 1 using Min-Max normalization.

Visualization – Created a radar chart using Matplotlib to compare the environmental profile of each group.

Key Findings
The radar chart shows that vegan diets have the lowest and most balanced environmental impact across all indicators. Meat-eaters consistently score higher in greenhouse gas emissions, land use, and biodiversity impact. Fish-eaters, while lower in carbon emissions, exert greater pressure on water resources, especially in terms of scarcity. These insights are clearer in a multi-dimensional radar chart than in traditional one-variable plots.

How to Run
Place Results_21Mar2022.csv in the data/ folder.

Install required Python libraries:

pip install pandas numpy matplotlib
Run the script:

python visualisation.py

File Structure

.
├── data/
│   └── Results_21Mar2022.csv
├── visualisation.py
└── README.md
