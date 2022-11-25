from PIL import Image
import torch
from torch.utils.data import Dataset

img = Image.open('flower_photos/')
print(img)