print("IMPORTED pkg")

# def print_items():
	# for item in items:
		# print(item)

# import importlib
# import sys
# pkg = sys.modules[__package__]

# from importlib import resources
# from importlib.abc import Traversable
# import os.path
# mods = []
# def Iter(f: Traversable, pkg: resources.Package = None):
	# if f.is_file():
		# basename, ext = os.path.splitext(f.name)
		# if ext != ".py":
			# return
		# if basename == "__init__":
			# return
		# mod = importlib.import_module("." + basename, pkg.__name__)
		# mods.append(mod)
	# else:
		# if pkg:
			# sub_pkg = importlib.import_module("." + f.name, pkg.__name__)
		# else:
			# sub_pkg = importlib.import_module(f.name)
		
		# for sub_f in f.iterdir():
			# Iter(sub_f, sub_pkg)
# Iter(resources.files(pkg))
# print(mods)