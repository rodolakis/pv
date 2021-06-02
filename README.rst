==============
2-BM Slack bot
==============

Usage
=====

::

    $ slackpv
      Bolt app is running!


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
