---
noteId: "cde60a3020eb11ea962a0d96220f9408"
tags: [postgres, python, ETL, ipython]

---
<h2>Summary</h2>
---

This project involved the creation of an ETL process for a Postgres relational database. The first step required an understanding of the dataset that would be processed and the primary function of the database, to allow analysis on song play data for a music streaming application. 

A star schema was employed in order to create a fact table (Songplay) and associated dimensions (Users, Songs, Artists, and Time). The data modeling was followed by the creation of the relevant tables and insert queries, as well as the creation of the ETL steps needed to convert JSON files into intermediary Pandas dataframe and eventually inserted by row into the Postgres database. The database in this exercise is called ***Sparkifydb***.

<h2>Running Python Script</h2>
---

The first step is the creation of the database; the tables are defined in ***sql_queries.py***. This is accomplished by running the following command:

    >>python create_tables.py

***create_tables.py*** drops any existing database tables and reinitializes the tables needed. As a side note - a real ETL process would not drop tables at the outset as this would be unnecessary to destroy an existing datastore. Still, for this toy exercise, it allows for experimentation.

The next step is to run ***etl.py***:

    >>python etl.py
    71 files found in data/song_data
    1/71 files processed.
    2/71 files processed.
    3/71 files processed.
    4/71 files processed.
    5/71 files processed.
    ...
    30 files found in data/log_data
    1/30 files processed.
    2/30 files processed.
    3/30 files processed.
    4/30 files processed.
    5/30 files processed.
    ...
    >>

To test that the creation and insertion of records successfully get inserted, you need to run a ***test.ipynb***. This notebook contains the steps needed to connect to the sparkifydb database.



<h2>Files in Repository</h2>
---

The repository contains the following files:

<ol>
<li>data</li>
<li>create_tables.py</li>
<li>etl.ipynb</li>
<li>etl.py</li>
<li>README.md</li>
<li>sql_queries.py</li>
<li>test.ipynb</li>
</ol>

The data used in this exercise is stored inside the ***data*** folder, and it contains log_data and song_data as subdirectories. Inside each subdirectory are the JSON files that are parsed to fill the database.

The ***create_tables.py*** file, as was previously mentioned, initializes the database tables in the schema defined inside of ***sql_queries.py***.

The ***etl.ipynb*** and ***etl.py*** files are where the actual ETL process takes place. The python script gathers the paths to the data stored inside the relevant song and log data directories and then proceeds to process and insert the data into the correct table.

The last file is ***test.ipynb***, which allows for the ***sql_queries.py***, ***create_tables.py***, ***etl.py***, and ***etl.ipynb*** to be checked by connecting to the database and performing basic select statements that let you see what records are inside the database.