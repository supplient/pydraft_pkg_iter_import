# imports only for type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from importlib.resources import Package
	from types import ModuleType

def ImportAllModules(pkg: Package)-> list[ModuleType]:
	'''Import all modules in `pkg`.

	e.g. For a package like:
		pkg
			__init__.py
			A.py
			sub_pkg
				B.py
	
	Use code as follows:
		import pkg
		mods = ImportAllModules(pkg)

	Then `mods` will be: [<module pkg.A>, <module pkg.sub_pkg.B>]
	'''
	import os.path
	import importlib
	from importlib.abc import Traversable

	mods = []
	# Iteration function
	def Iter(f: Traversable, pkg: importlib.resources.Package = None):
		# If current `f` is a file, check if it's a valid python module
		if f.is_file():
			basename, ext = os.path.splitext(f.name)
			if ext != ".py":
				return
			if basename == "__init__":
				return
			# Import the module by relative path
			mod = importlib.import_module("." + basename, pkg.__name__)
			mods.append(mod)
		# If current `f` is a directory, import it as a package and iterate into it.
		# Note: a directory without `__init__.py` will be treated as a namespace package.
		else:
			# Import the directory as a package.
			# Use relative path if there is a parent package, otherwise use absolute path.
			if pkg:
				sub_pkg = importlib.import_module("." + f.name, pkg.__name__)
			else:
				sub_pkg = importlib.import_module(f.name)
			# Iterate into the directory
			for sub_f in f.iterdir():
				Iter(sub_f, sub_pkg)
	# Enter iteration, use the input package as the root.
	# `resources.files(pkg)` will turn `pkg` into `importlib.resources.Traversable`
	Iter(importlib.resources.files(pkg))
	return mods