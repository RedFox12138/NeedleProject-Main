import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from scipy.io import loadmat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


def load_and_plot_mat_signals(file_path):
    """加载MAT文件并绘制四个信号的波形图"""
    try:
        # 加载MAT文件
        data = loadmat(file_path)

        # 提取四个信号 - 处理字典形式的数据
        signals = {}
        signal_names = ['I', 'II', 'V', 'V_source_set']

        for signal_name in signal_names:
            # 尝试不同的访问方式
            if signal_name in data:
                # 直接访问字典键
                signal_data = data[signal_name]
            else:
                # 如果直接访问失败，尝试在MATLAB变量中查找
                matlab_vars = [key for key in data.keys() if not key.startswith('__')]
                found = False
                for var_name in matlab_vars:
                    if hasattr(data[var_name], 'dtype') and data[var_name].dtype.names:
                        # 如果是结构化数组，检查是否包含目标信号名
                        if signal_name in data[var_name].dtype.names:
                            signal_data = data[var_name][0][0][signal_name]  # MATLAB结构化数组的典型访问方式
                            found = True
                            break
                if not found:
                    print(f"未找到信号: {signal_name}")
                    continue

            # 确保信号数据是1维数组
            if hasattr(signal_data, 'shape'):
                # 如果是numpy数组
                if signal_data.ndim > 1:
                    signal_data = signal_data.flatten()
                elif signal_data.ndim == 0:
                    # 标量值，转换为1维数组
                    signal_data = np.array([signal_data])
            elif isinstance(signal_data, (list, tuple)):
                # 如果是列表或元组
                signal_data = np.array(signal_data).flatten()

            signals[signal_name] = signal_data

        if not signals:
            print("未找到任何目标信号")
            return None

        print(f"找到的信号: {list(signals.keys())}")

        # 创建图像（根据找到的信号数量动态调整）
        num_signals = len(signals)
        fig, axes = plt.subplots(num_signals, 1, figsize=(10, 3 * num_signals))

        if num_signals == 1:
            axes = [axes]  # 确保axes是列表形式

        fig.suptitle(f'MAT文件信号波形 - {file_path.split("/")[-1]}', fontsize=12)

        # 绘制每个信号
        for i, (name, signal) in enumerate(signals.items()):
            axes[i].plot(signal, linewidth=0.8, color='blue')
            axes[i].set_title(f'信号: {name}', fontsize=10)
            axes[i].set_xlabel('采样点')
            axes[i].set_ylabel('幅值')
            axes[i].grid(True, alpha=0.3)

        plt.tight_layout()

        # 转换为QPixmap
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        buf = canvas.buffer_rgba()
        width, height = canvas.get_width_height()

        qimage = QImage(buf, width, height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)

        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return None