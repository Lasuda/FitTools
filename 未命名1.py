# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 17:00:28 2025

@author: LasudaR9000
"""

""" 共享参数拟合示例 """

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# from scipy.stats import t
import fittools as fs



# 定义统一的拟合函数
def shared_fit_func(x, a, b, *c):
    """
    统一的拟合函数，x 是合并后的自变量，a 和 b 是共享参数，c 是每条曲线的独立参数
    """
    num_curves = len(c)
    num_points_per_curve = len(x) // num_curves
    y = np.zeros_like(x)
    for i in range(num_curves):
        start = i * num_points_per_curve
        end = (i + 1) * num_points_per_curve
        y[start:end] = a * np.exp(b * x[start:end]) + c[i]
    return y

# 生成示例数据
# 曲线 1 的真实参数
a_true = 2
b_true = 0.5
c1_true = 1
# 曲线 2 的真实参数
c2_true = 2

# 生成曲线 1 的数据
x1 = np.linspace(0, 5, 50)
y1 = a_true * np.exp(b_true * x1) + c1_true + np.random.normal(0, 0.1, len(x1))

# 生成曲线 2 的数据
x2 = np.linspace(0, 5, 50)
y2 = a_true * np.exp(b_true * x2) + c2_true + np.random.normal(0, 0.1, len(x2))

# 合并数据
x_combined = np.concatenate((x1, x2))
y_combined = np.concatenate((y1, y2))

# 初始猜测值
p0 = [1, 0.1, 0, 0]

# 进行拟合
popt, pcov = curve_fit(shared_fit_func, x_combined, y_combined, p0=p0)

lowerupper = fs.FitConfInt(popt, pcov, x_combined, alpha=0.05)

# 提取拟合结果
a_fit, b_fit = popt[:2]
c_fits = popt[2:]

print(f"拟合得到的共享参数 a: {a_fit}, b: {b_fit}")
print(f"拟合得到的独立参数 c: {c_fits}")
for i, (param, low) in enumerate(zip(popt, lowerupper)):
    print(f"参数 {i + 1}: {param:.3f}, 95% 置信区间: (\pm {low:.3f})")

# 绘制原始数据和拟合曲线
plt.scatter(x1, y1, label='Curve 1 data')
plt.scatter(x2, y2, label='Curve 2 data')

y1_fit = a_fit * np.exp(b_fit * x1) + c_fits[0]
y2_fit = a_fit * np.exp(b_fit * x2) + c_fits[1]

plt.plot(x1, y1_fit, 'r-', label='Curve 1 fit')
plt.plot(x2, y2_fit, 'g-', label='Curve 2 fit')

plt.legend(frameon=False)
# plt.savefig('cos_function.svg', format='svg',transparent=True)
    