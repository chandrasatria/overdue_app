# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in overdue_app/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('overdue_app/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='overdue_app',
	version=version,
	description='app untuk membatasi jumlah invoice ketika ada overdue dari customer yang sama. contoh diset 1, maka customer tidak bisa lanjut submit untuk berikut - berikutnya ketika masih overdue.',
	author='das',
	author_email='das@das.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
