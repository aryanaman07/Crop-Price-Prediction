# Crop-Price-Prediction
---

# AGRI-FORECAST

AGRI-FORECAST is a Streamlit-based web application that predicts future average sales values for agri-horticulture commodities in India using time series analysis and machine learning models like ARIMA and SARIMA. By selecting various parameters, users can access predicted or historical sales values, assisting stakeholders in making informed decisions about commodity prices.

## Features

- **Zone, Season, and Commodity Selection**: Users can specify the geographical zone, season, and commodity type to tailor predictions.
- **Date Selection**: Users can select a specific year and month to view either historical data or a prediction.
- **ML Models for Prediction**: The app utilizes time series models, ARIMA and SARIMA, for accurate forecasting.
- **Results Display**: Displays predicted or historical sales prices based on input parameters.

- Deployed Application
Access the deployed version of AGRI-FORECAST here: https://crop-price-prediction-model.streamlit.app/

## Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/agri-forecast.git
   cd agri-forecast
   ```

2. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **File Structure**:
    - `app.py`: Main Streamlit application file with UI and prediction logic.
    - `requirements.txt`: Lists all required Python libraries.
    - `data/`: Folder containing pickle files with time series data and model predictions.

## Data and Models

The application relies on pre-trained ARIMA and SARIMA models for forecasting commodity prices, stored as pickle files. Each file corresponds to a commodity and contains time series data or model predictions. Place these files in the `data/` directory.

- **Pickle Files**:
  - Files like `combined_series_Dal.pkl` or `combined_series_Gur.pkl` store the pre-trained models and data for specific commodities.
  
## Background Image

The app includes CSS styling to display a natural background. You can change the image by updating the URL in the `app.py` file.

## Usage

1. **Select parameters**: Choose the zone, season, and commodity from the dropdown menus.
2. **Enter a year and month** for the prediction or historical value.
3. **Click "Get Value"** to view the predicted or historical sales price.

## Example

###For instance, selecting "Milk" for "West" zone in "Autumn" 2034 will display the predicted price of Gram Dal for the selected month.

![image](https://github.com/user-attachments/assets/bd2db0c3-68e4-46ef-b374-b8a69ea438ea)


###For instance, selecting "Gram Dal" for "North" zone in "Winter" 2024  will display the predicted price of Gram Dal for the selected month.

![Screenshot 2024-11-01 210610](https://github.com/user-attachments/assets/5c2bfbc2-022e-4238-a23f-b97360fe08dd)



## Future Enhancements

- **Advanced Models** : Future versions may include model improvements with additional parameters.
- **Real-Time Data**: Incorporation of live data updates.
- **Expanded Commodity List**: Add more commodities to address broader user needs.


