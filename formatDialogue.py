import os, csv
import re

DIALOG_EXTRACT_DIR = os.getenv("DIALOG_EXTRACT_DIR", "dialog-extract")
DIALOG_EXTRACT_CSV = os.getenv("DIALOG_EXTRACT_CSV", "dialog_extract.csv")
NARRATION_EXTRACT_CSV = os.getenv("NARRATION_EXTRACT_CSV", "narration_extract.csv")

def export_dialog_files_file_name(directory):
    d_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(".d"):
            d_files.append(filename)
    return d_files

def export_d_files_to_csv(directory, output_csv, narration_output_csv):
    say_pattern = re.compile(r'^\s*SAY\s+#?(\d+)?\s*/\*\s*~(.*?)~\s*\*/', re.IGNORECASE)
    # Match lines where the text starts with double quotes (after trimming)
    speaking_pattern = re.compile(r'^"')
    introduction_pattern = re.compile(r"\b(I am|I'm|My name is|call me)\b", re.IGNORECASE)
    # Read existing narration rows into a dict for update logic
    narration_rows = {}
    if os.path.exists(narration_output_csv):
        with open(narration_output_csv, "r", encoding="utf-8") as narrationfile:
            reader = csv.DictReader(narrationfile)
            for row in reader:
                filename = row["filename"]
                narration_rows[filename] = {
                    "line_number": row["line_number"],
                    "say_id": row["say_id"],
                    "possible_speaking": row["possible_speaking"]
                }

    # Process current run and update narration_rows as needed
    for filename in os.listdir(directory):
        if filename.endswith(".D"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    match = say_pattern.search(line)
                    if match:
                        text = match.group(2).strip()
                        say_id = match.group(1) or ""
                        if speaking_pattern.match(text):
                            possible_speaking = None
                            if introduction_pattern.search(text):
                                intro_match = introduction_pattern.search(text)
                                if intro_match:
                                    start = intro_match.start()
                                    words = text[start:].split()
                                    possible_speaking = " ".join(words[:8])
                            # Always keep the last/most recent row for this filename
                            narration_rows[filename] = {
                                "line_number": str(i),
                                "say_id": say_id,
                                "possible_speaking": possible_speaking
                            }
                        # else: handled below for main CSV

    # Write out the narration rows (one per filename)
    with open(narration_output_csv, "w", newline='', encoding="utf-8") as narrationfile:
        narration_writer = csv.writer(narrationfile)
        narration_writer.writerow(["filename", "line_number", "say_id","possible_speaking"])
        for filename, row in sorted(narration_rows.items()):
            narration_writer.writerow([filename, row["line_number"], row["say_id"], row["possible_speaking"]])

    # Write out the main CSV as before
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
                            text = match.group(2).strip()
                            say_id = match.group(1) or ""
                            if speaking_pattern.match(text):
                                # This is a speaking line, do not write to narration
                                writer.writerow([filename, i, say_id, text])
                            else:
                                # This is narration, write to main CSV
                                writer.writerow([filename, i, say_id, text])

if __name__ == "__main__":
    export_d_files_to_csv(DIALOG_EXTRACT_DIR, DIALOG_EXTRACT_CSV, NARRATION_EXTRACT_CSV)
    print(f"Exported SAY lines from '{DIALOG_EXTRACT_DIR}' to '{DIALOG_EXTRACT_CSV} & {NARRATION_EXTRACT_CSV}'")