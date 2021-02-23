/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    config.font_names = config.font_names + '微软雅黑;宋体;黑体;仿宋_GB2312;楷体_GB2312;隶书;幼圆;';
    config.disallowedContent = 'img{width,height};img[width,height]';
};
