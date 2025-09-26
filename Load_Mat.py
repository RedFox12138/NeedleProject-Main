import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from scipy.io import loadmat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os
import glob

# 简单缓存，避免文件未变化时重复IO与绘图
_cached_latest_path = None
_cached_latest_mtime = None
_cached_pixmap = None


def find_latest_mat_file(folder_path):
    """查找指定文件夹中最新的.mat文件"""
    # 获取所有.mat文件
    mat_files = glob.glob(os.path.join(folder_path, '*.mat'))

    if not mat_files:
        print("文件夹中没有找到.mat文件")
        return None

    # 按修改时间排序，获取最新的文件
    latest_file = max(mat_files, key=os.path.getmtime)
    # print(f"找到最新的MAT文件: {latest_file}")
    return latest_file


def _extract_signal_from_mat_dict(data, signal_name):
    """从loadmat返回的字典里提取目标信号为一维numpy数组。找不到返回None。"""
    # 直接键访问
    if signal_name in data:
        signal_data = data[signal_name]
    else:
        # 在可能的结构体变量里探测
        matlab_vars = [key for key in data.keys() if not key.startswith('__')]
        signal_data = None
        for var_name in matlab_vars:
            val = data[var_name]
            if hasattr(val, 'dtype') and getattr(val.dtype, 'names', None):
                if signal_name in val.dtype.names:
                    try:
                        # 典型结构体访问 [0][0][field]
                        signal_data = val[0][0][signal_name]
                        break
                    except Exception:
                        pass
    if signal_data is None:
        return None

    # 归一为1维数组
    if hasattr(signal_data, 'shape'):
        arr = np.array(signal_data)
        if arr.ndim > 1:
            arr = arr.flatten()
        elif arr.ndim == 0:
            arr = np.array([arr])
    elif isinstance(signal_data, (list, tuple)):
        arr = np.array(signal_data).flatten()
    else:
        arr = np.array([signal_data]).flatten()

    # 转为float，便于后处理
    with np.errstate(all='ignore'):
        arr = arr.astype(float, copy=False)
    return arr


def load_and_plot_latest_mat_signals(folder_path):
    """加载最新MAT文件并绘制I-V曲线（横轴V，纵轴I），返回QPixmap。

    - 仅绘制一张图，将'I'与'V'画到同一张图（I随V变化）。
    - 内置简单缓存：当最新文件路径与修改时间未变化时，直接返回上次生成的Pixmap，避免重复IO与绘图。
    """
    global _cached_latest_path, _cached_latest_mtime, _cached_pixmap
    try:
        # 查找最新的.mat文件
        file_path = find_latest_mat_file(folder_path)
        if file_path is None:
            return None

        current_mtime = os.path.getmtime(file_path)
        if (
            _cached_pixmap is not None and
            _cached_latest_path == file_path and
            _cached_latest_mtime == current_mtime
        ):
            # 文件未变化，直接返回缓存
            return _cached_pixmap

        # 加载MAT文件
        data = loadmat(file_path)

        # 提取I与V
        I = _extract_signal_from_mat_dict(data, 'I')
        V = _extract_signal_from_mat_dict(data, 'V')
        if I is None or V is None:
            print('未找到信号 I 或 V')
            return None

        # 对齐长度
        n = min(len(I), len(V))
        if n == 0:
            print('I/V 信号为空')
            return None
        I = I[:n]
        V = V[:n]

        # 清洗非法值
        mask = np.isfinite(I) & np.isfinite(V)
        if not mask.any():
            print('I/V 信号均为非有限值')
            return None
        I = I[mask]
        V = V[mask]

        # 可选：按V排序，曲线更平滑（尤其是回扫时可考虑不排序或颜色区分）
        order = np.argsort(V)
        V_sorted = V[order]
        I_sorted = I[order]

        # 创建图像（单张I-V曲线）
        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
        ax.plot(V_sorted, I_sorted, '-', linewidth=1.2, color='tab:blue')
        ax.set_title(f'I–V 曲线: {os.path.basename(file_path)}', fontsize=11)
        ax.set_xlabel('V', fontsize=10)
        ax.set_ylabel('I', fontsize=10)
        ax.grid(True, alpha=0.35)
        fig.tight_layout()

        # 转换为QPixmap（深拷贝图像数据，避免潜在访问冲突导致的0xC0000005闪退）
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        width, height = canvas.get_width_height()
        # buffer_rgba返回的是内存视图，其生命周期与canvas/fig绑定；copy()确保深拷贝
        qimage = QImage(canvas.buffer_rgba(), width, height, QImage.Format_RGBA8888).copy()
        pixmap = QPixmap.fromImage(qimage)

        plt.close(fig)

        # 更新缓存
        _cached_latest_path = file_path
        _cached_latest_mtime = current_mtime
        _cached_pixmap = pixmap

        return pixmap

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return None