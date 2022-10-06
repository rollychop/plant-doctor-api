import torch
import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import constant
import plant
import resnet9
import util
from plant import plants
from resnet9 import ResNet9

app = FastAPI()

model = ResNet9(3, 38)
model.load_state_dict(
    torch.load(
        constant.PATH,
        map_location=torch.device('cpu')
    )
)
model.eval()


@app.get('/')
async def home():
    return "Home"


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
) -> str:
    bb = await file.read()
    img = util.byteToPIL(bb)
    tt = util.pilToTensorCompose()  # transformation
    img_tensor = tt(img).unsqueeze(0)  # converting into batches
    p = resnet9.predict_image(img_tensor, model)
    cls = constant.class_list[p]
    item = list(filter(lambda x: str(x.name).lower() in cls.lower(), plant.plants))
    return item[0].set_disease(cls.split('___')[1].replace('_', ' '))


@app.get('/plant-list')
async def get_plant_list() -> JSONResponse:
    json_compatible_item_data = jsonable_encoder(plants)
    return JSONResponse(content=json_compatible_item_data)


@app.get('/plant-detail')
async def get_plant_detail():
    return dict(
        plantDetail=constant.plant_detail
    )


@app.get("/plant")
async def get_plant(id_: int):
    match = list(filter(lambda x: x.id == id_, plants))
    if len(match) >= 1:
        return match[0]
    else:
        return None


if __name__ == '__main__':
    uvicorn.run(app)
