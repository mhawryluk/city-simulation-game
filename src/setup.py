import cx_Freeze
import os


executables = [cx_Freeze.Executable(os.path.join('src', 'main.py'))]
cx_Freeze.setup(
    name='CitySimulationGame',
    options={
        'build_exe': {
            'packages': ['pygame', 'pygame_menu', 'numpy', 'pyperclip'],
            'include_files': ['Assets/', 'Maps/', 'SaveFiles/']
        }
    },
    executables = executables
)