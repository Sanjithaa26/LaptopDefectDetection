<h1 align="center">
  <img alt="Laptop Defect Detection AI" src="https://img.icons8.com/external-flatart-icons-outline-flatarticons/120/000000/external-laptop-computer-flatart-icons-outline-flatarticons.png" width="150px"/>
</h1>

<div align="center">

<!-- [![License](https://img.shields.io/github/license/Sanjithaa26/LaptopDefectDetection)](LICENSE)   -->
[![Framework](https://img.shields.io/badge/Backend-Flask-blue)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React-green)](https://react.dev/)
[![Models](https://img.shields.io/badge/Models-YOLOv8%20%7C%20ResNet50%20%7C%20MobileNetV2-purple)]()
[![Deploy](https://img.shields.io/badge/Deployed%20On-Render-green)](https://render.com/)
[![Dataset](https://img.shields.io/badge/Dataset-Roboflow%20%7C%20Kaggle%20%7C%20Amazon%20%7C%20Flipkart%20%7C%20Google-orange)]()

</div>

---

# Laptop Defect Detection AI

This project is an end-to-end web application that leverages deep learning and computer vision to automatically detect defects in laptop images. 
Users can upload individual images or entire folders of laptop photos, select from three models (ResNet-50, YOLOv8, MobileNetV2) and receive instant predictions about the presence and type of defects. 
The backend is powered by trained neural networks, while the frontend provides an intuitive interface for uploading, processing and visualizing results, including annotated images and confidence scores. 
This tool streamlines quality control for laptop hardware by enabling fast, automated and accurate defect identification.

---

## Features

- **Upload Options**: Upload single image or an entire folder.
- **Model Selection**: Choose between ResNet-50, YOLOv8, MobileNetV2 or run all at once.
- **Visual Feedback**: Displays annotated images (YOLO) and prediction details.
- **Confidence Scores**: Clear metrics with predicted class and model-wise results.
- **Batch Mode**: Automatically processes folders of images in one go.
- **Multi-label Classification**: All the three models handle multi-label (detect all the defects present in the image) defect detection.

---

## Sample Datasets

- **With Defects**: [Roboflow Defective Laptops Dataset](https://universe.roboflow.com/team-ks/broken-laptop-parts/images/)
- **Without Defects**: [Roboflow Clean Laptops Dataset](https://universe.roboflow.com/team-ks/broken-laptop-parts/images/)

---


---

## Models Used

| Model        | Primary Role                            |
|--------------|------------------------------------|
| **ResNet-50** | Hard-to-see and fine defects detection     |
| **YOLOv8**    | Detects multiple defects with exact shape and location using segementation |
| **MobileNetV2** | Quick multi-label defect classification as model is lightweight |

---

---

## Project Structure

```
LaptopDefectDetection/
├── backend/
│   ├── app.py
│   ├── models/
│   └── requirements.txt
├── ui/
│   ├── src/
│   └── package.json
└── README.md
```

---

## Installation

### Backend (Flask + Torch + YOLO)

```bash
git clone https://github.com/yourusername/laptop-defect-detection.git
cd backend
pip install -r requirements.txt
python app.py
```
### Frontend (React)

```bash
cd ../ui
npm install
npm start
```

---

## Usage

1. **Start the backend server**  
    Run the Flask backend as shown above.

2. **Start the frontend**  
    Launch the React app in a separate terminal.

3. **Access the app**  
    Open your browser and go to [http://localhost:3000](http://localhost:3000).

4. **Upload images**  
    Use the interface to upload images or folders, select models and view results.

---



---

## Contributors

- [Sanjitha R](https://github.com/Sanjithaa26)
- [Kiruthika Sermadurai](https://github.com/kiruthikasermadurai)
- [Vinithaa P](https://github.com/vinithaapalanisamy)
- [Durga G](https://github.com/Durgaganapathi)
- [Gayathri R](https://github.com/Gayathri4705)

    
---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [Roboflow](https://roboflow.com/) for datasets
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [PyTorch](https://pytorch.org/)
- [React](https://react.dev/)

---
