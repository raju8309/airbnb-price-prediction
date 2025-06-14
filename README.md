# 🏠 Airbnb Price Prediction (NYC) — Data Science + Streamlit App

This project uses real-world Airbnb listing data from New York City to predict the nightly rental price of a listing based on features like room type, location, availability, and reviews. It includes end-to-end data cleaning, machine learning, model evaluation, and deployment via Streamlit.

---

## 🚀 Live Demo

👉 [Click here to use the live app](https://your-username.streamlit.app)  
_(replace this link with your actual Streamlit Cloud URL)_

---

## 📂 Project Structure

```
airbnb-price-prediction/
├── app/
│   ├── app.py                 # Streamlit app
│   ├── price_model.pkl        # Trained ML model
│   └── model_columns.pkl      # Feature columns used in the model
├── data/
│   └── AB_NYC_2019.csv        # Raw dataset from Kaggle
├── models/
│   └── (optional if moved to app/)
├── notebook/
│   └── airbnb_price_model.ipynb  # Jupyter Notebook for analysis & training
├── requirements.txt
└── README.md
```

---

## 🔍 Problem Statement

> Airbnb hosts often struggle to choose the right price for their listings. This project helps them by predicting a fair and competitive nightly price based on the listing's features using machine learning.

---

## 📊 Features Used for Prediction

- Location (latitude, longitude)
- Room type (entire home, private room, shared)
- Neighbourhood group (Manhattan, Brooklyn, etc.)
- Number of reviews
- Reviews per month
- Minimum nights
- Availability
- Host listing count

---

## 🧪 Machine Learning Workflow

1. **Data Cleaning**  
   - Removed outliers and irrelevant columns  
   - Handled missing values  

2. **EDA (Exploratory Data Analysis)**  
   - Visualized trends with `Seaborn` and `Matplotlib`

3. **Feature Engineering**  
   - One-hot encoded categorical variables  
   - Removed high-cardinality fields (like raw neighborhood names)

4. **Modeling**  
   - Used `LinearRegression` for interpretability  
   - Evaluated using MAE, RMSE, R²  

5. **Deployment**  
   - Streamlit app where users input listing details and get a predicted price

---

## 📈 Model Performance

- **MAE**: ~$56  
- **RMSE**: ~$93  
- **R² Score**: ~0.32

💡 A good start for a linear model. Can be improved further with XGBoost or Random Forests.

---

## 📦 How to Run Locally

1. **Clone this repo**
```bash
git clone https://github.com/your-username/airbnb-price-prediction.git
cd airbnb-price-prediction
```

2. **Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Launch the app**
```bash
cd app
streamlit run app.py
```

---

## 🌍 Deployment

Deployed using **Streamlit Cloud**.  
To deploy your own version:

- Push the repo to GitHub
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Connect your repo
- Set `app/app.py` as the entry point
- Add model files and `requirements.txt`

---

## 📚 Dataset

Source: [NYC Airbnb Open Data on Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

---

## 🙌 Author

**Raju Kotturi**  
Aspiring Data Scientist, Python & Web Developer  
📍 Based in the US | 🎯 Seeking real-world DS opportunities  
📫 [LinkedIn](https://www.linkedin.com/in/your-link) | [GitHub](https://github.com/your-username)

---

## 📌 Future Work

- Improve model with ensemble methods (XGBoost, Random Forest)
- Add map-based visualizations
- Create price heatmaps for hosts
- Deploy with Docker or Hugging Face Spaces
