from streamlit_echarts import st_echarts
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

numeric_cols = ['TDP (W)', 'Freq (MHz)', 'Process Size (nm)', 'Transistors (million)']

@st.cache_data
def load_data():
    data = pd.read_csv(r'C:/Users/ANANYA/PycharmProjects/pythonProject/cleaned_chip_dataset.csv')
    data['Release Date'] = pd.to_datetime(data['Release Date'])
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    return data

data = load_data()

st.title('CPU Chip Dataset visualization using Streamlit ')
st.write('Explore the characteristics of CPU chips over time.')
st.markdown("""
**Course:** MFG 598: Engineering Computing w/Python (2023 Fall)  
**Final Project by:** Sai Shivani Lingampally  
**ASU ID:** 1228534270
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.slider('Select a range of release years',
                                  int(data['Release Date'].dt.year.min()),
                                  int(data['Release Date'].dt.year.max()),
                                  (2000, 2022))
selected_vendors = st.sidebar.multiselect('Select vendors', list(data['Vendor'].unique()), default=data['Vendor'].unique( ))
process_size_filter = st.sidebar.slider('Filter by Process Size (nm)',
                                        float(data['Process Size (nm)'].min()),
                                        float(data['Process Size (nm)'].max()),
                                        (float(data['Process Size (nm)'].min()),
                                         float(data['Process Size (nm)'].max())))

filtered_data = data[data['Release Date'].dt.year.between(selected_year[0], selected_year[1])]
filtered_data = filtered_data[filtered_data['Vendor'].isin(selected_vendors)]
filtered_data = filtered_data[filtered_data['Process Size (nm)'].between(process_size_filter[0], process_size_filter[1])]


st.header('Average TDP over Time')
yearly_avg_tdp = filtered_data.groupby(filtered_data['Release Date'].dt.year)['TDP (W)'].mean().reset_index()
yearly_avg_tdp.columns = ['Year', 'Average TDP']
line_chart_options = {
    "xAxis": {"type": "category", "data": yearly_avg_tdp['Year'].tolist()},
    "yAxis": {"type": "value"},
    "series": [{"data": yearly_avg_tdp['Average TDP'].tolist(), "type": "line"}]
}
st_echarts(options=line_chart_options, height="400px")

st.header('Vendor Distribution')
vendor_count = filtered_data['Vendor'].value_counts().reset_index()
vendor_count.columns = ['Vendor', 'Count']
vendor_pie_options = {
    "tooltip": {"trigger": "item"},
    "legend": {"top": "5%", "left": "center"},
    "series": [{
        "name": "Vendors",
        "type": "pie",
        "radius": "50%",
        "data": [{"value": count, "name": vendor} for vendor, count in zip(vendor_count['Vendor'], vendor_count['Count'])]
    }]
}
st_echarts(options=vendor_pie_options, height="400px")

st.header('Frequency vs. TDP Scatter Plot')
scatter_data = filtered_data[['Freq (MHz)', 'TDP (W)', 'Vendor']].values.tolist()
scatter_options = {
    "xAxis": {"type": "value", "name": "Freq (MHz)"},
    "yAxis": {"type": "value", "name": "TDP (W)"},
    "series": [{"data": scatter_data, "type": "scatter"}]
}
st_echarts(options=scatter_options, height="400px")

st.header('TDP Distribution Across Vendors')
fig, ax = plt.subplots()
sns.boxplot(x='Vendor', y='TDP (W)', data=filtered_data, ax=ax)
ax.set_title('TDP Distribution by Vendor')
st.pyplot(fig)

st.header('Correlation Heatmap')
corr = filtered_data[['TDP (W)', 'Freq (MHz)', 'Process Size (nm)', 'Transistors (million)']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.header('Dynamic Scatter Plot')
x_axis_val = st.selectbox('Select X-axis Value', numeric_cols)
y_axis_val = st.selectbox('Select Y-axis Value', numeric_cols)
fig, ax = plt.subplots()
sns.scatterplot(x=x_axis_val, y=y_axis_val, hue='Vendor', data=filtered_data, ax=ax)
st.pyplot(fig)

st.header('Summary Statistics')
st.write(filtered_data.describe())

st.header('Dynamic Line Chart for Selected Metric')
metric_selection = st.selectbox('Select a metric to visualize', numeric_cols)
fig, ax = plt.subplots()
for vendor in selected_vendors:
    vendor_data = filtered_data[filtered_data['Vendor'] == vendor]
    vendor_data = vendor_data.groupby(filtered_data['Release Date'].dt.year)[metric_selection].mean()
    ax.plot(vendor_data, label=vendor)
ax.set_xlabel('Year')
ax.set_ylabel(metric_selection)
ax.legend()
st.pyplot(fig)

st.header('Vendor Performance Comparison')
comparison_metric = st.selectbox('Select a metric for comparison', numeric_cols)
fig, ax = plt.subplots()
sns.boxplot(x='Vendor', y=comparison_metric, data=filtered_data, ax=ax)
st.pyplot(fig)

st.header('Interactive Data Table')
columns_to_display = st.multiselect('Select columns to display', data.columns)
st.write(filtered_data[columns_to_display])

st.download_button(label='Download Data as CSV', data=filtered_data.to_csv(index=False), file_name='filtered_data.csv', mime='text/csv')

st.header('User Feedback')
feedback = st.text_area("Share your feedback or suggestions here:")
if st.button('Submit Feedback'):
    st.write('Thank you for your feedback!')


