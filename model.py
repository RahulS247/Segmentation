import torch
import torch.nn as nn
import torchvision.transforms.funcitonal as TF


class DoubleConv(nn.Module):
    def __init__(self,in_channels,out_channels):
        super(DoubleConv,self).__init__()
        self.conv= nn.Sequential(
            nn.Conv2d(in_channels,out_channels,3,1,1,bias=False),
            nn.Bat
        )















print("Hello")