#!/usr/bin/python
#
# noquitting.py
# 
# A Zim plugin that attempts to override the "Ctrl-Q" shortcut that I so often hit on accident b/c 'q'
# (on my keyboard) is so close to the other useful shortcuts.
#

import gtk

from zim.plugins import PluginClass, WindowExtension, extends
from zim.actions import action

class NoQuittingPlugin(PluginClass):

	plugin_info = {
		'name': _('No Quitting'), # T: plugin name
		'description': _('''\
Tries to remove the 'quit' keyboard shortcut, to prevent accidental quitting.
'''), # T: plugin description
		'author': 'Robert Hailey',
		'help': 'Plugins:NoQuitting',
	}

@extends('MainWindow')
class MainWindowExtension(WindowExtension):

	# NB: until there is demand for it, "Alt-F4" still quits... hasn't bothered me yet.
	uimanager_xml = '''
		<ui>
			<menubar name='menubar'>
				<menu action='file_menu'>
					<placeholder name='page_modification_actions'>
						<menuitem action='dontclose'/>
						<menuitem action='dontquit'/>
					</placeholder>
				</menu>
			</menubar>
		</ui>
	'''

	def __init__(self, plugin, window):
		WindowExtension.__init__(self, plugin, window)

	@action(
		_('Dont Quit'),
		stock=gtk.STOCK_JUMP_TO,
		readonly=True,
		accelerator = '<Control>Q'
	) # T: menu item
	def dontquit(self):
		print "Not quitting"


	@action(
		_('Dont Close Window'),
		stock=gtk.STOCK_JUMP_TO,
		readonly=True,
		accelerator = '<Control>W'
	) # T: menu item
	def dontclose(self):
		print "Not closing window"


