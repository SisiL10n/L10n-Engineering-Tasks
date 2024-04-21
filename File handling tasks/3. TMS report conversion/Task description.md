File Handling Task: 


Your company is using a home-brew TMS to manage client and project data. Every time you receive a file, you analyze it in your CAT tool, generate a report from the CAT-tool, import the report to your system and create a quote using the information from both the report and your system. One day, a new client reached out. This client has its own TMS, and because of this they often have a report of their own. To keep consistency, you need to convert their report into a format that is readable to your system.


Below you will find a sample report from your system and your client’s system. Imagine the client report has more than 500 lines (which made it impossible to do a “manual” conversion). Try to write a script to convert the client’s report. 

Sample of your client’s report:2023-11-07_sampleProject_Metrics.xlsx
Sample of your own report: mySampleReport.csv

Here are the rules for the conversion:


In the client report, “word non-translatable”, “Words ICE Match” and “Words Leveraged Match” count towards “ICE Match” in your own report.


“95%-99%” in client report counts towards “90%-100%” in your own report.
“85%-94%” towards “”80%-90%”
“75-84” towards “70%-90%”
“Words no match” to “0%-60%”
“Words repeat” to “repetition”


Convert the client report to a report readable to your own system. 


Gentle reminder: your report is written in .csv format. And while a csv can be open with Microsoft Excel or Google Sheets, you need to open it in a text editor (like sublime text or notepad++) to get its details. 