#!/usr/bin/env python3

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [],
                 'excludes': [],
                 "include_files": ["fa_mainwindow.ui",
                                   "stock.ui",
                                   "icon.png"]}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('fa.py', base=base)
]

setup(name='Fa',
      version = '1.0',
      description = 'Test',
      options = {'build_exe': build_options},
      executables = executables)
