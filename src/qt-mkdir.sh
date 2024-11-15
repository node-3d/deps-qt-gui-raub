# $1 is tmp path - ${{ github.workspace }}/../__tmp

rm -rf $1
mkdir -p $1

mkdir -p $1/plugins
mkdir -p $1/plugins/platforms
mkdir -p $1/plugins/iconengines
mkdir -p $1/plugins/imageformats
