from ... import globals

sys_type = globals.get(["platform"])[0]["type"]

if sys_type == "posix":
    from .posix import shell_name, shell_ver
else:
    shell_name,shell_ver = "",""
    

shell = "%s %s" % (shell_name, shell_ver)
shell = shell.strip()
