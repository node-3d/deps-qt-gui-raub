'use strict';

const core = require('deps-qt-core-raub');


module.exports = {
	core: require('deps-qt-core-raub'),
	...require('addon-tools-raub').getPaths(__dirname),
};
