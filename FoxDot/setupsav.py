#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as f:
    long_description=f.read()

with open("FoxDot/lib/.version", "r") as f:
    version = f.read()

setup(name='FoxDot',
      version=version,
      description='Live coding music with SuperCollider',
      author='Ryan Kirkbride',
      author_email='ryan@foxdot.org',
      url='http://foxdot.org/',
      packages=['FoxDot',
                'FoxDot.lib',
                'FoxDot.lib.Code',
                'FoxDot.lib.Custom',
                'FoxDot.lib.Extensions',
                'FoxDot.lib.Extensions.VRender',
                'FoxDot.lib.Extensions.SonicPi',
                'FoxDot.lib.Workspace',
                'FoxDot.lib.EspGrid',
                'FoxDot.lib.Effects',
                'FoxDot.lib.Patterns',
                'FoxDot.lib.SCLang',
                'FoxDot.lib.Settings',
                'FoxDot.lib.Utils',
                'FoxDot.lib.Crashserver',
                'FoxDot.lib.Crashserver.speech',
                ],
      long_description=long_description,
      long_description_content_type="text/markdown",
      entry_points={'gui_scripts' : ['FoxDot = FoxDot.__init__:main']},
      package_data = {'FoxDot': ['snd/*/*/*.*',
                                 'lib/Crashserver/crash_snd/*/*/*.*',
                                 'lib/Crashserver/crash_snd/_loop_/*/*.*',
                                 'lib/Crashserver/crash_snd/_loop_/*.*',
                                 'lib/Crashserver/speech/*.*',
                                 'snd/_loop_/foxdot.wav',
                                 'osc/*.scd',
                                 'osc/sceffects/*.scd',
                                 'osc/scsyndef/*.scd',
                                 'demo/*.py',
                                 'rec/.null',
                                 'lib/Extensions/*/*.*',
                                 'lib/Extensions/*/*/*.*',
                                 'lib/.version',
                                 'README.md',
                                 ],
                      'FoxDot.lib.Workspace': ['img/*', 'tmp/*'],
                      'FoxDot.lib.Settings' : ['conf.txt']})
