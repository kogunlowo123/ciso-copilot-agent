#!/bin/bash
set -euo pipefail
echo "Setting up CISO Copilot Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
