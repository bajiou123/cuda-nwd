import torch
from torch import nn

# 1. 定义模型并移动到GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model = nn.Linear(10, 2).to(device)  # 关键：.to(device)

# 2. 准备数据并移动到GPU
input_data = torch.randn(5, 10).to(device)  # 关键：.to(device)

# 3. 运行推理
output = model(input_data)
print("输出形状:", output.shape)  # 应输出torch.Size([5, 2])