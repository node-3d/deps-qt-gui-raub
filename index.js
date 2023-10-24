'use strict';

module.exports = {
	core: require('deps-qt-core-raub'),
	...require('addon-tools-raub').getPaths(__dirname),
};
