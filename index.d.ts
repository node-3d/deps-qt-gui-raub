declare module "deps-qt-gui-raub" {
	/**
	 * Exports of `deps-qt-core-raub`
	*/
	export const core: {
		bin: string;
		include: string;
	};
	
	/**
	 * Path to binaries
	 *
	 * Platform binary directory absolute path
	*/
	export const bin: string;
	/**
	 * Path to includes
	 *
	 * Include directory for this module
	*/
	export const include: string;
}
