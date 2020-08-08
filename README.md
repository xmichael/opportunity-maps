# opportunity-maps

Facilitates (semi-)automatic generation of opportunity maps from geospatial data.

## Usage

The software will currently modify a CSV file by applying a Jenks classification on a value of interest and create a new column with the results:

```
usage: natural_breaks_csv.py [-h] [-n N] [--plot] input_file output_file field_name

Classify CSV file using Natural Breaks (Jenks) algorithm.

positional arguments:
  input_file   input CSV file
  output_file  input CSV file
  field_name   field name of the CSV file. e.g. "SCORE"

optional arguments:
  -h, --help   show this help message and exit
  -n N         number of classes (default: 10)
  --plot       plot classification result (default: False)
```
