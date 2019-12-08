#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Beremiz, a Integrated Development Environment for
# programming IEC 61131-3 automates supporting plcopen standard and CanFestival.
#
# Copyright (C) 2016: Andrey Skvortsov
#
# See COPYING file for copyrights details.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


from __future__ import absolute_import
from __future__ import unicode_literals

import subprocess
import os

import util.paths as paths


def GetCommunityHelpMsg():
    return _(
        "The best place to ask questions about Beremiz software\n"
        "is project's mailing list: beremiz-devel@lists.sourceforge.net\n"
        "\n"
        "This is the main community support channel.\n"
        "For posting it is required to be subscribed to the mailing list.\n"
        "\n"
        "You can subscribe to the list here:\n"
        "https://lists.sourceforge.net/lists/listinfo/beremiz-devel"
    )


def GetAppRevision():
    return "underway"


def GetAboutDialogInfo():
    import wx
    info = wx.AboutDialogInfo()

    info.Name = "PLCOpenEditorLight"
    info.Version = app_version

    info.Copyright = ""
    info.Copyright += "(C) 2016-2017 Andrey Skvortsov\n"
    info.Copyright += "(C) 2008-2015 Eduard Tisserant\n"
    info.Copyright += "(C) 2008-2015 Laurent Bessard"

    info.WebSite = ("http://beremiz.org", "beremiz.org")

    info.Description = _("Open Source framework for automation, "
                         "implemented IEC 61131 IDE with constantly growing set of extensions "
                         "and flexible PLC runtime.")

    info.Developers = (
        "Andrey Skvortsov <andrej.skvortzov@gmail.com>",
        "Sergey Surkov <surkov.sv@summatechnology.ru>",
        "Edouard Tisserant <edouard.tisserant@gmail.com>",
        "Laurent Bessard <laurent.bessard@gmail.com>")

    info.License = (
        '\n This program is free software; you can redistribute it and/or\n'
        ' modify it under the terms of the GNU General Public License\n'
        ' as published by the Free Software Foundation; either version 2\n'
        ' of the License, or (at your option) any later version.\n'
        '\n'
        ' This program is distributed in the hope that it will be useful,\n'
        ' but WITHOUT ANY WARRANTY; without even the implied warranty of\n'
        ' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n'
        ' GNU General Public License below for more details.\n'
        '\n'
    )

    # read license file
    path = paths.AbsDir(__file__)
    license_path = os.path.join(path, "COPYING")
    if os.path.exists(license_path):
        with open(license_path) as f:
            info.License += f.read()

    info.Icon = wx.Icon(os.path.join(path, "images", "about_brz_logo.png"), wx.BITMAP_TYPE_PNG)

    info.Translators = (
        "This version does not support multilingual",
        "notation, currently available English only.",
        "",
    )
    
    info.Artists = (
        "Extracting editor code, interface rearrange", 
        "with some fixings relative to simplification", 
        "was been done by Simplest System Solutions",
        "http://sites.google.com/view/simplest/ ",
        "",
    )
    return info


app_version = "0.0"
rev = GetAppRevision()
if rev is not None:
    app_version = app_version + "-" + rev.rstrip()
