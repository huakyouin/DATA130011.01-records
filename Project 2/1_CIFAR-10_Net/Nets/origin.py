import torch
import torch.nn as nn
from torchvision.models import resnet

def ResNet_original():
    model = resnet.resnet18(pretrained=False)
    model.avgpool = nn.AdaptiveAvgPool2d((1, 1))
    model.fc = nn.Sequential(
                nn.BatchNorm1d(512*1),
                nn.Linear(512*1,10),
            )
    return model