# SystemD User Skeleton

Reference skeleton for user level systemd service. In this repo you can find detail on how to start a simple service as a user with benefit of SystemD machinery.

* https://systemd.io/ ~ Home page of SystemD
* https://www.freedesktop.org/wiki/Software/systemd/ ~ Wikipedia info about SystemD
* https://github.com/systemd/systemd ~ The source code
* https://www.spi-inc.org/projects/systemd/ ~ Software of public intrest
* http://0pointer.de/blog/projects/systemd.html ~ Lennart Poettering (original author)
* https://wiki.archlinux.org/title/systemd/User ~ Arch Linux User level help

At first you have to enable the paerticular user to use the good parts of SystemD

```bash
sudo loginctl enable-linger $USER
```

Then you can start by creating `~/.config/systemd/user` folder and start filling it with your services, scheduled jobs, etc.

When a new `*.service` is added or modified in there then you have to invoke `systemctl --user daemon-reload` to refresh the unit in __systemd__ memory.

Then you can use other goodies:

* `systemctl --user` - to see short tree of your units
* `systemctl --user --state failed` - to se what failed
* `systemctl --user status` - to see longer list of units
* `systemctl -user --type=service --state=active` - shorter list of units
* `systemctl --user enable` - enable to start the service next time you (re)start your box

and other `systemctl` and `journalctl` commands, do not forget to always add `--user` flag.
