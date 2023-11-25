import pandas as pd
import plotly.express as px

# Sample DataFrame
data = {'Column1': [1, 2, 3, 1, 2, 3, 1, 2, 3]}
df = pd.DataFrame(data)

# Count unique values in 'Column1'
unique_counts = df['Column1'].value_counts().reset_index()

# Rename the columns for clarity
unique_counts.columns = ['Unique Values', 'Count']

# Create an interactive bar plot using Plotly Express
fig = px.bar(unique_counts, x='Unique Values', y='Count', title='Interactive Bar Plot of Unique Values Counts')

# Save the plot as an HTML file
fig.write_html('interactive_bar_plot.html')
fig.show()