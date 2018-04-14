import argparse
import sys

import log_util

logger = log_util.get_logger(__name__)


def _parse_arguments(argv):
    parser = argparse.ArgumentParser(description='TODO')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode.')

    # Insert arguments here

    return parser.parse_args(argv)


def main(argv):
    flags = _parse_arguments(argv)
    if flags.debug:
        log_util.set_log_level(logger, 'DEBUG')

    logger.debug('TODO')


if __name__ == '__main__':
    main(sys.argv[1:])


