import os, csv
import re

DIALOG_EXTRACT_DIR = os.getenv("DIALOG_EXTRACT_DIR", "dialog-extract")
OUTPUT_CSV = os.getenv("OUTPUT_CSV", "dialog_say_export.csv")

def export_d_files_to_csv(directory, output_csv):
    say_pattern = re.compile(r'^\s*SAY\s+#?(\d+)?\s*/\*\s*~(.*?)~\s*\*/', re.IGNORECASE)
    with open(output_csv, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "line_number", "say_id", "text"])
        for filename in os.listdir(directory):
            if filename.endswith(".D"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f, 1):
                        match = say_pattern.search(line)
                        if match:
                            say_id = match.group(1) or ""
                            text = match.group(2).strip()
                            writer.writerow([filename, i, say_id, text])

if __name__ == "__main__":
    export_d_files_to_csv(DIALOG_EXTRACT_DIR, OUTPUT_CSV)
    print(f"Exported SAY lines from '{DIALOG_EXTRACT_DIR}' to '{OUTPUT_CSV}'")