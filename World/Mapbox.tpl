<?xml version="1.0" encoding="UTF-8"?>
<!--
	This map requires a style for the Mapbox tile scheme like
	https://github.com/tumic0/QtPBFImagePlugin-styles/tree/master/Mapbox/bright
	The default OpenMapTiles tile scheme style included in QtPBFImagePlugin
	won't display the map properly!
-->
<map xmlns="http://www.gpxsee.org/map/1.4">
	<name>Mapbox Vector Tiles</name>
	<url>https://c.tiles.mapbox.com/v4/mapbox.mapbox-streets-v7/$z/$x/$y.vector.pbf?access_token=insert-your-apikey-here</url>
	<!-- The tile size is 512px since QtPBFImagePlugin v2, use 256 if you have v1 -->
	<tile type="vector" size="512"/>
	<zoom max="18"/>
	<copyright>© Mapbox, © OpenStreetMaps</copyright>
</map>
