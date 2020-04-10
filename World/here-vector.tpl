<?xml version="1.0" encoding="UTF-8"?>
<!--
	This map requires a style for the Tilezen tile scheme like
	https://github.com/tumic0/QtPBFImagePlugin-styles/blob/master/Tilezen/apollo-bright/style.json
	The default OpenMapTiles tile scheme style included in QtPBFImagePlugin
	won't display the map properly!
-->
<map xmlns="http://www.gpxsee.org/map/1.4">
	<name>HERE Vector Tiles</name>
	<url>https://vector.hereapi.com/v2/vectortiles/base/mc/$z/$x/$y/omv?apiKey=insert-your-apikey-here</url>
	<!-- The tile size is 512px since QtPBFImagePlugin v2, use 256 if you have v1 -->
	<tile type="vector" size="512"/>
	<zoom min="1" max="17"/>
	<copyright>HERE maps (various 3rd party sources)</copyright>
</map>
