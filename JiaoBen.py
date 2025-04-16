import sys

def main():
    # 检查是否传入了参数
    if len(sys.argv) > 1:
        print(f"成功接收到参数: '{sys.argv[1]}'")
        print(f"参数类型: {type(sys.argv[1])}")
        return 0
    else:
        print("未接收到任何参数", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())