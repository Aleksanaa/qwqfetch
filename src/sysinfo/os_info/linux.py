import distro


info = "%s %s %s" % (distro.name(), distro.version(), distro.codename())
info = info.strip()