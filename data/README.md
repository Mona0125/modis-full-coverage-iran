# Data Directory

This directory is intended for local geospatial input data required by the notebook.

## Iran Boundary Data

Before running the notebook, place the Iran boundary shapefile and its associated files in this directory.

A shapefile normally includes several related files, such as:

```text
iran_boundary.shp
iran_boundary.shx
iran_boundary.dbf
iran_boundary.prj
```

All associated shapefile components must have the same base filename.

## Important Notes

- Large datasets should not be committed to this repository.
- Downloaded satellite data should remain on the user's local system.
- Users must follow the license and attribution requirements of the original data provider.
- The notebook path configuration may need to be updated to match the actual boundary filename.
