"""ML Model: Insert one line documentation here.

Insert detailed description here.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def get_model_fn(hparams):
  """Returns a model_fn constructed from hyperparameters, if any."""

  def model_fn(features, labels, mode):
    """Model function to pass to tf.estimator.Estimator."""

    # Insert model description here

    # Refer to the following link for other how to return EstimatorSpec:
    # https://www.tensorflow.org/api_docs/python/tf/estimator/EstimatorSpec
    return tf.estimator.EstimatorSpec(mode)

  return model_fn


def build_estimator(run_config, hparams):
  return tf.estimator.Estimator(
      model_fn=get_model_fn(hparams),
      config=run_config)
