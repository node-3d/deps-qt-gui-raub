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
				'action_name' : 'Rpath CORE added.',
				'inputs'      : [],
				'outputs'     : ['<(qt_gui_bin)/qml'],
				'action'      : [
					'install_name_tool -add_rpath "<(qt_core_bin)" "<(qt_gui_bin)/plugins/platforms/libqcocoa.dylib" || echo',
					'Already added.',
				],
			}
			],
		},
		{
			'target_name'  : 'fix_osx2',
			'type'         : 'none',
			'dependencies' : ['fix_osx1'],
			'actions'      : [{
				'action_name' : 'Rpath GUI added.',
				'inputs'      : [],
				'outputs'     : ['<(qt_gui_bin)/plugins'],
				'action'      : [
					'install_name_tool -add_rpath "<(qt_gui_bin)" "<(qt_gui_bin)/plugins/platforms/libqcocoa.dylib" || echo',
					'Already added.',
				],
			}
			],
		},
	]}]],
}
