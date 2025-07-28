import os
from formatDialogue import export_d_files_to_csv, export_dialog_files_file_name
from elevenlabsScript import generate_audio_from_csv

print("Exporting dialogue files to CSV:")

DIALOG_EXTRACT_DIR = os.getenv("DIALOG_EXTRACT_DIR", "dialog-extract")
NARRATION_OUTPUT_CSV = os.getenv("NARRATION_OUTPUT_CSV", "narration_export.csv")
DIALOG_OUTPUT_CSV = os.getenv("DIALOG_OUTPUT_CSV", "dialog_export.csv")


OUTPUT_AUDIO_DIR = os.getenv("OUTPUT_AUDIO_DIR", "audio_output")
API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "7898AMdRTtesf0Y9zS54")
MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_turbo_v2_5")

if __name__ == "__main__":
    # print(export_dialog_files_file_name(DIALOG_EXTRACT_DIR))
    print(f"Exporting dialogue files from '{DIALOG_EXTRACT_DIR}' to '{DIALOG_OUTPUT_CSV}'")
    export_d_files_to_csv(DIALOG_EXTRACT_DIR, DIALOG_OUTPUT_CSV, NARRATION_OUTPUT_CSV)
    print(f"Generating audio files to '{OUTPUT_AUDIO_DIR}' using voice ID '{VOICE_ID}' and model ID '{MODEL_ID}'")
    generate_audio_from_csv(DIALOG_OUTPUT_CSV, OUTPUT_AUDIO_DIR, API_KEY, VOICE_ID, MODEL_ID)
    print("Export completed.")
