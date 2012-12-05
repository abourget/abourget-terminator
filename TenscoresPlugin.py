import gtk
import urllib
import terminatorlib.plugin as plugin
import re

# Written by Alexandre Bourget @bourgetalexndre
# Copyright 2012 Alexandre Bourget
# See copyright file that comes with this file for full licence
#
# Kick-start my Terminator sessions faster!
#

AVAILABLE = ['TenscoresPlugin']

class TenscoresPlugin(plugin.MenuItem):
    capabilities = ['terminal_menu']

    def __init__(self):
        self.terminal = None

    def callback(self, menuitems, menu, terminal):
        item = gtk.MenuItem('Tenscores Plugin')
        item.connect("activate", self.run_it)
        menuitems.append(item)
        self.terminal = terminal

    my_tabs = {
        "PSERVE": "cdp; act; pserve --reload local.ini",
        "COMPILE": "cdp; act; ts-compile-less local.ini",
        }

    def run_it(self, menuitem):
        window = self.terminal.get_toplevel()

        for x in range(len(self.my_tabs)):
            window.tab_new()

        notebook = window.get_child()
        terminals = notebook.terminator.terminals

        for i, (label, cmd) in enumerate(self.my_tabs.iteritems(), 1):
            term = terminals[-i]
            notebook.get_tab_label(term).set_custom_label(label)
            term.vte.feed_child(cmd + '\n')
