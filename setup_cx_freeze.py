from cx_Freeze import setup, Executable

exe = Executable(
    targetName='cauldron_#0_1.exe',  # версия для термопар
    script="main.py",
    base="Win32GUI",
    )
setup(
    name="Cauldron",
    version="0.1",
    description="",
    executables=[exe]
    )
