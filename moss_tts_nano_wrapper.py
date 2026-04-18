from __future__ import annotations

import argparse
import time
from pathlib import Path

import torchaudio

from moss_tts_nano_runtime import NanoTTSService


def generate_tts(
    *,
    runtime: NanoTTSService,
    text: str,
    output_path: str | Path,
    voice: str | None = None,
    mode: str = "voice_clone",
    prompt_audio_path: str | Path | None = None,
    prompt_text: str | None = None,
) -> dict[str, object]:
    result = runtime.synthesize(
        text=text,
        voice=voice,
        mode=mode,
        output_audio_path=output_path,
        prompt_audio_path=prompt_audio_path,
        prompt_text=prompt_text,
    )

    saved_path = Path(str(result["audio_path"])).expanduser()
    if not saved_path.exists():
        waveform = result["waveform"]
        sample_rate = int(result["sample_rate"])
        torchaudio.save(str(output_path), waveform.unsqueeze(0), sample_rate)
        result["audio_path"] = str(Path(output_path).expanduser().resolve())

    return result


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal Nano-TTS wrapper (no WeTextProcessing required).")
    parser.add_argument("--text", type=str, default="", help="Text to synthesize.")
    parser.add_argument("--output", type=str, default="", help="Output WAV path.")
    parser.add_argument("--voice", type=str, default="", help="Voice preset name (e.g. Junhao, Trump).")
    parser.add_argument("--list-voices", action="store_true", help="Print available voice presets and exit.")
    parser.add_argument("--mode", type=str, default="voice_clone", choices=["voice_clone", "continuation"])
    parser.add_argument("--prompt-audio", type=str, default="", help="Prompt audio path (optional).")
    parser.add_argument("--prompt-text", type=str, default="", help="Prompt text (required for continuation mode).")
    parser.add_argument("--device", type=str, default="auto", help="auto/cpu/cuda (or e.g. cuda:0).")
    parser.add_argument("--dtype", type=str, default="auto", help="auto/float32/float16/bfloat16.")
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="",
        help="HF model id or local path for MOSS-TTS-Nano (default: OpenMOSS-Team/MOSS-TTS-Nano).",
    )
    parser.add_argument(
        "--audio-tokenizer",
        type=str,
        default="",
        help="HF model id or local path for MOSS-Audio-Tokenizer-Nano (default: OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano).",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()

    runtime_kwargs: dict[str, object] = {"device": args.device, "dtype": args.dtype}
    checkpoint = str(args.checkpoint).strip()
    audio_tokenizer = str(args.audio_tokenizer).strip()
    if checkpoint:
        runtime_kwargs["checkpoint_path"] = checkpoint
    if audio_tokenizer:
        runtime_kwargs["audio_tokenizer_path"] = audio_tokenizer
    runtime = NanoTTSService(**runtime_kwargs)

    if bool(args.list_voices):
        print("Available voices")
        print("---------------")
        for voice_name in sorted(runtime.voice_presets):
            preset = runtime.voice_presets[voice_name]
            exists = "ok" if preset.prompt_audio_path.exists() else "missing"
            print(f"- {preset.name} [{exists}] {preset.prompt_audio_path}")
        return 0

    text = str(args.text or "").strip() or input("Enter text: ").strip()
    output_path = str(args.output or "").strip() or input("Enter output file (e.g. output.wav): ").strip()
    voice = str(args.voice or "").strip() or None
    prompt_audio_path = str(args.prompt_audio or "").strip() or None
    prompt_text = str(args.prompt_text or "").strip() or None

    print("\nGenerating audio...\n")
    started = time.time()
    result = generate_tts(
        runtime=runtime,
        text=text,
        output_path=output_path,
        voice=voice,
        mode=str(args.mode),
        prompt_audio_path=prompt_audio_path,
        prompt_text=prompt_text,
    )
    elapsed = time.time() - started

    print("Done.")
    print(f"Saved to: {result['audio_path']}")
    print(f"Voice: {result.get('voice')} | Mode: {result.get('mode')}")
    print(f"Time taken: {elapsed:.2f} seconds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
