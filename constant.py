PATH = 'C:/Users/ROHIT KUMAR/code/ml/plant-disease-model1.pth'

class_list = ['Apple___Apple_scab',
              'Apple___Black_rot',
              'Apple___Cedar_apple_rust',
              'Apple___healthy',
              'Blueberry___healthy',
              'Cherry_(including_sour)___Powdery_mildew',
              'Cherry_(including_sour)___healthy',
              'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
              'Corn_(maize)___Common_rust_',
              'Corn_(maize)___Northern_Leaf_Blight',
              'Corn_(maize)___healthy',
              'Grape___Black_rot',
              'Grape___Esca_(Black_Measles)',
              'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
              'Grape___healthy',
              'Orange___Haunglongbing_(Citrus_greening)',
              'Peach___Bacterial_spot',
              'Peach___healthy',
              'Pepper,_bell___Bacterial_spot',
              'Pepper,_bell___healthy',
              'Potato___Early_blight',
              'Potato___Late_blight',
              'Potato___healthy',
              'Raspberry___healthy',
              'Soybean___healthy',
              'Squash___Powdery_mildew',
              'Strawberry___Leaf_scorch',
              'Strawberry___healthy',
              'Tomato___Bacterial_spot',
              'Tomato___Early_blight',
              'Tomato___Late_blight',
              'Tomato___Leaf_Mold',
              'Tomato___Septoria_leaf_spot',
              'Tomato___Spider_mites Two-spotted_spider_mite',
              'Tomato___Target_Spot',
              'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
              'Tomato___Tomato_mosaic_virus',
              'Tomato___healthy']

plant_detail = [
    dict(
        name="Apple",
        disease=[
            "Apple_scab",
            "Black_rot",
            "Cedar_apple_rust"
        ],
        urls=[
            "https://nationaltoday.com/wp-content/uploads/2021/10/Apple-Tree-Day.jpg"
        ]
    ),
    dict(
        name="Blueberry",
        disease=[]
    ),
    dict(
        name="Cherry",
        disease=[
            "Powdery mildew"
        ]
    ),
    dict(
        name="Corn",
        disease=[
            "Cercospora leaf spot Gray leaf spot",
            "Common Rust",
            "Northern Leaf Blight"
        ]
    ),
    dict(
        name="Grape",
        disease=[
            "Black Rot",
            "Esca (Black Measles)",
            "Leaf Blight (Isariopsis Leaf Spot)"
        ]
    ),
    dict(
        name="Orange",
        disease=[
            "Haunglongbing (Citrus greening)"
        ]
    ),
    dict(
        name="Peach",
        disease=[
            "Bacterial spot",
        ]
    ),
    dict(
        name="Potato",
        disease=[
            "Early Blight",
            "Late Blight"
        ]
    ),
    dict(
        name="Raspberry",
        disease=[]
    ),
    dict(
        name="Soybean",
        disease=[]
    ),
    dict(
        name="Squash",
        disease=[
            "Powdery Mildew"
        ]
    ),
    dict(
        name="Strawberry",
        disease=[
            "Leaf Scorch"
        ]
    ),
    dict(
        name="Tomato",
        disease=[
            "Bacterial Spot",
            "Early blight",
            "Late Blight",
            "Leaf Mold",
            "Leaf Blight",
            "Septoria Leaf Spot",
            "Spider Mites Two spotted",
            "Target Spot",
            "Yellow Leaf Curl Virus",
            "Mosaic Virus"
        ]
    )

]

plant_list = [
    "Apple",
    "Blueberry",
    "Cherry",
    "Corn",
    "Grape",
    "Orange",
    "Peach",
    "Pepper,",
    "Potato",
    "Raspberry",
    "Soybean",
    "Squash",
    "Strawberry",
    "Tomato"
]
