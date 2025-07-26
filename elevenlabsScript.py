import os, csv
from elevenlabs import ElevenLabs, VoiceSettings

DIALOGUE_CSV = os.getenv("OUTPUT_CSV", "dialog_say_export.csv")
OUTPUT_AUDIO_DIR = os.getenv("OUTPUT_AUDIO_DIR", "audio_output")

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "7898AMdRTtesf0Y9zS54")
MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_turbo_v2_5")

eleven = ElevenLabs(api_key=API_KEY)

def generate_audio_from_csv(csv_path, output_dir, api_key, voice_id, model_id):
    os.makedirs(output_dir, exist_ok=True)
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row["text"]
            if not text.strip():
                continue
            filename = f"{row['filename']}_line{row['line_number']}.mp3"
            out_path = os.path.join(output_dir, filename)
            audio_gen = eleven.text_to_speech.convert(
                voice_id=voice_id,
                model_id=model_id,
                text=text,
                output_format="mp3_22050_32",
                voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.5)
            )
            with open(out_path, "wb") as out:
                for chunk in audio_gen:
                    out.write(chunk)
            print("Generated:", out_path)

if __name__ == "__main__":
    generate_audio_from_csv(DIALOGUE_CSV, OUTPUT_AUDIO_DIR, API_KEY, VOICE_ID, MODEL_ID)
