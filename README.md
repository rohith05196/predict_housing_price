# 🏡 House Price Prediction Web App

This repository contains a machine learning-powered Flask web application that predicts house prices. It uses a trained regression model and a web frontend to allow users to input features and receive price predictions.

## 🚀 Features

- Machine learning model (trained regression) for house pricing
- Flask web app with HTML/CSS frontend
- Docker support for easy deployment
- Heroku compatibility (via `Procfile`)
- Static and template directories for UI elements
- Jupyter notebook for EDA and model training

---

## 📁 Project Structure

```bash
.
├── .github/workflows/      # GitHub Actions workflows
├── static/images/          # Static files (e.g., CSS, images)
├── templates/              # HTML templates for rendering pages
├── .gitignore              # Ignored files for Git
├── DockerFile              # Dockerfile for containerization
├── HousePricing.ipynb      # Jupyter notebook for training and analysis
├── LICENSE                 # Project license
├── Procfile                # Heroku deployment configuration
├── README.md               # Project documentation (you are here)
├── app.py                  # Main Flask application
├── reg_predict.pickle      # Trained regression model
├── requirements.txt        # Python dependencies
├── scalar.pickle           # Feature scaler used during training
```

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/house-price-predictor.git
   cd house-price-predictor
   ```

2. **Create a virtual environment**
   ```bash
   conda create --name housepred python=3.9
   conda activate housepred
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

Then open your browser and go to `http://127.0.0.1:5000/`.

---

## 🐳 Docker Deployment

To build and run the app using Docker:

```bash
docker build -t house-pricing-app .
docker run -p 5000:5000 house-pricing-app
```

---

## 🌐 Deploying to Heroku

1. Commit all your files.
2. Push to a Heroku remote.
3. Heroku will detect the `Procfile` and deploy accordingly.

---

## 📊 Model Details

- Trained using regression techniques on housing data
- Scaling applied using `scalar.pickle`
- Model file: `reg_predict.pickle`

For more details, check the `HousePricing.ipynb` notebook.
