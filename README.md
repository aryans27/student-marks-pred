# 🎓 Student Performance Prediction Web Application

A machine learning-powered web application built with **Flask** that predicts student academic performance based on various demographic and educational attributes. The application provides an intuitive user interface for input, handles preprocessing, and returns performance predictions using a trained **CatBoost** model.

---

## 🚀 Features

- 🧠 **Machine Learning Model**: Uses a trained CatBoost model for accurate predictions.
- 🖥️ **Web Interface**: Responsive frontend built with HTML, CSS, and JavaScript.
- 🔍 **EDA & Model Training**: Includes Jupyter notebooks for data exploration and model development.
- 🔧 **Data Preprocessing Pipeline**: Scalable and modular data processing components.
- 🧰 **Logging & Exception Handling**: Custom logging and error-handling for easier debugging.
- 📦 **Reusable Codebase**: Clean, modular Python code in `src/` for training and inference pipelines.

---

## 🗂️ Project Structure

```
student-marks-pred/
├── app.py                    # Main Flask application
├── artifacts/                # Saved models and preprocessors
├── notebooks/                # EDA and model training notebooks
│   ├── data_preprocessing.ipynb
│   └── model_training.ipynb
├── src/                      # Core application logic
│   ├── components/           # Data loading, transformation, model handling
│   ├── pipeline/             # Training and prediction pipelines
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py          # Custom exceptions
│   ├── logger.py             # Logging configuration
│   └── utils.py              # Utility functions
├── static/                   # Static frontend assets
│   ├── bg-img.jpg
│   ├── scripts.js
│   └── style.css
├── templates/                # HTML templates
│   ├── index.html            # Home page
│   └── home.html             # Prediction form page
├── requirements.txt          # Python dependencies
├── setup.py                  # Setup script (if packaging)
├── .gitignore
└── README.md                 # You're here!
```

---

## 🖼️ Screenshots

Here’s how the application works when running locally:

**🔹 Initial Form Page – Before Prediction**  
The user is prompted to fill in relevant student information.

👉 [View Screenshot](https://drive.google.com/file/d/1tdmXNPfEeoDD6Droy9JxYs3-5IuF68Kf/view?usp=sharing)

---

**🔹 Output Page – After Submitting**  
Once the form is submitted, the predicted performance score is displayed.

👉 [View Screenshot](https://drive.google.com/file/d/1HGFpBtm01FH3tolmnLgN3Mdd8SG0nfHv/view?usp=sharing)

---

## 🧪 Model Details

- **Algorithm**: CatBoost Regressor
- **Input Features**:
  - Gender
  - Race/Ethnicity
  - Parental Education Level
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score
- **Processing**:
  - StandardScaler for numeric features
  - Label encoding for categorical data
- **Output**: Predicted math score or performance score

Model artifacts are saved in `artifacts/model.pkl` and used during inference.

---

## 📦 Requirements

- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy
- CatBoost

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aryans27/student-marks-pred.git
   cd student-marks-pred
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   # or
   source myenv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

1. **Start the Flask server**:

   ```bash
   python app.py
   ```

2. **Open your browser and navigate to**:

   ```
   http://localhost:5000
   ```

3. **Enter student details** on the prediction page:
   - Gender
   - Race/Ethnicity
   - Parental Education
   - Lunch Type
   - Test Prep Course
   - Reading Score
   - Writing Score

4. **Submit the form** to get the predicted performance score.

---

## 📊 Development & Training

- **Exploratory Data Analysis** and **Model Training** are available in the `notebooks/` directory.
- **Prediction logic** resides in `src/pipeline/predict_pipeline.py`
- **Training logic** is handled by `src/pipeline/train_pipeline.py`

To retrain the model or extend functionality, modify the relevant pipeline or notebooks.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Dataset Source: *https://www.kaggle.com/datasets/spscientist/students-performance-in-exams/data*
- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [CatBoost](https://catboost.ai/)

---

## 💡 Future Improvements

- Add deployment via Docker or Heroku
- Integrate database support for logging predictions
- Support for multiple model comparisons
- Improve UI with modern frameworks like React or Vue

---
