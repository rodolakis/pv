===============
PV Slack logger
===============

Usage
=====

::

    $ pv slack

.. image:: docs/source/img/pv_log.png
    :width: 50%
    :align: center

.. image:: docs/source/img/pv_slack.png
    :width: 50%
    :align: center

::

    $ pv set --pv-list "2bma:TomoScan:Energy, 2bma:TomoScan:EnergyMode"

For all options::

    $ pv -h
    usage: pv [-h] [--config FILE]  ...

    optional arguments:
      -h, --help     show this help message and exit
      --config FILE  File name of configuration

    Commands:
      
        init         Create configuration file
        status       Show the pv-cli status
        set          Set PV to log as a comma-separated list
        slack        Send the list of PVs to slack


Installation
============

Pre-requisites
--------------

Read the installation pre requisited of `2bm slack <https://github.com/decarlof/2bm-slack>`_ to set slack.

Installing from source
======================

In a prepared virtualenv or as root for system-wide installation clone the 
`slack2pv <https://github.com/decarlof/slackpv>`_ from `GitHub <https://github.com>`_ repository

::

    $ git clone https://github.com/decarlof/slackpv slackpv

To install slackpv, run::

    $ cd slackpv
    $ python setup.py install

.. warning:: Make sure your python installation is in a location set by #!/usr/bin/env python, if not please edit the first line of the bin/dmagic file to match yours.

Dependencies
============

Install the following package::

    $ pip install python-dotenv
    $ pip install slack-bolt
    $ pip install pyepics
