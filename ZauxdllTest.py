import pyvisa

class GBIOConnect:
    # 全局变量，存储成功连接的 GPIB 设备
    connected_gpib_devices = []

    def __init__(self):
        """
        初始化方法：扫描所有已连接的 GPIB 设备，并存储到全局变量中。
        """
        # 弹出提示：扫描中
        # QMessageBox.information(None, "扫描状态", "正在扫描 GPIB 设备...")

        # 创建资源管理器
        self.rm = pyvisa.ResourceManager()
        self.rm.visa_timeout = 3000  # 全局默认3秒超时（单位：毫秒）
        # 列出所有连接的设备
        all_resources = self.rm.list_resources()

        # 清空全局变量
        GBIOConnect.connected_gpib_devices.clear()

        # 过滤出 GPIB 设备并检查是否成功连接
        for resource in all_resources:
            if resource.startswith("GPIB"):  # 检查是否是 GPIB 设备
                try:
                    # 尝试打开设备
                    instrument = self.rm.open_resource(resource)
                    print(f"Successfully connected to GPIB device: {resource}")
                    GBIOConnect.connected_gpib_devices.append(resource)
                    instrument.close()  # 关闭连接
                except pyvisa.errors.VisaIOError:
                    # 如果无法打开设备，则跳过
                    print(f"Failed to connect to GPIB device: {resource}")

        # 弹出提示：扫描结束
        # QMessageBox.information(None, "扫描状态", "GPIB 设备扫描完成！")

        # 打印成功连接的 GPIB 设备
        print("Connected GPIB devices:", GBIOConnect.connected_gpib_devices)