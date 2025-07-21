import torch
print(torch.__version__)

device_count = torch.cuda.device_count()
print("Number of GPUs Available: ", device_count)
