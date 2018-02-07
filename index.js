'use strict';

const path = require('path');

const tools = require('addon-tools-raub');

require('deps-qt-core-raub');


const coreInclude = path.dirname(require.resolve('deps-qt-core-raub')).replace(/\\/g, '/');

module.exports = {
	...tools.paths(__dirname),
	...{ core: tools.paths(coreInclude).bin }
};

console.log('index.js', module.exports);
