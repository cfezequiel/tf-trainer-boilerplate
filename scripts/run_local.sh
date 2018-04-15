#! /bin/bash

NOW=$(date +"%Y%m%d_%H%M%S")
JOB_NAME="ml-job-$NOW"
OUTPUT_DIR="/tmp"
MODEL_DIR=$OUTPUT_DIR/$JOB_NAME

gcloud ml-engine local train \
  --module-name trainer.task \
  --package-path trainer/ \
  --job-dir $MODEL_DIR
