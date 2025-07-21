import torch

# 生成相同随机数据（CPU和GPU）
size = 1000
x_cpu = torch.randn(size, size, device="cpu")  # CPU数据（FP32）
x_gpu = x_cpu.clone().to("cuda")               # GPU数据（FP32）

# 计算矩阵乘法
result_cpu = x_cpu @ x_cpu
result_gpu = x_gpu @ x_gpu

# 同步GPU操作并比较
torch.cuda.synchronize()
try:
    assert torch.allclose(result_cpu, result_gpu.cpu(), atol=1e-5, rtol=1e-5)
    print("结果一致（FP32）")
except AssertionError:
    # 尝试使用FP64（双精度）减少误差
    x_cpu = x_cpu.to(torch.float64)
    x_gpu = x_gpu.to(torch.float64)
    result_cpu = x_cpu @ x_cpu
    result_gpu = x_gpu @ x_gpu
    torch.cuda.synchronize()
    assert torch.allclose(result_cpu, result_gpu.cpu(), atol=1e-10, rtol=1e-10)
    print("结果一致（FP64）")