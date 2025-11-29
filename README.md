# 📄 PDF to CSV Table Extractor

A lightweight Python utility that automatically extracts all tables from any PDF and saves them as separate CSV files, preserving structure and handling uneven rows gracefully.

Perfect for automation projects, data extraction workflows, or quick table cleanup tasks.

## 🚀 Features

- Extracts every table from every page of a PDF

- Saves each table as a separate CSV file

- Automatically normalizes rows with missing columns

- Creates a dedicated output folder: <pdfname>_tables/

- Simple CLI usage

- 100% offline, no external APIs required

## 📦 Requirements

Install dependencies using:
~~~
pip install pdfplumber
or 
pip install -r requirements.txt
~~~
## 🛠️ Usage

### Run the script:
~~~
python3 pdf2csv.py <path/to.pdf>
~~~
#### Example:
~~~
python3 pdf2csv.py invoice.pdf
~~~
#### Output:  
A folder named: `invoice_tables/` at `<path>`

Inside it you'll find:
~~~
table1.csv
table2.csv
table3.csv
...
~~~

## 📁 How It Works

- Opens the PDF using `pdfplumber`

- Iterates through each page

- Detects tables using `extract_tables()`

- Cleans uneven rows by padding missing cells

- Saves each table to its own CSV inside an output directory

## ❗ Error Handling

- The script handles common issues:  

- Missing input file → prints an error  

- No tables detected → clean message  

- Mixed/uneven rows → automatically normalized

## 📝 Example Output
~~~
✓ Saved Table 1 → invoice_tables/table1.csv
✓ Saved Table 2 → invoice_tables/table2.csv

🎉 Extracted 2 tables into 'invoice_tables/'
~~~