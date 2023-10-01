# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('Mall_Customers.csv')

# %%
# Display basic information about the dataset
def display_basic_info(df):
    print("First few rows of the dataset:")
    print(df.head())
    print("\nSummary statistics:")
    print(df.describe())

# Create a pairplot for scatter plots and histograms
def create_pairplot(df, hue_column='Gender'):
    sns.set(style="ticks")
    sns.pairplot(df, hue=hue_column)
    plt.show()

# Create a correlation heatmap
def create_correlation_heatmap(df):
    columns_to_plot = [col for col in df.columns if col != 'Gender']
    corr = df[columns_to_plot].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

def create_overlapping_histograms(df, columns_to_plot):
    plt.figure(figsize=(10, 5))
    for column_name in columns_to_plot:
        sns.histplot(data=df, x=column_name, kde=True, bins=30, label=column_name)

    plt.title("Distribution of Features")
    plt.legend()
    plt.show()
    
# Create a boxplot
def create_boxplot(df, x_column, y_column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=x_column, y=y_column, data=df)
    plt.title(f"{y_column} by {x_column}")
    plt.show()


# %%
display_basic_info(df)

# %%
df.drop('CustomerID', inplace=True, axis=1)

# %%
create_pairplot(df, hue_column='Gender')
create_correlation_heatmap(df)
columns_to_plot = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
create_overlapping_histograms(df, columns_to_plot)
create_boxplot(df, 'Gender', 'Spending Score (1-100)')

# %%
new_column_names = {
    'Spending Score (1-100)': 'Score',
    'Annual Income (k$)': 'Income',
}

df.rename(columns=new_column_names, inplace=True)
df.head()

# %%
df_encoded = pd.get_dummies(df, columns=['Gender'], prefix=['Gender']).astype(int)

# %%
def minmax_scaling(df):
    df_normalized = df.copy()
    for column in df.columns:
        if column != 'Score':  # Exclude the 'score' column from normalization
            df_normalized[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df_normalized

# Call the function to normalize the columns in your DataFrame
normalized_data = minmax_scaling(df_encoded)

# %%
normalized_data.head()

# %%
if normalized_data.isnull().values.any():
    print("There are missing (NaN) values in the DataFrame.")
else:
    print("There are no missing (NaN) values in the DataFrame.")

# %%
print(normalized_data.dtypes)

# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

X = normalized_data.drop(columns=['Score'])

# 'Score' column will be your target variable (y)
y = normalized_data['Score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)
rf_predictions = rf_regressor.predict(X_test)
rf_mse = mean_absolute_error(y_test, rf_predictions)
print("Random Forest Regressor MAE:", rf_mse)

# AdaBoost Regressor
adaboost_regressor = AdaBoostRegressor(n_estimators=50, random_state=42)
adaboost_regressor.fit(X_train, y_train)
adaboost_predictions = adaboost_regressor.predict(X_test)
adaboost_mse = mean_absolute_error(y_test, adaboost_predictions)
print("AdaBoost Regressor MAE:", adaboost_mse)

# k-Nearest Neighbors (KNN) Regressor
knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(X_train, y_train)
knn_predictions = knn_regressor.predict(X_test)
knn_mse = mean_absolute_error(y_test, knn_predictions)
print("K-Nearest Neighbors Regressor MAE:", knn_mse)

# %%
import pickle 

model_filename = 'random_forest_regression_model.pkl'

# Save the trained model to a pickle file
with open(model_filename, 'wb') as file:
    pickle.dump(rf_regressor, file)

print(f"Random Forest Regression Model saved as {model_filename}")


