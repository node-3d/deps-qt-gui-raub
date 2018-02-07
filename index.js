'use strict';

const path = require('path');

const tools = require('addon-tools-raub');

const core = require('deps-qt-core-raub');


module.exports = {
	core,
	...tools.paths(__dirname),
};
