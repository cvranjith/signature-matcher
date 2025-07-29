import torch
import torch.nn as nn
import timm

class Embedder(nn.Module):
    def __init__(self):
        super().__init__()
        self.backbone = timm.create_model("mobilenetv2_100", pretrained=True, features_only=True)
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(self.backbone.feature_info[-1]["num_chs"], 128)

    def forward(self, x):
        features = self.backbone(x)[-1]
        pooled = self.pool(features).flatten(1)
        return self.fc(pooled)
