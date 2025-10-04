<?xml version="1.0" encoding="UTF-8"?>
<!--
	This map requires a style for the Tilezen tile scheme like
	https://github.com/tumic0/QtPBFImagePlugin-styles/blob/master/Tilezen/apollo-bright
-->
<map xmlns="http://www.gpxsee.org/map/1.6">
	<name>HERE Vector Tiles</name>
	<url>https://vector.hereapi.com/v2/vectortiles/base/mc/$z/$x/$y/omv?apiKey=insert-your-apikey-here</url>
	<tile type="vector" size="512" vectorLayers="boundaries,buildings,earth,landuse,places,pois,roads,road_labels,transit,water"/>
	<zoom min="1" max="17"/>
	<copyright>HERE maps (various 3rd party sources)</copyright>
</map>
