import os, subprocess


def check_cli_installed():
    """检查HandBrakeCLI是否安装"""

    # 检查PATH
    try:
        subprocess.run(['HandBrakeCLI', '--version'],
                       capture_output=True, timeout=3)
        print("✅ HandBrakeCLI 已在PATH中")
        return True
    except:
        pass

    # 检查常见路径
    paths = [
        r"I:\Tools\HandBrakeCLI\HandBrakeCLI.exe",
        r"C:\Program Files\HandBrake\HandBrakeCLI.exe",
        r"C:\Program Files (x86)\HandBrake\HandBrakeCLI.exe"
    ]

    for path in paths:
        if os.path.exists(path):
            print(f"✅ HandBrakeCLI 存在: {path}")
            # 测试能否运行
            try:
                result = subprocess.run([path, '--version'],
                                        capture_output=True, timeout=3)
                print(f"   版本: {result.stdout.decode().split()[1]}")
                return True
            except:
                print(f"   但无法运行")

    print("❌ HandBrakeCLI 未安装")
    print("请下载: https://github.com/HandBrake/HandBrake/releases")
    print("查找: HandBrakeCLI-*.zip")
    return False


# 运行检查
check_cli_installed()