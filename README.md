<h1 align="center">
  <img alt="Laptop Defect Detection AI" src="https://img.icons8.com/external-flatart-icons-outline-flatarticons/120/000000/external-laptop-computer-flatart-icons-outline-flatarticons.png" width="150px"/>
</h1>

<div align="center">

<!-- [![License](https://img.shields.io/github/license/Sanjithaa26/LaptopDefectDetection)](LICENSE)   -->
[![Framework](https://img.shields.io/badge/Backend-Flask-blue)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React-green)](https://react.dev/)
[![Models](https://img.shields.io/badge/Models-YOLOv8%20%7C%20ResNet50%20%7C%20MobileNetV2-purple)]()
[![Deploy](https://img.shields.io/badge/Deployed%20On-Render-green)](https://render.com/)
[![Dataset](https://img.shields.io/badge/Dataset-Roboflow-orange)](https://universe.roboflow.com/team-ks/broken-laptop-parts/images/)

</div>

---

# 💻 Laptop Defect Detection AI

An end-to-end AI-powered web application for identifying laptop defects using computer vision and deep learning. The system supports real-time detection from single images or batch uploads, powered by three models: **ResNet-50**, **YOLOv8**, and **MobileNetV2**.

🌟 Ideal for quality control teams in laptop manufacturing, refurbishing, or repair sectors.

---

## 🔍 Features

- 📦 **Upload Options**: Upload single image or entire folders.
- 🔀 **Model Selection**: Choose between ResNet-50, YOLOv8, MobileNetV2 or run all at once.
- 📸 **Visual Feedback**: Displays annotated images (YOLO) and prediction details.
- 📈 **Confidence Scores**: Clear metrics with predicted class and model-wise results.
- 🔁 **Batch Mode**: Automatically processes folders of images in one go.
- 🧠 **Multi-label & Binary Classification**: MobileNet handles multi-label (type-wise) defect detection, others perform binary classification.

---

## 📸 Sample Datasets

- 🔧 **With Defects**: [Roboflow Defective Laptops Dataset](https://universe.roboflow.com/team-ks/broken-laptop-parts/images/)
- ✅ **Without Defects**: [Roboflow Clean Laptops Dataset](https://universe.roboflow.com/team-ks/broken-laptop-parts/images/)

---

## 🚀 Demo

Watch the web app in action:

> ⚠️ _Insert your demo video or hosted app link here if available_

---

## 🧠 Models Used

| Model        | Purpose                            | Type                     |
|--------------|------------------------------------|--------------------------|
| **ResNet-50** | Defect or No Defect                | Binary Classification    |
| **YOLOv8**    | Object-level defect detection + annotation | Object Detection     |
| **MobileNetV2** | Detect specific types of defects (e.g. keyboard crack, screen damage) | Multi-label Classification |

---

## 🛠️ Installation

### 🧰 Backend (Flask + Torch + YOLO)

```bash
git clone https://github.com/yourusername/laptop-defect-detection.git
cd backend
pip install -r requirements.txt
python app.py
```
### 🌐 Frontend (React)

```bash
cd ../frontend
npm install
npm start
```

---

## ⚙️ Usage

1. **Start the backend server**  
    Run the Flask backend as shown above.

2. **Start the frontend**  
    Launch the React app in a separate terminal.

3. **Access the app**  
    Open your browser and go to [http://localhost:3000](http://localhost:3000).

4. **Upload images**  
    Use the interface to upload images or folders, select models, and view results.

---

## 📂 Project Structure

```
LaptopDefectDetection/
├── backend/
│   ├── app.py
│   ├── models/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
└── README.md
```

---

## 📝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests for improvements and bug fixes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Roboflow](https://roboflow.com/) for datasets
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [PyTorch](https://pytorch.org/)
- [React](https://react.dev/)

---