#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
cron = """
-> nano /etc/crontab -e || {crontab -e} [CRON]

__________________________________________   Minute (0-59)
|   ______________________________________   Hour (0-23)
|   |   __________________________________   Day Of Month (0-31)
|   |   |   ______________________________   Month (1-12) || (jan, feb, mar...)
|   |   |   |   __________________________   Weekday (0-6) || (sun, mon, tue...)
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   | {username}   {command to exec.}
v   v   v   v   v

*   *   *   *   *   [user]         [command]

-> crontab -l   {lists cron jobs for user}
"""

chmod = """
Permissions  |  Owner | Group | Others
--------------------------------------
read         |   4    |   4   |   4
write        |   2    |   2   |   2
execute      |   1    |   1   |   1

  -             r--      r--     r--
 --             -w-      -w-     -w-
---             --x      --x     --x

ex:	-r--r--r--		{Read : All Users}
        --w--w--w-      {Write : All Users}
        ---x--x--x      {Execute : All Users}

       (- or d) (---) (---) (---)
                owner group others

chmod ug=rw [file] {sets read + write for owner & group}
chmod u=rw,g=r,o= [file] {sets read + write for owner,
                          read for group,
                          denies access to others}
"""

mysql = """

* Login                       -> [mysql_directory]/bin/mysql -h [hostname] -u root -p [database];

* Create Database             -> mysql> create database [db-name];

* List All DBs                -> mysql> show databases;

* Switch To DB                -> mysql> use [db-name];

* Show all tables in DB       -> mysql> show tables;

* View DB's field formats     -> mysql> describe [table];

* Delete DB                   -> mysql> drop database [db-name];

* Delete Table                -> mysql> drop table [table];

* Show all data in table      -> mysql> select * from [table];

* Return column and column
  info pertaining to table    -> mysql> show columns from [table];

* Show selected rows with
  value "n"                   -> mysql> select * from [table] where [field_name]='n';

* Delete column               -> mysql> alter table [table] drop column [column_name];

* Add new column              -> mysql> alter table [table] add column [column_name] varchar(20);

* Alter column size           -> mysql> alter table [table] modify [column_name] varchar([size]);

* Insert new row              -> mysql> insert into [table] values ("values", "for", "row");

* Delete items from table     -> mysql> delete from [table] where [condition];

* Export database             -> mysqldump -u [username] -p [db_name] > [dump_file.sql]

* Import database             -> mysql -u [username] -p [db_name] < [filename.sql]

"""

basic_conf = """
* gnome-control-center                          [Graphical Configuration]

* nmcli
* nmtui                                         [Network Configuration]
* nm-connection-editor

* localectl                                     [Language/Keyboard Configuration]

* timedatectl
* date                                          [Date/Time Configuration]

* /etc/chrony.conf
* ntpdate                                       [Date/Time Sync.]
"""

jbsrv = """

             [List All Services]
              -----------------

* systemctl -at service
* ls /etc/systemd/system/*.service
* ls /usr/lib/systemd/system/*.service

             [List Running Services]
              ---------------------

* systemctl -t service --state=active

             [Check If Service Is Enabled]
              ---------------------------

* systemctl is-enabled [service]

             [Create New Service Or Modify Configuration]
              ------------------------------------------

* systemctl daemon-reload
* /etc/systemd/system/*.service

             [View Runlevel/Target]
              --------------------
* who -r

             [Change Runlevel/Target]
              ----------------------

* systemctl isolate [name.target]

             [Configure Logging]
              -----------------

* /etc/rsyslog.conf
* /etc/rsyslog.d/*.conf
* /var/log/journal
* systemd-journal.service

             [View Logs]
              ---------

* /var/log
* journalctl
"""

kbh = """
             [Power Off/Halt/Reboot]
              ---------------------

* poweroff
* systemctl poweroff
* shutdown

             [Configure Grub Bootloader]
              -------------------------

* /etc/default/grub
* grub2-mkconfig
* grub-set-default

             [View Configured Hardware]
              ------------------------

* lshw

             [Configure Kernel Module]
              -----------------------

* modprobe   {-r to remove}

             [Configure Hardware Device]
              -------------------------

* udev

             [View Kernel Parameters]
              ----------------------

* sysctl -a
* cat /proc/cmdline

             [View Kernel Version]
              -------------------

* rpm -q kernel
* uname -r
"""

sftwr_mgmt = """
             [Install Software]
              ----------------

* yum install
* yum group install
* apt install
* apt-get install

             [View Software Info]
              ------------------

* yum info
* yum group info

             [Update Software]
              ---------------

* yum update
* apt update
* apt-get update

             [Upgrade Software]
              ----------------

* yum upgrade
* apt upgrade
* apt-get upgrade

             [Configure Software Repos]
              ------------------------

* /etc/yum.repos.d/*.repo

             [Find Package Owning File]
              ------------------------

* yum provides [filename-glob]

             [View Software Version]
              ---------------------

* rpm -q [package-name]

             [View Installed Software]
              -----------------------

* yum list installed
* apt list

             [Configuration]
              -------------

* dpkg-reconfigure    {ex: console-setup}
"""
user_mgmt = """

             [Graphical User Management]
              -------------------------

* system-config-users

             [Create User Account]
              -------------------

* useradd

             [Delete User Account]
              -------------------

* userdel

             [View Or Change User]
              -------------------

* usermod
* /etc/passwd

             [Account Details]
              ---------------

* vipw
* id

             [Create User Group]
              -----------------

* groupadd

             [Delete User Group]
              -----------------

* groupdel

             [Change Group Details]
              --------------------

* groupmod
* /etc/group

             [Change User Password]
              --------------------

* passwd

             [Change User Permissions]
              -----------------------

* visudo

             [Change Password Policy]
              ----------------------

* chage

             [View User Sessions]
              ------------------

* w
"""
FSVolsDsks = """
             [Default File System]
              -------------------

* xfs

             [Create/Modify Disk]
              ------------------

* fdisk
* gdisk

             [Partitions]
              ----------

* parted
* gparted
* ssm create

             [Defragment Disk Space]
              ---------------------

* fsck
* xfs_fsr

             [Mount Storage]
              -------------

* mount
* /etc/fstab
* ssm mount

             [Mount And Activate Swap]
              -----------------------

* swapon -a

             [View Free Disk Space]
              --------------------

* df
* free

             [View Logical Volume Info]
              ------------------------

* lvdisplay
* lvs
* vgdisplay
* vgs
* pvdisplay
* pvs

             [Create Physical Volume]
              ----------------------

* pwcreate

             [Create Logical Volume]
              ---------------------

* lvcreate

             [Create Volume Group]
              -------------------

* vgcreate

             [Enlarge Vols. Formatted w/ Default File System]
              ------------------------------------------------

* vgextend
* lvextend
* resizefs

             [Shrink Vols. Formatted w/ Default File System]
              ---------------------------------------------

* vgextend

             [Check/Repair File System]
              ------------------------

* fsck

             [View NFS Share]
              --------------

* showmount -e
* mount

             [Configure NFS Share]
              -------------------

* /etc/exports
* systemctl reload nfs.service

             [Configure On-demand Auto Mount]
              ------------------------------

* /etc/auto.*
* /etc/auto.master.d/*.autofs

             [Change File Permissions]
              -----------------------

* chmod
* chown
* chgrp
* umask

             [Change File Attributes]
              ----------------------

* chattr

             [Change Access Control List]
              --------------------------

* setfacl

"""
lds = """

  / --- bin    default   rc.d   sound   sysconfig   x11
     |            |        |      |         |        |
     -- boot      |        |      |         |        |
     |            |        |      |         |        |
     -- dev       |        |      |         |        |
     |            |        |      |         |        |
     -- etc ------------------------------------------
     |
     -- home ----------------------
     |              |             |
     -- lib     username_1    username_2
     |
     -- lost+found
     |                                 -- X11R6
     -- misc       cdrom   floppy      |
     |               |       |         -- bin
     -- mnt ------------------         |
     |                                 -- games
     -- net     -----------------------|
     |          |                      -- include
     -- opt     |    -- gdm            |
     |          |    |                 -- lib
     -- proc    |    -- lib            |
     |          |    |                 -- local
     -- root    |    -- lock           |
     |          |    |                 -- man
     -- sbin    |    -- run            |
     |          |    |                 -- sbin
     -- tmp     |    -- log            |
     |          |    |                 -- share -- doc
     -- usr -----    -- spool          |
     |               |                 -- src
     -- var ----------- tmp
"""

networking = """
             [Configure Name Resolution]
              -------------------------

* /etc/hosts
* /etc/resolv.conf
* nmcli con mod

             [Configure Hostname]
              ------------------

* hostnamectl
* /etc/hostname
* nmtui

             [View Network Interface Info]
              ---------------------------

* ip addr
* nmcli dev show
* teamdctl
* brctl
* bridge

             [Configure Network Interface]
              ---------------------------

* /etc/sysconfig/network-scripts/ifcfg-*
* nmcli con [add | mod | edit]
* nmtui
* nm-connection-editor

             [View Routes]
              -----------

* ip route

             [Configure Routes]
              ----------------

* ip route add
* nmcli
* nmtui
* nm-connection-editor
* /etc/sysconfig/route-iface

             [Configure Firewall]
              ------------------

* firewall-cmd
* firewall-config

             [View Ports/Sockets]
              ------------------

* ss
* lsof
"""
secid = """
             [Security Directory]
              ------------------

* /etc/selinux/

             [Configure System Security]
              -------------------------

* chcon
* restorecon
* semanage
* setsebool
* system-config-selinux

             [Report On System Security]
              -------------------------

* sealert

             [LDAP, SSSD, Kerberos]
              --------------------

* authconfig-tui
* authconfig-gtk

             [Network Users]
              -------------

* getent
"""
recman = """
             [Trace System Calls]
              ------------------

* strace

             [Trace Library Calls]
              -------------------

* ltrace

             [Change Process Priority]
              -----------------------

* nice
* renice

             [Change Process Run Location]
              ---------------------------

* taskset

             [Kill A Process]
              --------------

* kill
* pkill
* killall

             [View System Usage]
              -----------------

* top
* ps
* sar
* iostat
* ss
* vmstat
* mpstat
* numastat
* tuna

             [View Disk Uasge]
              ---------------

* df
* iostat
"""
apache2 = """
             [Start]
              -----

* /etc/init.d/apache2 start
* service apache2 start
* apachectl -k start

             [Stop]
              ----

* /etc/init.d/apache2 stop
* service apache2 stop
* apachectl -k stop

             [Restart]
              -------

* /etc/init.d/apache2 restart
* service apache2 restart
* apachectl restart

             [Reload]
              ------

* /etc/init.d/apache2 reload
* service apache2 reload
* apachectl -k reload

             [Status]
              ------

* /etc/init.d/apache2 status
* service apache2 status

             [Graceful]
              --------

* apachectl -k graceful
* apachectl -k graceful-stop

             [Enable/Disable Virtual Hosts]
              ----------------------------

* a2ensite xxxx.conf
* a2dissite xxxx.conf

             [Syntax Check]
              ------------

* apachectl configtest
* apachectl -t

             [Website Directory Structure]
              ---------------------------

* /var/www/html             -             Default
* /var/www                  -             Other Domains

             [Configuration Files]
              -------------------

* /etc/apache2/apache2.conf
* /etc/apache2/ports.conf

             [Log Files]
              ---------
[tail -f {log_path}]

* /var/log/apache2/error.log
* /var/log/apache2/access.log

             [Loaded Modules]
              --------------

* apachectl -M
* apache2ctl -M

             [Available Modules]
              -----------------

* /usr/lib/apache2/modules
"""
#####
# SECENG
#####

lies = """
             [Baseline]
              --------

* Before attempting to spot a dishonest person
  or trying to catch a person in a lie, you should
  first have a 'normal baseline'. To obtain this
  baseline, attempt to make small talk with the
  target, asking them seemingly harmless questions
  about themselves or simpy make small talk to get
  a feel for how they usually react to basic, simple
  questions. It is best to use questions that require
  an affirmative or negative response such as things
  the target may or may not like. This will give you
  an idea of how the target responds when they are
  being honest. Don't ask questions that the target
  may feel the need to lie about. This will cause
  your baseline reading to be faulty making it harder
  to tell a lie from the truth when the real questions
  are asked later. Take note of the targets 'tics' or
  behavior during this line of questioning but remember,
  you are trying to get a baseline reading so don't say
  or do anything that may make the target uncomfortable.
  You should also take note of how often and for how long
  the target blinks. An average person will blink roughly
  every 10 to 12 seconds. When stressed or when the target
  knows he is lying, he may blink 5 or 6 times in quick
  succession. However it is important to note that some
  medical disorders may change a persons blink rate. A
  person with Parkinson's may blink more slowly while a
  person with schizophrenia may blink more rapidly.

             [After Establishing Baseline]
              ---------------------------

* After you have established a baseline, begin asking more
  pointed or suggestive questions, taking note of how the
  responds as well as the body language of the target, tone
  of voice, persperation, and blinking intervals.
"""

g_opers = """
Web Search:
-----------

    allinanchor:, allintext:, allintitle:, allinurl:,
    cache:, define:, filetype:, id:, inanchor:, info:,
    intext:, intitle:, inurl:, link:, related:, site:

Image Search:
-------------

    allintitle:, allinurl:, filetype:, inurl:, intitle:
    site:

Groups:
-------

    allintext:, allintitle:, author:, group:, insubject:,
    intext:, intitle:

Directory:
----------

    allintext:, allintitle:, allinurl:, ext:, filetype:,
    intext:, intitle:, inurl:

News:
-----

    allintext:, allintitle:, allinurl:, intext:, intitle:,
    inurl:, location:, source:

Product Search:
---------------

    allintext:, allintitle:

"""
