# CPU Chip Dataset Analysis and Visualization


## Project Overview

This Python project, developed for the MFG 598: Engineering Computing w/Python course, focuses on analyzing and visualizing a CPU chip dataset. Utilizing Streamlit, the project offers interactive visualizations and insights into various characteristics of CPU chips over time.

## Dataset

The dataset(https://www.kaggle.com/datasets/michaelbryantds/cpu-and-gpu-product-data) includes various attributes of CPU chips, such as process size, thermal design power (TDP), frequency, the number of transistors, and performance metrics. It reflects the technological advancements in CPU chips over the years.

## Data Preprocessing

The dataset undergoes several preprocessing steps to ensure quality and reliability:

- Missing values in numerical columns are filled with the median.
- Missing values in categorical columns are replaced with 'Unknown'.
- 'Release Date' is converted to a datetime format.
- Unnecessary index columns are removed.
- The cleaned data is then saved as a new CSV file.

## Streamlit Application

The Streamlit application provides an interactive interface to explore the dataset. Key features include:

- **Dynamic Filters**: Users can select release years, vendors, and process sizes.
- **Visualizations**: Various charts like line charts, pie charts, scatter plots, boxplots, and heatmaps.
- **Dynamic Charting**: Options to choose different metrics for scatter plots and line charts.
- **Summary Statistics**: Display of descriptive statistics of the dataset.
- **Downloadable Data**: Feature to download filtered data as CSV.
- **User Feedback**: A section for users to provide their feedback.

## Author
Name: Sai Shivani Lingampally

Course: MFG 598: Engineering Computing w/Python

Year: 2023


## License
This project is licensed under the MIT License (MIT).

