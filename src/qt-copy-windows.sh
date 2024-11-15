# $1 is tmp path - ${{ github.workspace }}/../__tmp
# $2 is Qt platform path - /home/opc/6.8.0/gcc_arm64

# Gui
cp $2/bin/Qt6Gui.dll $1/Qt6Gui.dll
cp $2/bin/Qt6OpenGL.dll $1/Qt6OpenGL.dll
cp $2/bin/Qt6Svg.dll $1/Qt6Svg.dll
cp $2/bin/Qt6Widgets.dll $1/Qt6Widgets.dll
cp $2/plugins/iconengines/qsvgicon.dll $1/plugins/iconengines/qsvgicon.dll
cp $2/plugins/imageformats/qgif.dll $1/plugins/imageformats/qgif.dll
cp $2/plugins/imageformats/qico.dll $1/plugins/imageformats/qico.dll
cp $2/plugins/imageformats/qjpeg.dll $1/plugins/imageformats/qjpeg.dll
cp $2/plugins/imageformats/qsvg.dll $1/plugins/imageformats/qsvg.dll
cp $2/plugins/platforms/qoffscreen.dll $1/plugins/platforms/qoffscreen.dll
cp $2/plugins/platforms/qwindows.dll $1/plugins/platforms/qwindows.dll
