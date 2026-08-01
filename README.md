# Telecom Customer Churn Prediction 📞📉

## Project Goal
The primary objective of this project is to develop a predictive model to identify the probability of a customer terminating their telecommunication services (Churn) based on historical data.

## Data Processing & EDA
- **Exploratory Data Analysis (EDA):** Analyzed the distribution of the target variable and explored feature correlations using Matplotlib and Seaborn.
- **Data Preprocessing:** 
  - Handled missing values (dropped rows with missing traffic data, filled missing contract durations with 0).
  - Dropped irrelevant columns (e.g., `id`).
  - Applied `StandardScaler` to normalize numerical features.

## Model Details & Evaluation
- **Algorithm:** Random Forest Classifier (`n_estimators=100`)
- The model was trained and evaluated using the following metrics:
  - **Accuracy:** ~94.2%
  - **Precision:** ~95.8%
  - **Recall:** ~93.6%
  - **F1 Score:** ~94.7%
  
These metrics indicate a highly effective model for identifying potential churners while minimizing false positives.

## Project Structure
telecom-churn-prediction/
│
├── data/
│   └── internet_service_churn.csv   # Raw dataset
├── notebooks/
│   └── 1_eda.ipynb                  # Jupyter notebook with EDA, Modeling, and Prediction function
├── README.md                        # Project documentation
├── .gitignore                       # Ignored files for Git

## How to Run
### Local Execution
1. Clone the repository.
2. Install the required dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `jupyter`.
3. Open `notebooks/1_eda.ipynb` in Jupyter Notebook or PyCharm and run the cells sequentially.

### Usage Example
The project includes a `predict_churn` function that takes a new customer's data and predicts their churn probability:
```python
new_customer = [1, 0, 2.0, 20, 0.0, 3, 10.0, 2.0, 0]
predict_churn(new_customer, rf_model, scaler)

# Output:
# Churn Probability: 85.00%
# Result: The client has a high probability of churn ⚠️
