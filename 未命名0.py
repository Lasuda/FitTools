# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 16:50:27 2025

@author: LasudaR9000
"""

""" 非线性拟合示例 """

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import fittools as fs




# 定义要拟合的函数
def func(x, a, b):
    return a * np.exp(b * x)


# 生成一些示例数据
x = np.array([1, 2, 3, 4, 5])
y = func(x, 2.5, 1.3)
# 添加一些噪声
y_noisy = y + 0.2 * np.random.normal(size=len(x))

# 进行非线性拟合
popt, pcov = curve_fit(func, x, y_noisy)

# 计算置信区间
lowerupper = fs.FitConfInt(popt, pcov, x)

# 输出结果
for i, (param, low) in enumerate(zip(popt, lowerupper)):
    print(f"参数 {i + 1}: {param:.3f}, 95% 置信区间: (\pm {low:.3f})")

# 生成拟合曲线的 x 值
x_fit = np.linspace(min(x), max(x), 100)
y_fit = func(x_fit, *popt)

# 绘制原始数据和拟合曲线
plt.scatter(x, y_noisy, label='Original data')
plt.plot(x_fit, y_fit, 'r-', label='Fitted curve')
plt.legend()
plt.show()
    