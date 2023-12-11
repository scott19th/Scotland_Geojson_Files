
import geopandas as gpd
import os

output_dir = 'council_geo_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# mapping of council area names to GeoJSON filenames
geojson_files = {
    'Aberdeen City': 'ward_geo_files/S12000033.json',
    'Aberdeenshire': 'ward_geo_files/S12000034.json',
    'Angus': 'ward_geo_files/S12000041.json',
    'Argyll & Bute': 'ward_geo_files/S12000035.json',
    'City of Edinburgh': 'ward_geo_files/S12000036.json',
    'Clackmannanshire': 'ward_geo_files/S12000005.json',
    'Dumfries & Galloway': 'ward_geo_files/S12000006.json',
    'Dundee City': 'ward_geo_files/S12000042.json',
    'East Ayrshire': 'ward_geo_files/S12000008.json',
    'East Dunbartonshire': 'ward_geo_files/S12000045.json',
    'East Lothian': 'ward_geo_files/S12000010.json',
    'East Renfrewshire': 'ward_geo_files/S12000011.json',
    'Falkirk': 'ward_geo_files/S12000014.json',
    'Fife': 'ward_geo_files/S12000015.json',
    'Glasgow City': 'ward_geo_files/S12000046.json',
    'Highland': 'ward_geo_files/S12000017.json',
    'Inverclyde': 'ward_geo_files/S12000018.json',
    'Midlothian': 'ward_geo_files/S12000019.json',
    'Moray': 'ward_geo_files/S12000020.json',
    'Na h-Eileanan Siar': 'ward_geo_files/S12000013.json',
    'North Ayrshire': 'ward_geo_files/S12000021.json',
    'North Lanarkshire': 'ward_geo_files/S12000044.json',
    'Orkney Islands': 'ward_geo_files/S12000023.json',
    'Perth & Kinross': 'ward_geo_files/S12000024.json',
    'Renfrewshire': 'ward_geo_files/S12000038.json',
    'Scottish Borders': 'ward_geo_files/S12000026.json',
    'Shetland Islands': 'ward_geo_files/S12000027.json',
    'South Ayrshire': 'ward_geo_files/S12000028.json',
    'South Lanarkshire': 'ward_geo_files/S12000029.json',
    'Stirling': 'ward_geo_files/S12000030.json',
    'West Dunbartonshire': 'ward_geo_files/S12000039.json',
    'West Lothian': 'ward_geo_files/S12000040.json',
}

for council_area, filename in geojson_files.items():
    # Load the GeoJSON file (using os.path.join for proper path handling)
    file_path = os.path.join(filename)
    gdf = gpd.read_file(file_path)

    # Dissolve all ward polygons into a single geometry
    gdf_dissolved = gdf.dissolve()

    # Update the 'WD13NM' field to the current council area
    gdf_dissolved['WD13NM'] = council_area

    # Construct the output filename
    output_filename = os.path.join(output_dir, council_area.replace(' ', '_').lower() + '.geojson')

    # Save the result back to a new GeoJSON file
    gdf_dissolved.to_file(output_filename, driver='GeoJSON')

