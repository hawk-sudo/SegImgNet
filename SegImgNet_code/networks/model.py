import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from networks.U_net import U_Net,U_Net_mid_output
import timm


def get_Model(model_name):
    if model_name == 'Unet':
        model = U_Net(img_ch=3,output_ch=2)
    if model_name == 'U_Net_mid_output':
        model = U_Net_mid_output(img_ch=3,output_ch=2)
    return model
