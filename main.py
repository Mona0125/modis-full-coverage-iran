from src.modis_download import download_modis
from src.coverage_analysis import calculate_coverage
from src.visualization import create_map


def main():

    granules = download_modis()

    results = calculate_coverage(granules)

    create_map(results)


if __name__ == "__main__":
    main()
