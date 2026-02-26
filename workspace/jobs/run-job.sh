#!/bin/bash
# Job Runner
# Usage: run-job.sh <job-name>
# Runs gather phase (if exists), then outputs prompt for LLM phase

set -e

JOB_NAME="$1"
JOBS_DIR="$(dirname "$0")"
JOB_DIR="$JOBS_DIR/$JOB_NAME"

if [[ -z "$JOB_NAME" ]]; then
  echo "Usage: $0 <job-name>"
  exit 1
fi

if [[ ! -d "$JOB_DIR" ]]; then
  echo "Error: Job '$JOB_NAME' not found in $JOBS_DIR"
  exit 1
fi

# Phase 1: Gather (if script exists)
if [[ -x "$JOB_DIR/gather.sh" ]]; then
  bash "$JOB_DIR/gather.sh" >/dev/null 2>&1
fi

# Phase 2: Output prompt for LLM interpretation
if [[ -f "$JOB_DIR/prompt.md" ]]; then
  cat "$JOB_DIR/prompt.md"
else
  echo "Error: No prompt.md found for job '$JOB_NAME'"
  exit 1
fi
