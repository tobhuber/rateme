# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mainwindow.py'],
             pathex=['C:\\Users\\tobi (nvidia)\\Documents\\Projects\\rateme'],
             binaries=[],
             datas=[('db.json', '.'), ('recources/ratemeicon.ico', './recources'), ('recources/watermelonsuger.jpg', './recources'), ('recources/default.png', 'recources/'), ('recources/MadeInTheAM.jpg', 'recources/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='RateMe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='recources/ratemeicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mainwindow')
