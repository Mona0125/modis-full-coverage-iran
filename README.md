🌍 MODIS Full Coverage Over Iran
Identify 100% spatially covered MODIS MOD02/MYD02 overpasses across Iran
<p align="left"> <img src="https://img.shields.io/badge/Python-3.9%2B-blue" /> <img src="https://img.shields.io/badge/Remote%20Sensing-MODIS-orange" /> <img src="https://img.shields.io/badge/NASA-Earthdata-lightgrey" /> <img src="https://img.shields.io/badge/Geospatial-Analysis-green" /> </p>

This project analyzes MODIS MOD02/MYD02 overpasses to determine which dates and times provide full (100%) coverage over Iran.
It retrieves MODIS swath metadata from NASA Earthdata, extracts spatial geometry, computes coverage percentage, and generates visual + analytical outputs.

🚀 Features

🔍 Query MOD021KM granules using NASA Earthdata API

🛰 Extract MODIS swath boundaries (BoundingBox or Polygon)

📐 Compute coverage percentage over Iran

🌍 Generate interactive HTML maps

📊 Export Excel reports (granule metadata + coverage)

📁 Organized project structure for reproducible workflows

📁 Repository Structure
modis-full-coverage-iran/
│── modis-full-coverage-iran.ipynb     # Main analysis notebook
│── requirements.txt                    # Dependencies
│── README.md                           # Documentation
│── data/                               # Iran shapefile (you add this)
│── output/                             # Results (HTML + Excel)

🔧 Requirements

Install dependencies:

pip install -r requirements.txt


Core libraries:

earthaccess

geopandas

shapely

pandas

folium

openpyxl

▶️ Usage

Clone this repository:

git clone https://github.com/Mona0125/modis-full-coverage-iran


Place the Iran shapefile in the data/ folder:

data/
   └── gadm41_IRN_0.shp


Open the notebook:

modis-full-coverage-iran.ipynb


Run all cells

Outputs will be saved in:

output/
   ├── MODIS_Iran_Coverage_Map_*.html
   └── MODIS_Iran_Results_*.xlsx

📊 Output Examples
✔ HTML Interactive Map

Generated with Folium — displaying MODIS swaths intersecting Iran with color-coded coverage levels.

✔ Excel Report

Includes:

Granule ID

Start/End time

Swath size

Coverage percentage

Summary row

🛰 Data Source

MODIS MOD02 (Terra)

MODIS MYD02 (Aqua)

NASA Earthdata Search API

💬 Author

Mona Fakhri
MSc Student in Remote Sensing Engineering
📍 Iran

📜 License

This project is open for research and academic use.
Feel free to modify and extend.
