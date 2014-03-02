import sys

def setup(core, object):
	object.setIntAttribute('no_trade', 1)
	object.setStfFilename('static_item_n')
	object.setStfName('item_force_sensitive_pendant_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_force_sensitive_pendant_01_02')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 12)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:strength_modified', 12)
	object.setStringAttribute('class_required', 'Jedi')
	return
