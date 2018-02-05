# FreeImage binaries

* Platforms: win x32/x64, linux x32/x64, mac x64.
* Library: FreeImage.
* Linking: static dll-type.


## Install

`npm i -s deps-qt-core-raub`


## Legal notice

This software uses the [Qt library](https://www.qt.io/).
Qt is legally used under the LGPLv3 (GNU Lesser General Public License) version.
It is [explicitly stated](https://doc.qt.io/qt-5.10/licensing.html) that Qt can be used commercially under LGPLv3:

> Qt licensed under the GNU Lesser General Public License (LGPL) version 3 is
appropriate for the development of Qt applications provided you can comply
with the terms and conditions of the GNU LGPL version 3 (or GNU GPL version 3).

These **terms and conditions** allow using (unmodified) Qt as a shared library (DLL), in a closed-source project.
To which this project fully complies.

Qt licensing information (a COPY) is given in a [separate file](/QT_LGPL),
which also can be found on
[Qt's official web-site](http://doc.qt.io/qt-5/lgpl.html).

The binaries were ripped from installed copy of the framework.

---

The rest of this package is MIT licensed.

---


## Usage

### binding.gyp

```javascript
	'variables': {
		'qt_core_include' : '<!(node -e "require(\'deps-qt-core-raub\').include()")',
		'qt_core_bin'     : '<!(node -e "require(\'deps-qt-core-raub\').bin()")',
	},
	...
	'targets': [
		{
			'target_name': '...',
			
			'include_dirs': [
				'<(freeimage_include)',
				...
			],
			
			'library_dirs': [ '<(freeimage_bin)' ],
			
			'conditions': [
				
				['OS=="linux"', {
					'libraries': [
						'-Wl,-rpath,<(freeimage_bin)',
						'<(freeimage_bin)/freeimage.so',
						...
					],
				}],
				
				['OS=="mac"', {
					'libraries': [
						'-Wl,-rpath,<(freeimage_bin)',
						'<(freeimage_bin)/freeimage.dylib',
						...
					],
				}],
				
				['OS=="win"', {
					'libraries': [ 'FreeImage.lib', ... ],
				}],
				
			],
		},
```


### addon.cpp

```cpp
#include <FreeImage.h>
```
