#!/bin/bash

set -e

echo "🚀 Setting up MOSS-TTS-Nano..."

# ---- Check Python ----
if ! command -v python3.10 &> /dev/null
then
    echo "❌ Python 3.10 not found. Please install it first."
    exit 1
fi

# ---- Create venv ----
echo "📦 Creating virtual environment..."
python3.10 -m venv .venv
source .venv/bin/activate

# ---- Upgrade pip ----
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# ---- Install PyTorch (fast source) ----
echo "⚡ Installing PyTorch (CPU version)..."
pip install torch==2.7.0 torchaudio==2.7.0 \
  --index-url https://download.pytorch.org/whl/cpu

# ---- Install WeTextProcessing ----
echo "⚡ Installing WeTextProcessing..."
pip install WeTextProcessing

# ---- Install remaining dependencies ----
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "👉 IMPORTANT:"
echo "Make sure the virtual environment is activated before running the script."
echo ""
echo "To activate:"
echo "source .venv/bin/activate"
echo ""
echo "Then run:"
echo "python run.py"