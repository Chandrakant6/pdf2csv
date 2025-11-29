import sys
import os
import csv
import pdfplumber


def convert_pdf_to_csv_tables(input_path):
    base, _ = os.path.splitext(input_path)
    output_dir = base + "_tables"

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    table_count = 0

    with pdfplumber.open(input_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table in tables:
                if not table:
                    continue

                table_count += 1
                output_csv = os.path.join(output_dir, f"table{table_count}.csv")

                # Normalize uneven rows
                max_cols = max(len(r) for r in table)
                cleaned_rows = [
                    r + [""] * (max_cols - len(r)) for r in table
                ]

                # Write each table into its own CSV
                with open(output_csv, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(cleaned_rows)

                print(f"✓ Saved Table {table_count} → {output_csv}")

    if table_count == 0:
        print("❌ No tables detected in the PDF.")
    else:
        print(f"\n🎉 Extracted {table_count} tables into '{output_dir}/'")


def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf2csv_tables.py <pdf-file>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print("❌ File does not exist.")
        sys.exit(1)

    convert_pdf_to_csv_tables(input_path)


if __name__ == "__main__":
    main()
