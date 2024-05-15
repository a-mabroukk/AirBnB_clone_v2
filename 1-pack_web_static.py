#!/usr/bin/python3
"""fabric script"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function"""
    local("mkdir -p versions")
    timestamp = local("date +%Y%m%d%H%M%S", capture=True)
    archive_name = "web_static_{}.tgz".format(timestamp)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
