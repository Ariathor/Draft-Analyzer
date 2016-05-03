# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'Sounds', 'Sounds' ),
         ( 'Icons', 'Icons' ),
         ( 'Card Info/card_info.json', 'Card Info'),
		 ( 'Resources/api.ini', 'API INI')]

a = Analysis(['Draft Analyzer.py'],
             pathex=['C:\\Users\\Ioannis\\Dropbox\\Programming\\Hex Programming'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Draft Analyzer',
          debug=False,
          strip=False,
          upx=True,
          console=False,
		  icon='Resources/D-Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Draft Analyzer')

