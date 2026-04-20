import argparse
import subprocess
from pathlib import Path
import time

def run_infer(text, prompt_audio_path, output_path = None):
    cmd = ["python", "infer.py", "--text", text, "--prompt-audio-path", prompt_audio_path]

    if output_path:
        cmd.extend(["--output-audio-path", str(output_path)])

    start = time.time()
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end = time.time()
    duration = end - start

    return duration


def main():
    parser = argparse.ArgumentParser(description="Simple TTS wrapper using infer.py")
    parser.add_argument("--text", type=str, help="Text to synthesize")


    args = parser.parse_args()

    text = args.text or input("Enter text: ").strip()
    output = input("Enter output file (e.g. output.wav): ").strip()
    prompt_audio = input("Enter prompt audio path: ").strip()

    duration = run_infer(
        text=text,
        output_path=output,
        prompt_audio_path=prompt_audio,
    )

    print(f"\nSaved to: {output}")
    print(f"Time taken: {duration:.2f} seconds")


if __name__ == "__main__":
    main()