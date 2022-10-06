from io import BytesIO

from PIL import Image
from torchvision.transforms import transforms, Compose


def byteToPIL(bb: bytes) -> Image:
    return Image.open(BytesIO(bb))


stats = ((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))


def pilToTensorCompose() -> Compose:
    convert_tensor = transforms.Compose(
        [
            transforms.Resize(256, antialias=True),
            transforms.ToTensor(),
            transforms.Normalize(*stats)
        ]
    )
    return convert_tensor
