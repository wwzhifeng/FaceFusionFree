from typing import Optional

METADATA =\
{
	'name': 'FaceFusionFree',
	'description': 'Industry leading face manipulation platform',
	'version': 'VIP3.5',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://space.bilibili.com/1772750129/lists/3258125?type=season'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
