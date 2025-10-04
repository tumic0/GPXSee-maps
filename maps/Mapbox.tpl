<?xml version="1.0" encoding="UTF-8"?>
<!--
	This map requires a style for the Mapbox tile scheme like
	https://github.com/tumic0/QtPBFImagePlugin-styles/tree/master/Mapbox/bright
-->
<map xmlns="http://www.gpxsee.org/map/1.6">
	<name>Mapbox Vector Tiles</name>
	<url>https://c.tiles.mapbox.com/v4/mapbox.mapbox-streets-v7/$z/$x/$y.vector.pbf?access_token=insert-your-apikey-here</url>
	<tile type="vector" size="512" vectorLayers="landuse,waterway,water,aeroway,barrier_line,building,landuse_overlay,road,admin,country_label,marine_label,state_label,place_label,water_label,airport_label,rail_station_label,mountain_peak_label,poi_label,motorway_junction,road_label,waterway_label,housenum_label"/>
	<zoom max="18"/>
	<copyright>© Mapbox, © OpenStreetMaps</copyright>
</map>
