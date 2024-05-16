#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""

from fabric.api import *


def deploy():
    """function it is"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
