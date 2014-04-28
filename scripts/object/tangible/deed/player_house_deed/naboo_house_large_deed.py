import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'deeds/structureDeed')
	object.setConstructorTemplate('object/building/player/construction/shared_construction_player_house_naboo_large_style_01.iff')
	object.setStructureTemplate('object/tangible/deed/player_house_deed/shared_naboo_house_large_deed.iff')
	object.setLotRequirement(2)
	object.setBMR(8)
	return

	
	
	
