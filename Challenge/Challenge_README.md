# Analysis of Election Audit

## Overview
The Colorado Board of Elections has requested an election audit for a U.S. Congressional Precinct. While this task is usually done manually in Excel, using Python allows for the automation of this task. Using Python, this analysis presents the total number of votes cast, a breakdown of total votes by County, and a breakdown of votes by Candidate.


## Election-Audit Results

* How many votes were cast in this congressional election?
    
    * There were 369,711 votes cast.

* How many votes did each County cast?
    * Jefferson County cast 38,855 votes (10.5%)
    * Denver County cast 306,055 votes (82.8%)
    * Arapahoe County cast 24,801 votes (6.7%)

* Which County had the highest turnout?
    * **Denver County** cast the highest number of votes!

* How many votes did each candidate receive?
    * Charles Casper Stockham received 85,213 votes (23.0%)
    * Diana DeGette received 272,892 votes (73.8%)
    * Raymon Anthony Doane received 11,606 votes (3.1%)

* Who won the election?
    * **Diana Degette** won the election with 272,892 votes (73.8%)!

## Election-Audit Summary

The script created to present this Election-Audit can be modified to analyze other elections going forward. So long as data for other elections are collected in a CSV file using a similar template as this election, the script is flexible enough to work!

To be used in any election, the script and data can be modified to take in the scope and location of the election. Say there is a similarly sized election in Georgia, if the data returned from the election has a column for scope and location the script can then be modified to take that in. For example, the .txt file's heading could look like:
```

Local Election Results for Georgia Congressional Precinct

```

This will make the output for each subsequent election clearer what it is analyzing!

For a larger election (perhaps at the federal level), both the data collected and script would have to be modified to account for the greater complexity in scope. For example in a federal election, every ballot's state can be taken in along with county and candidate. The following would be added to the script in this case:
 ```py
state_options = []
state_votes = {}
```
These variables would be used and iterated over in the same way  `county_options` and `county_votes`  are.




