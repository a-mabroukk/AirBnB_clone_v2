#!/usr/bin/python3
""" Deploy archive"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ["54.209.26.10", "34.207.120.104"]


def do_deploy(archive_path):
    """distributing an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    put("archive_path", "/tmp/")
    # Extract filename from archive path
    filename = os.path.basename(archive_path).split(".")[0]

    # Unpack archive
    with cd("/data/web_static/releases"):
        run(f"tar -xzvf /tmp/{filename}.tgz")

    run(f"rm -rf /tmp/{filename}.tgz")
    run("rm -rf /data/web_static/current")
    run("mv /data/web_static/releases/{}/web_static/* ".format(filename) +
        "/data/web_static/releases/{}/".format(filename))

    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename))
    return True