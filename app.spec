# -*- mode: python ; coding: utf-8 -*-
# WARNING: This spec bundles the repo-level .env into the executable.
# For production builds, replace .env with a dedicated file that contains
# only production values — never commit real secrets to the repo-level .env.
# Recommended: create a separate .env.prod, copy it to .env before running
# PyInstaller, then delete it from the repo root afterwards.

import os

_datas = [('src/assets', 'src/assets')]
if os.path.exists('.env'):
    _datas.append(('.env', '.'))

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=_datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
