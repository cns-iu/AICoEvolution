# AICoEvolution

## Stakeholder Needs Analysis and User Study

A stakeholder needs analysis (SNA) was employed in order to identify insight needs and use cases for using indicators and visualizations of emergence (and indirectly convergence) in daily decision making environments.

A user study was employed to examine the visualizations on terns of utility and readability.

- User Needs Analysis 
   - [online survey]{https://iu.co1.qualtrics.com/jfe/form/SV_9HzcwI1BNTy6gM5}
   - survey form: /User-Study/User Need Analysis Instrument.pdf

- User Study 
   - [online survey link](https://iu.co1.qualtrics.com/jfe/form/SV_6h4hvTKlnVW410h)
   - survey form: /User-Study/User Study Analysis Instrument.pdf

## Data

Data Statistics: /code/datset-crane-stats.ipynb

## Keyword Extraction - MaxMatch

Using results from a linguistic algorithm comparison detailed in Börner et al. (2018), the MaxMatch algorithm (Wong & Chan, 1996)was used to identify terms in NSF funding awards that match the unique WOS Author Keywords specific to the three topic areas. Characters like [ ] { } and” were removed. See Appendix for extracted keywords disambiguation and normalization.

Maxmatch code: /Code/Maxmatch in Python.ipynb



## Network Layout Algorithms

Gephi (Version 0.9.2) (Bastian, Heymann, & Jacomy, 2009) was used to compute data overlays with the following plugins:

-	*ForceAtlas2* was used to layout the Co-Author Network figure
-	*GeoLayout* was used to create 1) the Co-Author network overlaid on US map with mercator basemap and the Temporal Convergence figure using x-y coordinates to display nodes. 

## Burst Detection

Burst Detection uses Kleinberg's algorithm available in Sci2 (Sci2 Team, 2009). See the burst visualization code in Code section.
 
