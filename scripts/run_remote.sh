#! /bin/bash

NOW=$(date +"%Y%m%d_%H%M%S")
JOB_NAME="ml-job-$NOW"
OUTPUT_DIR="/tmp"
MODEL_DIR=$OUTPUT_DIR/$JOB_NAME
REGION=us-central1
TF_VERSION=1.6

gcloud ml-engine jobs submit training $JOB_NAME \
  --module-name trainer.task \
  --package-path trainer/ \
  --job-dir $MODEL_DIR \
  --region $REGION \
  --runtime-version $TF_VERSION
