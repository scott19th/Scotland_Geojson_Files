# Scotland_Geojson_Files
This repository contains the two versions of Scottish Council Area geojson files. One with the wards which collectively make up the council area and one without. I spent some time getting these in the right format to create a Python Plotly Choropleth and thought they may be useful to others who wish to represent data by council or ward in map format.

The Scotland_Councils_With_Wards_Geojson folder contains the original geojson files for each council area of Scotland. Each of these Geojson files contains multiple 'features' which represent the constituent wards which make up the council area. This would be suitable is you had data at a ward level for each council but for my purposes I wanted to create a choropleth chart with data representing each of Scotlands 32 council areas as a whole.

The Scotland_Councils_Without_Wards_Geojson folder contains the outpout geojson files which represent each of the 32 Scottish council areas as a single feature. 

Ward_to_Council_Converter.py Python file is the script I used to remove the sub features, in this case the Scottish wards which make up each council area. If you wanted to use this script on another set of files you would need to remap the 'geojson_files' dictionary so the key represents the new consolidated feature the and the value points to the geojson file you wish to convert.


