# Image Classification Web Application with Django and ResNet50

![Image Classification Demo](https://via.placeholder.com/600x300?text=Image+Classification+Demo)

A web application for classifying images using Django as the backend framework and ResNet50 (pretrained on ImageNet) for machine learning predictions.

## Features

- **Simple UI**: Clean interface for uploading images
- **Powerful Backend**: Uses Keras with ResNet50 model for image classification
- **Real-time Predictions**: Displays top 3 predictions with confidence percentages
- **Responsive Design**: Works on both desktop and mobile devices
- **Django-Powered**: Robust backend handling file uploads and processing

## Technologies Used

- **Frontend**:
  - HTML5
  - CSS3

- **Backend**:
  - Django 2.2
  - Python 3.6+

- **Machine Learning**:
  - TensorFlow/Keras
  - ResNet50 (pretrained on ImageNet)

## Project Structure

```
myWebApp/
├── imgUpload/               # Django app for image upload functionality
│   ├── __init__.py
│   ├── admin.py             # Admin configurations
│   ├── apps.py              # App configurations
│   ├── forms.py             # Form for image upload
│   ├── models.py            # Database models
│   ├── tests.py             # Test cases
│   ├── urls.py              # URL routing
│   ├── views.py             # View functions
│   └── templates/           # HTML templates
│       ├── home.html        # Upload page
│       └── result.html      # Results display page
├── manage.py                # Django management script
└── db.sqlite3               # SQLite database
```

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd myWebApp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: The project expects you to have TensorFlow installed. If not, install with:*
   ```bash
   pip install tensorflow
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and navigate to `http://localhost:8000/imgeupload`

## Usage

1. On the home page, click "Choose File" to select an image from your device
2. Click "Upload" to submit the image
3. The system will process the image using ResNet50 and display the top 3 predictions with confidence percentages

## Screenshots

1. **Upload Page**:
   ![Upload Page](https://via.placeholder.com/400x200?text=Upload+Page)

2. **Results Page**:
   ![Results Page](https://via.placeholder.com/400x200?text=Results+Page)

## Customization

To customize the application:

1. **Change Model**:
   Modify `views.py` to use a different pretrained model from Keras applications

2. **Update UI**:
   Edit the templates in `templates/` folder to change the look and feel



