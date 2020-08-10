# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/g1k/zephyr-panel/src/main/python/main.py'],
             pathex=['/home/g1k/zephyr-panel/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/g1k/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/g1k/zephyr-panel/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          name='zephyr-panel',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='zephyr-panel')
