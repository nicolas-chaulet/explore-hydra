import logging
import sys

import hydra

log = logging.getLogger(__name__)


@hydra.main(config_path="config/config.yaml")
def my_app(_cfg) -> None:
    print(_cfg.pretty())


if __name__ == "__main__":
    sys.exit(my_app())