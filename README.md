# MOSS TTS Nano – Local Runner

Minimal script to generate speech from text using MOSS-TTS-Nano and measure inference speed.

---

## ⚙️ Requirements

* Linux or WSL (Ubuntu recommended)
* Python 3.10

---

## 🚀 Setup

```bash
git clone https://github.com/khushal-coder-learner/MOSS-TTS-Nano-wrapper.git
cd MOSS-TTS-Nano

chmod +x setup.sh
./setup.sh
```

---

## ▶️ Run

```bash
python run.py
```

You will be prompted to:

* Enter text
* Enter output file path (e.g. `output.wav`)

---

## ⚡ Example

```
Enter text: Hello, this is a test.
Enter output file: output.wav

Generating audio...

Done.
Saved to: /path/output.wav
Time taken: 12.34 seconds
```

---

## 🎯 Options

```bash
python run.py --voice Junhao
python run.py --prompt-audio assets/audio/zh_1.wav
```

---

## ⏱ Notes

* First run is slower (model loading)
* Later runs are faster (cached)
* Time taken is printed after generation

---

## ⚠️ Important

* Must run in Linux/WSL (Windows alone may fail due to dependencies)
* Stable internet required for first-time model download

---

## 🧩 Troubleshooting

If something breaks:

```bash
./setup.sh
```

---

## ✅ Quick Start

```bash
git clone ...
cd MOSS-TTS-Nano
./setup.sh
python run.py
```

---

That’s it.
