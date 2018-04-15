"""ML Model: Insert one line documentation here.

Insert detailed description here.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def _model_fn(features, labels, mode):
  """Returns a model function to pass to tf.estimator.Estimator."""

  # Insert model description here

  # Refer to the following link for other how to return EstimatorSpec:
  # https://www.tensorflow.org/api_docs/python/tf/estimator/EstimatorSpec
  return tf.estimator.EstimatorSpec(mode)


def build_estimator(run_config):
  return tf.estimator.Estimator(
      model_fn=_model_fn,
      config=run_config)
