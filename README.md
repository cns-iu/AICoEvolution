# AICoEvolution

## Stakeholder Needs Analysis and User Study

A stakeholder needs analysis (SNA) was employed in order to identify insight needs and use cases for using indicators and visualizations of emergence (and indirectly convergence) in daily decision making environments.

A user study was employed to examine the visualizations on terns of utility and readability.

- User Needs Analysis 
   - [online survey](https://iu.co1.qualtrics.com/jfe/form/SV_9HzcwI1BNTy6gM5)
   - survey form: /User-Study/User Need Analysis Instrument.pdf

- User Study 
   - [online survey link](https://iu.co1.qualtrics.com/jfe/form/SV_6h4hvTKlnVW410h)
   - survey form: /User-Study/User Study Analysis Instrument.pdf

## Data

Data Statistics: /code/dataset-crane-stats.ipynb

i.	Web of Science database:

We extracted data consisting of two columns, WOS_id and WOS_ref from Web of Science database. Each row represents the source and target of references. WOS_id and WOS_ref consist of unique identification number assigned to a paper.  We extracted three csv files, corresponding to each field of interest (AI, IoT and Robotics). See WoS relational database schema - Link: https://cadre.iu.edu/resources/documentation/wos_core_erd%20(1).pdf

ii.	Web of Science Online Portal:

We used Institute of Scientific Information (ISI) publication data from Web of Science Online Portal to get the year and other relevant descriptions of papers. ISI files are converted to CSV using Make-a-Vis available at https://make-a-vis.netlify.com/

## Keyword Extraction - MaxMatch

Using results from a linguistic algorithm comparison detailed in Börner et al. (2018), the MaxMatch algorithm (Wong & Chan, 1996)was used to identify terms in NSF funding awards that match the unique WOS Author Keywords specific to the three topic areas. Characters like [ ] { } and” were removed. See Appendix for extracted keywords disambiguation and normalization.

Maxmatch Algorithm is describe in the repository for the paper "Skill Discrepancies Between Research, Education, and Jobs Reveal the Critical Need to Supply Soft Skills for the Data Economy" (https://github.com/cns-iu/cjobs)[https://github.com/cns-iu/cjobs].

## Network Layout Algorithms

Gephi (Version 0.9.2) (Bastian, Heymann, & Jacomy, 2009) was used to compute data overlays with the following plugins:

-	*ForceAtlas2* was used to layout the Co-Author Network figure
-	*GeoLayout* was used to create 1) the Co-Author network overlaid on US map with mercator basemap and the Temporal Convergence figure using x-y coordinates to display nodes. 

Data processing is describe in Workflow CRANE (see Appendix folder).

## Burst Detection

Burst Detection uses Kleinberg's algorithm available in Sci2 (Sci2 Team, 2009). See the burst visualization code in Code section.
 
