'use strict';

require('node-deps-qt-core-raub');

const os = require('os');

const addonPaths = {
	win32 : '/bin_win32/webgl' ,
	linux : '/bin_linux/webgl' ,
	darwin: '/bin_darwin/webgl',
};

process.env.path += ';' + __dirname + addonPaths[os.platform()];

module.exports = __dirname;
