{
	'variables': {
		'rm'          : '<!(node -e "require(\'addon-tools-raub\').rm()")',
		'rem'         : '<!(node -e "require(\'.\').rem()")',
		'qt_core_bin' : '<!(node -e "require(\'.\').core.bin()")',
		'qt_gui_bin'  : '<!(node -e "require(\'.\').bin()")',
		'XALL%' : 'false',
	},
	'targets': [
		{
			'target_name' : 'remove_extras',
			'type'        : 'none',
			'conditions'  : [['XALL=="false"', {'actions': [
				{
					'action_name' : 'Unnecessary binaries removed.',
					'inputs'      : [],
					'outputs'     : ['build'],
					'action'      : ['<(rm)', '-rf', '<@(rem)'],
				}
			]}]],
		},
		
	],
	'conditions': [['OS=="mac"', { 'targets': [
		{
			'target_name'  : 'fix_osx1',
			'type'         : 'none',
			'dependencies' : ['remove_extras'],
			'actions'      : [{
				'action_name' : 'Execution permitted.',
				'inputs'      : [],
				'outputs'     : ['<(qt_gui_bin)/qml'],
				'action'      : [
					'chmod +x', '<(qt_gui_bin)/fix-rpath.sh',
				],
			}],
		},
		{
			'target_name'  : 'fix_osx2',
			'type'         : 'none',
			'dependencies' : ['fix_osx1'],
			'actions'      : [{
				'action_name' : 'Rpaths added.',
				'inputs'      : [],
				'outputs'     : ['<(qt_gui_bin)/plugins'],
				'action'      : [
					'<(qt_gui_bin)/fix-rpath.sh', '<(qt_core_bin)', '<(qt_gui_bin)',
				],
			}],
		},
	]}]],
}
