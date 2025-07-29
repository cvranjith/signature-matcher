from model import Embedder
import cv2
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import torchvision.transforms as T

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = Embedder().to(device)
model.eval()

transform = T.Compose([
    T.ToPILImage(),
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def preprocess(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    tensor = transform(img).unsqueeze(0).to(device)
    return tensor

def compare_signatures(path1, path2):
    img1 = preprocess(path1)
    img2 = preprocess(path2)
    with torch.no_grad():
        emb1 = model(img1).cpu().numpy()
        emb2 = model(img2).cpu().numpy()
    score = cosine_similarity(emb1, emb2)[0][0]
    percent = float(score) * 100
    if percent >= 95:
        label = f"✅ Exact Match ({percent:.2f}%)"
    elif percent >= 80:
        label = f"🟢 High Match ({percent:.2f}%)"
    elif percent >= 50:
        label = f"🟡 Moderate Match ({percent:.2f}%)"
    elif percent >= 10:
        label = f"🟠 Weak Match ({percent:.2f}%)"
    else:
        label = f"🔴 No Match ({percent:.2f}%)"
    return label
