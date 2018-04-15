"""Run model training and evaluation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import tensorflow as tf

from trainer import model


def _parse_arguments(argv):
  parser = argparse.ArgumentParser(description='TODO')
  parser.add_argument(
      '--job-dir',
      help='Output path for ML training job.')
  parser.add_argument(
      '--hparams',
      help='Model training hyperparameters as comma-separated "key=value" pairs.')

   # Insert other arguments here

  return parser.parse_args(argv)


def run_experiment(hparams):
  # Setup ML experiment here

  run_config = tf.estimator.RunConfig()
  run_config = run_config.replace(model_dir=hparams.job_dir)
  estimator = model.build_estimator(run_config)

  # Do training and evaluation here


def main(argv):
  flags = _parse_arguments(argv[1:])
  tf.logging.set_verbosity(tf.logging.INFO)

  # Do stuff with flags

  hparams = tf.contrib.training.HParams(**flags.__dict__)
  hparams.parse(flags.hparams)
  run_experiment(hparams)


if __name__ == '__main__':
  tf.app.run(main)
