# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "My Theme",
			"color": "orange",
			"icon": "fa fa-computer",
			"type": "module",
			"label": _("My Theme")
		}
	]
