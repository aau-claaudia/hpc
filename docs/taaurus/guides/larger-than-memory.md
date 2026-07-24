# Larger than memory

Sometimes we can find ourselves in a situation, where the dataset we want to work with is larger than what we can fit into the memory of the compute host we are working on. Provided that we have room foor it on the disk, a solution to this problem could be to make use of a library that allows us to work with the data directly from the disk.

## DuckDB

DuckDB can do exactly this. One great advantage of using DuckDB, is that integrates well with R's built-in database interface (`DBI`), which allows us to use it as a drop-in replacement for existing methods for reading data, while still being able to query the data with well known libraries, such as `dplyr` and `bioconductor`. Since DuckDB operations are paralellized out of the box, we can expect DuckDB to deliver high performance.

# Installing DuckDB

DuckDB can be installed from `CRAN` using your preferred method for [software environments](/taaurus/guides/getting-containers/).

```R
install.packages("duckdb")
```

## Working with DuckDB

We could load the libary like so:

```R
library(duckdb)
```

Initiate the database connection:
```R
con <- dbConnect(duckdb(), dbdir = ".duckbdb")
```
With the `dbdir` argument, we specify that this should be a file on disk.
At first the file will represent an empty database, and it will only contain the metadata required for duckdb to manage it as such.

### Reading in the dataset

With the function `dbGetQuery()`, we can define a SQL query to populate our database.

If we wanted to read in the entire dataset, we would say:

```R
large_dataset <- dbGetQuery(con, "SELECT * FROM read_csv_auto('big_data.csv')")
```

We should note that this process will store the result of the query in memory. If we attempt to read in a larger-than-memory dataset, this process will fail.
Instead we should create a table in our database:
```R
dbExecute(con, "CREATE TABLE large_data AS SELECT * FROM read_csv_auto('big_data.csv')")
```

??? note "Storing database tables"

    Note that here we are creating a new table inside the database. When the table create is created to reflect the entirety of our dataset, a copy is stored in the dataset file. Although this copy is compressed slightly by default, we must ensure that we have enough disk space. In most cases, this will not be a problem since available disk space is almost always much greater than available RAM.

### Querying the dataset

We can query the table using SQL syntax, like so:
```R
result <- dbGetQuery(con, "SELECT * FROM large_data LIMIT 10")
print(result)
```

We can also query the dataset using R libraries.

First create a lazy table pointing to the DuckDB table:
```R
large_dataset <- tbl(con, "large_data")
```
And query the data with some dplyr functions:

```R
large_dataset %>%
filter(Age >= 65) %>%
group_by(Age) %>%
summarise(n = mean(Height_cm)) %>%
arrange(Age) %>%
collect()
```

