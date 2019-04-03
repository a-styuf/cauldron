from cx_Freeze import setup, Executable
import matplotlib.backends.backend_tkagg

exe = Executable(
    targetName='cauldron_#0_1.exe',  # версия для термопар
    script="main.py",
    base="Win32GUI",
    )
setup(
    name="Cauldron",
    version="0.1",
    description="",
    options={'build_exe': {'includes': ['atexit', 'numpy.core._methods', 'numpy.lib.format']}},
    executables=[exe]
    )

