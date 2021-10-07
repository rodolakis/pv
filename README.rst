===============
pv Slack-Logger
===============

**pv** provides an EPICS PV logger with slack support. A list of PVs are monitored to be displayed on the console and saved in a text file at preset time interval (Logger). The same PVs are also broadcasted on a slack channel. To reduce traffic on the slack channel PVs are published only on-change using the EPICS PV callback mechanism.

Usage
=====

::

    $ slackpvmonitor.sh
    
or::

    $ pv slack --pv-list "ACIS:ShutterPermit, OPS:message4, OPS:message5" --pv-log-time 60


To start in screen session::

    $ screen -dmS SLACKPV slackpvmonitor.sh
    $ screen -list
    There is a screen on:
            1759231.SLACKPV (Detached)
    1 Socket in /run/screen/S-29iduser.


PVs are logged and on-change published to the authorized slack channel at --pv-log-time interval (default 5 s):

.. image:: docs/source/img/pv_log.png
    :width: 50%
    :align: center

PVs are also sent to a slack channel on-change only:

.. image:: docs/source/img/pv_slack.png
    :width: 50%
    :align: center

::

    $ pv set --pv-list "2bma:TomoScan:Energy, 2bma:TomoScan:EnergyMode"

For help::

    pv set -h
    usage: pv set [-h] [--pv-list PV_LIST] [--pv-log-time PV_LOG_TIME]
                  [--config FILE] [--verbose]

    optional arguments:
      -h, --help            show this help message and exit
      --pv-list PV_LIST     a string containing comma separated PVs to log, e.g.
                            2bma:TomoScan:Energy, 2bma:TomoScan:EnergyMode
                            (default: 0,-1,1)
      --pv-log-time PV_LOG_TIME
                            PVs log time in seconds (default: 5)
      --config FILE         File name of configuration (default:
                            /home/beams/TOMO/slackpv.conf)
      --verbose             Verbose output (default: True)

For all options::

    $ pv -h
    usage: pv [-h] [--config FILE]  ...

    optional arguments:
      -h, --help     show this help message and exit
      --config FILE  File name of configuration

    Commands:
      
        init         Create configuration file
        status       Show the pv-cli status
        set          Set PV to monitor as a comma-separated list
        log          Send the list of PVs to a logger
        slack        Send the list of PVs to slack

Installation
============

Pre-requisites
--------------

Read the installation pre requisited of `2bm slack <https://github.com/decarlof/2bm-slack>`_ to set slack.

Installing from source
======================

In a prepared virtualenv or as root for system-wide installation clone the 
pv Slack-Logger from its github repository

::

    $ git clone https://github.com/xray-imaging/pv pv

To install pv, run::

    $ conda activate slackenv
    $ cd slackpv
    $ ~/.conda/envs/slackenv/bin/python setup.py install

.. warning:: Make sure to edit the channel_id value in the OnChange() callback function to match the name of the slack channel that is autorized for this App. This is located `here <https://github.com/decarlof/pv/blob/e300de699e4daea9746606d29c14706a8b786332/pv/pv.py#L21>`_.




Dependencies
============

Install the following package::

    $ pip install python-dotenv
    $ pip install slack-bolt
    $ pip install pyepics
    $ pip install numpy
