# Resilient City Toolkit

The Resilient City Toolkit contains a set of tools for visualizing risks to urban infrastructure, and for adapting urban forms to reduce such risks.  General methods include re-sighting, landscape-scale hazard mitigation, and building-scale adaptation.  For resilience to flooding in particular, we have implemented New York City and FEMA recommendations.

The implementation of the Toolkit is based on a combination of web services and ESRI CityEngine 3D rules.  The web services are used to organize required base data, including adopting it to a single standard data schema used by downstream tools.  The intent is to provide a starting point for any community using readily-available national or international datasets.  Often a community has better local data, and this can be incorporated simply by adjusting that data to fit the RCT schema.  Primary requirements are:

1) Elevation data - Defaults to ESRI elevation service, for the US based on USGS National Elevation Data.  Best practice is to use a digital elevation model based on LIDAR if available.

2) Parcel boundaries OR building footprints OR building 3d models.  Best practices here vary based on local data availability.

3) Flood Planes OR FEMA DFIRM inundation models OR SLR simulations.  US defaults are FEMA DFIRM where available.  Best practices include tidally-corrected "bathtub" models of coastal innundation, or outputs of dynamic coastal models such as NOAA SLOSH were available.
