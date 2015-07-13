from distutils.core import setup
import py2exe

setup(
    windows = [{
            "script":"Draft Analyzer.py",
            "icon_resources": [(1, "Icons/D-Icon.ico")],
            }],
    name='Hex Programming',
    version='2.0',
    packages=[''],
    url='',
    license='',
    author='Ioannis',
    author_email='219af24a@opayq.com',
    description='Removed most prints. Including trimmed values and export collection'
)
