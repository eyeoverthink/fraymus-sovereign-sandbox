# ============================================================================
# FRAYMUS SOVEREIGN SANDBOX — NATIVE AUTONOMY & RSI MAKEFILE
# Designed for Hermes, OpenClaw, GitHub Copilot, and Local Sovereign Nodes
# Zero proprietary cloud dependencies.
# ============================================================================

PYTHON ?= python3
PORT ?= 8080
OLLAMA_URL ?= http://127.0.0.1:11434
REPO_BRANCH ?= main

.PHONY: help bootstrap verify-opeg rsi-cycle hermes-daemon openclaw-agent sync-hemispheres serve git-push

help:
	@echo "======================================================================"
	@echo " FRAYMUS SOVEREIGN SANDBOX // HERMES + OPENCLAW + COPILOT RSI ENGINE"
	@echo "======================================================================"
	@echo "  make bootstrap        - Verify Python, Git, and directory structure"
	@echo "  make verify-opeg      - Run OPEG-V1.0 (Sigma -> R_san) & 4D Voxel check"
	@echo "  make rsi-cycle        - Execute 1 full 5-Stage Recursive Self-Improvement pass"
	@echo "  make hermes-daemon    - Run continuous Hermes + OpenClaw RSI loop (every 30m)"
	@echo "  make sync-hemispheres - Beam latest Git ledger to Creator Nexus & Fraymus Eternal"
	@echo "  make serve            - Launch standalone 4D Micro-Instrument UI on :$(PORT)"
	@echo "  make git-push         - Commit & push verified RSI artifacts to GitHub"

bootstrap:
	@mkdir -p agents artifacts
	@$(PYTHON) hermes_rsi_daemon.py --mode bootstrap

verify-opeg:
	@$(PYTHON) hermes_rsi_daemon.py --mode verify

rsi-cycle:
	@$(PYTHON) hermes_rsi_daemon.py --mode rsi-once --ollama-url $(OLLAMA_URL)

hermes-daemon:
	@$(PYTHON) hermes_rsi_daemon.py --mode daemon --interval 1800 --ollama-url $(OLLAMA_URL)

sync-hemispheres:
	@$(PYTHON) hermes_rsi_daemon.py --mode sync-bridges

serve:
	@echo "Serving standalone Base44-free 4D Sandbox at http://127.0.0.1:$(PORT)"
	@$(PYTHON) -m http.server $(PORT)

git-push:
	@git add -A
	@git commit -m "[Hermes/OpenClaw RSI] Autonomous verified evolution step" || true
	@git push origin $(REPO_BRANCH)
