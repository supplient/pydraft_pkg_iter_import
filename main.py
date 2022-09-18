import pkg
from pkg_iter_import import ImportAllModules
mods = ImportAllModules(pkg)
print(mods)

# Output should be:
#	IMPORTED pkg
#	IMPORTED A
#	IMPORTED B
#	IMPORTED sub_pkg
#	IMPORTED C
#	[<module 'pkg.A' from 'pkg\\A.py'>, <module 'pkg.B' from 'pkg\\B.py'>, <module 'pkg.sub_pkg.C' from 'pkg\\sub_pkg\\C.py'>]