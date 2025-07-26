import os
from formatDialogue import export_d_files_to_csv
from elevenlabsScript import generate_audio_from_csv
# Example usage of the export_d_files_to_csv function

print("Exporting dialogue files to CSV:")

DIALOG_EXTRACT_DIR = os.getenv("DIALOG_EXTRACT_DIR", "dialog-extract")
OUTPUT_CSV = os.getenv("OUTPUT_CSV", "dialog_say_export.csv")

OUTPUT_AUDIO_DIR = os.getenv("OUTPUT_AUDIO_DIR", "audio_output")
API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "7898AMdRTtesf0Y9zS54")
MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_turbo_v2_5")

if __name__ == "__main__":
    print(f"Exporting dialogue files from '{DIALOG_EXTRACT_DIR}' to '{OUTPUT_CSV}'")
    export_d_files_to_csv(DIALOG_EXTRACT_DIR, OUTPUT_CSV)
    print(f"Generating audio files to '{OUTPUT_AUDIO_DIR}' using voice ID '{VOICE_ID}' and model ID '{MODEL_ID}'")
    generate_audio_from_csv(OUTPUT_CSV, OUTPUT_AUDIO_DIR, API_KEY, VOICE_ID, MODEL_ID)
    print("Export completed.")

# This script reads and prints the content of all .D files in the specified directory.

