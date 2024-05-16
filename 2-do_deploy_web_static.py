#!/usr/bin/python3
""" Deploy archive"""
from fabric.api import put, run, env, sudo
from os.path import exists

env.hosts = ["54.209.26.10", "34.207.120.104"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """distributing an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    if archive_path:
        filename = archive_path.split("/")[-1]
        extract = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, extract))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, path, extract))
        run("rm /tmp/{}".format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, extract))
        run("rm -rf {}{}/web_static".format(path, extract))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, extact))
        return True
    else:
        return False
