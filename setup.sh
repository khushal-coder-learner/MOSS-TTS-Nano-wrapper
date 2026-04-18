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

# ---- Install remaining dependencies ----
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo "👉 Run: python run.py"