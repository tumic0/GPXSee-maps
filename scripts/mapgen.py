#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import shutil
import codecs
import xml.etree.ElementTree as ET

COUNTRYCODES = {
	'AD': 'Andorra',
	'AE': 'United Arab Emirates',
	'AF': 'Afghanistan',
	'AG': 'Antigua & Barbuda',
	'AI': 'Anguilla',
	'AL': 'Albania',
	'AM': 'Armenia',
	'AN': 'Netherlands Antilles',
	'AO': 'Angola',
	'AQ': 'Antarctica',
	'AR': 'Argentina',
	'AS': 'American Samoa',
	'AT': 'Austria',
	'AU': 'Australia',
	'AW': 'Aruba',
	'AZ': 'Azerbaijan',
	'BA': 'Bosnia and Herzegovina',
	'BB': 'Barbados',
	'BD': 'Bangladesh',
	'BE': 'Belgium',
	'BF': 'Burkina Faso',
	'BG': 'Bulgaria',
	'BH': 'Bahrain',
	'BI': 'Burundi',
	'BJ': 'Benin',
	'BM': 'Bermuda',
	'BN': 'Brunei Darussalam',
	'BO': 'Bolivia',
	'BR': 'Brazil',
	'BS': 'Bahama',
	'BT': 'Bhutan',
	'BU': 'Burma (no longer exists)',
	'BV': 'Bouvet Island',
	'BW': 'Botswana',
	'BY': 'Belarus',
	'BZ': 'Belize',
	'CA': 'Canada',
	'CC': 'Cocos (Keeling) Islands',
	'CF': 'Central African Republic',
	'CG': 'Congo',
	'CH': 'Switzerland',
	'CI': 'Côte D\'ivoire (Ivory Coast)',
	'CK': 'Cook Iislands',
	'CL': 'Chile',
	'CM': 'Cameroon',
	'CN': 'China (PRC)',
	'CO': 'Colombia',
	'CR': 'Costa Rica',
	'CS': 'Czechoslovakia (no longer exists)',
	'CU': 'Cuba',
	'CV': 'Cape Verde',
	'CX': 'Christmas Island',
	'CY': 'Cyprus',
	'CZ': 'Czech Republic',
	'DD': 'German Democratic Republic (no longer exists)',
	'DE': 'Germany',
	'DJ': 'Djibouti',
	'DK': 'Denmark',
	'DM': 'Dominica',
	'DO': 'Dominican Republic',
	'DZ': 'Algeria',
	'EC': 'Ecuador',
	'EE': 'Estonia',
	'EG': 'Egypt',
	'EH': 'Western Sahara',
	'ER': 'Eritrea',
	'ES': 'Spain',
	'ET': 'Ethiopia',
	'FI': 'Finland',
	'FJ': 'Fiji',
	'FK': 'Falkland Islands (Malvinas)',
	'FM': 'Micronesia',
	'FO': 'Faroe Islands',
	'FR': 'France',
	'FX': 'France, Metropolitan',
	'GA': 'Gabon',
	'GB': 'United Kingdom (Great Britain)',
	'GD': 'Grenada',
	'GE': 'Georgia',
	'GF': 'French Guiana',
	'GH': 'Ghana',
	'GI': 'Gibraltar',
	'GL': 'Greenland',
	'GM': 'Gambia',
	'GN': 'Guinea',
	'GP': 'Guadeloupe',
	'GQ': 'Equatorial Guinea',
	'GR': 'Greece',
	'GS': 'South Georgia and the South Sandwich Islands',
	'GT': 'Guatemala',
	'GU': 'Guam',
	'GW': 'Guinea-Bissau',
	'GY': 'Guyana',
	'HK': 'Hong Kong',
	'HM': 'Heard & McDonald Islands',
	'HN': 'Honduras',
	'HR': 'Croatia',
	'HT': 'Haiti',
	'HU': 'Hungary',
	'ID': 'Indonesia',
	'IE': 'Ireland',
	'IL': 'Israel',
	'IN': 'India',
	'IO': 'British Indian Ocean Territory',
	'IQ': 'Iraq',
	'IR': 'Islamic Republic of Iran',
	'IS': 'Iceland',
	'IT': 'Italy',
	'JM': 'Jamaica',
	'JO': 'Jordan',
	'JP': 'Japan',
	'KE': 'Kenya',
	'KG': 'Kyrgyzstan',
	'KH': 'Cambodia',
	'KI': 'Kiribati',
	'KM': 'Comoros',
	'KN': 'St. Kitts and Nevis',
	'KP': 'Korea, Democratic People\'s Republic of',
	'KR': 'Korea, Republic of',
	'KW': 'Kuwait',
	'KY': 'Cayman Islands',
	'KZ': 'Kazakhstan',
	'LA': 'Lao People\'s Democratic Republic',
	'LB': 'Lebanon',
	'LC': 'Saint Lucia',
	'LI': 'Liechtenstein',
	'LK': 'Sri Lanka',
	'LR': 'Liberia',
	'LS': 'Lesotho',
	'LT': 'Lithuania',
	'LU': 'Luxembourg',
	'LV': 'Latvia',
	'LY': 'Libyan Arab Jamahiriya',
	'MA': 'Morocco',
	'MC': 'Monaco',
	'MD': 'Moldova, Republic of',
	'MG': 'Madagascar',
	'MH': 'Marshall Islands',
	'ML': 'Mali',
	'MN': 'Mongolia',
	'MM': 'Myanmar',
	'MO': 'Macau',
	'MP': 'Northern Mariana Islands',
	'MQ': 'Martinique',
	'MR': 'Mauritania',
	'MS': 'Monserrat',
	'MT': 'Malta',
	'MU': 'Mauritius',
	'MV': 'Maldives',
	'MW': 'Malawi',
	'MX': 'Mexico',
	'MY': 'Malaysia',
	'MZ': 'Mozambique',
	'NA': 'Namibia',
	'NC': 'New Caledonia',
	'NE': 'Niger',
	'NF': 'Norfolk Island',
	'NG': 'Nigeria',
	'NI': 'Nicaragua',
	'NL': 'Netherlands',
	'NO': 'Norway',
	'NP': 'Nepal',
	'NR': 'Nauru',
	'NT': 'Neutral Zone (no longer exists)',
	'NU': 'Niue',
	'NZ': 'New Zealand',
	'OM': 'Oman',
	'PA': 'Panama',
	'PE': 'Peru',
	'PF': 'French Polynesia',
	'PG': 'Papua New Guinea',
	'PH': 'Philippines',
	'PK': 'Pakistan',
	'PL': 'Poland',
	'PM': 'St. Pierre & Miquelon',
	'PN': 'Pitcairn',
	'PR': 'Puerto Rico',
	'PT': 'Portugal',
	'PW': 'Palau',
	'PY': 'Paraguay',
	'QA': 'Qatar',
	'RE': 'Réunion',
	'RO': 'Romania',
	'RU': 'Russian Federation',
	'RW': 'Rwanda',
	'SA': 'Saudi Arabia',
	'SB': 'Solomon Islands',
	'SC': 'Seychelles',
	'SD': 'Sudan',
	'SE': 'Sweden',
	'SG': 'Singapore',
	'SH': 'St. Helena',
	'SI': 'Slovenia',
	'SJ': 'Svalbard & Jan Mayen Islands',
	'SK': 'Slovakia',
	'SL': 'Sierra Leone',
	'SM': 'San Marino',
	'SN': 'Senegal',
	'SO': 'Somalia',
	'SR': 'Suriname',
	'ST': 'Sao Tome & Principe',
	'SU': 'Union of Soviet Socialist Republics (no longer exists)',
	'SV': 'El Salvador',
	'SY': 'Syrian Arab Republic',
	'SZ': 'Swaziland',
	'TC': 'Turks & Caicos Islands',
	'TD': 'Chad',
	'TF': 'French Southern Territories',
	'TG': 'Togo',
	'TH': 'Thailand',
	'TJ': 'Tajikistan',
	'TK': 'Tokelau',
	'TM': 'Turkmenistan',
	'TN': 'Tunisia',
	'TO': 'Tonga',
	'TP': 'East Timor',
	'TR': 'Turkey',
	'TT': 'Trinidad & Tobago',
	'TV': 'Tuvalu',
	'TW': 'Taiwan (Republic of China)',
	'TZ': 'Tanzania, United Republic of',
	'UA': 'Ukraine',
	'UG': 'Uganda',
	'UM': 'United States Minor Outlying Islands',
	'US': 'United States of America',
	'UY': 'Uruguay',
	'UZ': 'Uzbekistan',
	'VA': 'Vatican City State (Holy See)',
	'VC': 'St. Vincent & the Grenadines',
	'VE': 'Venezuela',
	'VG': 'British Virgin Islands',
	'VI': 'United States Virgin Islands',
	'VN': 'Viet Nam',
	'VU': 'Vanuatu',
	'WF': 'Wallis & Futuna Islands',
	'WS': 'Samoa',
	'YD': 'Democratic Yemen (no longer exists)',
	'YE': 'Yemen',
	'YT': 'Mayotte',
	'YU': 'Yugoslavia',
	'ZA': 'South Africa',
	'ZM': 'Zambia',
	'ZR': 'Zaire',
	'ZW': 'Zimbabwe',
	'ZZ': 'Unknown or unspecified country',
}


def sectionname(name):
	if name in COUNTRYCODES:
		return COUNTRYCODES[name]
	else:
		return name

def header(name, level):
	return "<h" + str(level) + ">" + name + "</h" + str(level) + ">\n"

def tile(xmlfile, suffix):
	base = os.path.splitext(os.path.basename(xmlfile))[0]
	tile = "tiles/" + base + suffix
	return tile

def mapinfo(xmlfile):
	with open(xmlfile) as f:
		xmlstring = f.read()
	xmlstring = re.sub('\\sxmlns="[^"]+"', '', xmlstring, count=1)
	root = ET.fromstring(xmlstring)

	info = {}
	for element in root:
		if element.tag == "name":
			info["name"] = element.text

	info["url"] = "maps/" + os.path.basename(xmlfile)

	png = tile(xmlfile, ".png")
	jpg = tile(xmlfile, ".jpg")
	if os.path.isfile("../" + png):
		info["tile"] = png
	elif os.path.isfile("../" + jpg):
		info["tile"] = jpg
	else:
		info["tile"] = "tiles/NA.png"

	return info

def processmaps(maps, htmlfile):
	htmlfile.write("<table>\n<tr>\n")

	items = []
	for xmlfile in maps:
		shutil.copyfile(xmlfile, "../maps/" + os.path.basename(xmlfile))
		items.append(mapinfo(xmlfile))
	items.sort(key=lambda tup: tup["name"])

	i = 0
	for info in items:
		if i and i % 4 == 0:
			htmlfile.write("</tr><tr>\n")
		template = "  <small>[TPL]</small>" if info["url"].endswith(".tpl") else ""
		htmlfile.write("<td>" + "<a href=\"" + info["url"] + "\" download><img src=\""
		  + info["tile"]
		  + "\" alt=\"Map Preview\" width=\"256\" height=\"256\"/></a><br/>"
		  + info["name"] + template + "</td>\n")
		i = i + 1

	htmlfile.write("</tr>\n</table>\n")

def processdir(path, level, name, htmlfile):
	maps = []
	sections = []

	entries = os.listdir(path)
	for entry in entries:
		entrypath = os.path.join(path, entry)
		if (os.path.isdir(entrypath)):
			sections.append((sectionname(entry), entrypath))
		else:
			maps.append(entrypath)

	if maps:
		processmaps(maps, htmlfile)
	sections.sort()
	for section in sections:
		htmlfile.write(header(section[0], level + 1))
		processdir(section[1], level + 1, section[0], htmlfile)


if len(sys.argv) < 2:
	sys.stderr.write("Usage: " + os.path.basename(sys.argv[0]) + " WORLDDIR\n")
	sys.exit(-1)

htmlfile = codecs.open("../index.html", "w", encoding='utf-8')

htmlfile.write("""<!DOCTYPE html>
<html lang="en">
<head>
<title>GPXSee Online Maps</title>
<link rel="stylesheet" href="style.css" type="text/css" media="all"/>
<meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
</head>

<body>
<div class="center">
<h1>GPXSee Online Maps</h1>
<p><a href="https://www.gpxsee.org">GPXSee</a> online map definition files
ready to use. Simply download the XML file and open it in GPXSee as a map
file. To use the map permanently, copy the file to the &quot;maps&quot;
directory as found under Help->Paths.</p>
<p><small>Some maps require API keys or user credentials. Such map definition
files have a &quot;.tpl&quot; extension instead of the usual &quot;.xml&quot;
extension. You must fill in the required info and rename the file before you
can use it in GPXSee.</small></p>
""")

htmlfile.write(header("Worldwide", 2))
processdir(sys.argv[1], 1, os.path.basename(sys.argv[1]), htmlfile)

htmlfile.write("""
</div>
</body>
</html>
""")

htmlfile.close()
