#README for redcap2BIDS

The current repository extract data from an xlsx file extracted from redcap in order to get a BIDS configuration. 
An example dataset is provided

Please follow these steps if you want to use the code

Login to redcap
Click « Data Exports, Reports, and Stats »
In line « All data », click « Export Data »
Choose « CSV / Microsoft Excel (raw data) ; « Remove All Identifier Fields » ;  « Set CSV delimiter character as comma »

Open excel
Open > your-redcap-data.csv
Click « Delimiter »
Click Next
Choose "comma" as delimiter
Click End

Save as « your-redcap-data.xslx » in folder BIDS

Open terminal
use ipython

copy-paste the scripts.

Don't forget to reinitialize the terminal before using a script
