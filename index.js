'use strict';

const path = require('path');

const tools = require('addon-tools-raub');

const core = require('deps-qt-core-raub');


module.exports = {
	...tools.paths(__dirname),
	...{ core: core.bin }
};
