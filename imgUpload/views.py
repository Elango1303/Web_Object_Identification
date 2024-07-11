from django.shortcuts import render
from .forms import ImageUploadForm
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from django.http import HttpResponse
import numpy as np

def handle_upload_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_upload_file(request.FILES['image'])

        model = ResNet50(weights='imagenet')
        img_path = 'img.jpg'

        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded_preds = decode_predictions(preds, top=3)[0]

        predictions = []
        for pred in decoded_preds:
            predictions.append((pred[1], np.round(pred[2] * 100, 2)))

        return render(request, 'result.html', {'predictions': predictions})

    return HttpResponse("Processing completed")
