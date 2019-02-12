CORE_DIR="$1"
GUI_DIR="$2"

install_name_tool -add_rpath "$CORE_DIR" "$GUI_DIR/plugins/platforms/libqcocoa.dylib" \
&& install_name_tool -add_rpath "$GUI_DIR" "$GUI_DIR/plugins/platforms/libqcocoa.dylib" \
|| echo "Rpath already present."
