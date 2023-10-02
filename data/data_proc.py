import pandas as pd

# Read data from each file into dataframes
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

# Filter rows where the "product" field is "pink morse" in each dataframe
filtered_df1 = df1[df1['product'] == 'pink morsel']
filtered_df2 = df2[df2['product'] == 'pink morsel']
filtered_df3 = df3[df3['product'] == 'pink morsel']

# Concatenate the filtered dataframes vertically
combined_df = pd.concat([filtered_df1, filtered_df2, filtered_df3], ignore_index=True)

# Remove the dollar sign and convert the "price" column to numeric
combined_df['price'] = combined_df['price'].str.replace('$', '').astype(float)

# Multiply the "price" and "quantity" columns to create the "sales" column
combined_df = combined_df.assign(sales=combined_df['price'] * combined_df['quantity'])

# Keep only the "sales" and "region" columns
combined_df = combined_df[['sales', 'date', 'region']]

# Write the combined dataframe to a new file
combined_df.to_csv('data/processed_data.csv', index=False)
