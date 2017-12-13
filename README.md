# Resilient City Toolkit

![alt tag](https://github.com/geodesign/slr/blob/master/SLR_Adaptation_Project/images/CE2017.1_Demo_Scene.gif)

## Overview
The Resilient City Toolkit contains a set of tools for visualizing risks to urban infrastructure, and for adapting urban forms to reduce such risks.  General methods include re-sighting, landscape-scale hazard mitigation, and building-scale adaptation.  The intial release contains tools primarily intended for flood resilience.  For resilience to flooding, we have implemented New York City, FEMA and EPA low impact development (LID) recommendations.

The implementation of the Toolkit is based on a combination of web services and ESRI CityEngine 3D rules.  The web services are used to organize required base data, including adopting it to a single standard data schema used by downstream tools.  The intent is to provide a starting point for any community using readily-available national or international datasets.  Often a community has better local data, and this can be incorporated simply by adjusting that data to fit the RCT schema.  

## Inputs
Primary requirements are:

1) Elevation data - Defaults to ESRI elevation service, for the US based on USGS National Elevation Data.  Best practice is to use a digital elevation model based on LIDAR if available.

2) Parcel boundaries OR building footprints OR building 3d models.  Best practices here vary based on local data availability.

3) Flood Planes OR FEMA DFIRM inundation models OR SLR simulations.  US defaults are FEMA DFIRM where available.  Best practices include tidally-corrected "bathtub" models of coastal innundation, or outputs of dynamic coastal models such as NOAA SLOSH were available.

## Process

These tools are organized to follow a geodesign process.  The general idea is to first build an existing conditions scenario, and then a set of alternative futures.  The futures vary along two primary dimensions: biophysical stressors, and adaptation actions.  Stressors can include various potential flood depths, or levels of sea level rise.  Adaptation measures include building elevation, internal building adaptation measures, and building removal, among others.  Importantly, adapation measures can be applied at an individual building scale, for a zone of interest, or for species sets of conditions across thousands of buildings.  

### Example of Interactive Exploration of Adaption Measures

![alt tag](https://github.com/geodesign/slr/blob/master/SLR_Adaptation_Project/images/CE2017.1_Adaptation_Options.gif)

## Outputs

The models produce a variety of outputs:  general vulnerability assessments, scenario-based risk assessments, economic damage assessments, and 3d visualizations.  
