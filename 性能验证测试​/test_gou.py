import torch
import random
import numpy as np

# 设置全局随机种子（关键！）
seed = 42
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

# 生成数据（明确类型和设备）
size = 1000
x_cpu = torch.randn(size, size, dtype=torch.float32, device="cpu")
x_gpu = x_cpu.clone().to(device="cuda", dtype=torch.float32)

# CPU计算
result_cpu = x_cpu @ x_cpu

# GPU计算（同步后读取）
result_gpu = x_gpu @ x_gpu
torch.cuda.synchronize()  # 强制同步

# 验证结果（调整精度容差）
try:
    assert torch.allclose(
        result_cpu,
        result_gpu.cpu(),
        atol=1e-5,  # FP32允许的绝对误差
        rtol=1e-5   # FP32允许的相对误差
    )
    print("✅ CPU/GPU结果一致（FP32）")
except AssertionError:
    # 若FP32误差过大，尝试FP64
    x_cpu_fp64 = x_cpu.to(torch.float64)
    x_gpu_fp64 = x_gpu.to(torch.float64)
    result_cpu_fp64 = x_cpu_fp64 @ x_cpu_fp64
    result_gpu_fp64 = x_gpu_fp64 @ x_gpu_fp64
    torch.cuda.synchronize()
    assert torch.allclose(
        result_cpu_fp64,
        result_gpu_fp64.cpu(),
        atol=1e-10,  # FP64允许的绝对误差
        rtol=1e-10   # FP64允许的相对误差
    )
    print("✅ CPU/GPU结果一致（FP64）")