import logging
import logging.handlers


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="[{asctime}] [{levelname:<8}] {name}: {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.handlers.RotatingFileHandler(
                filename="api/logs/kawaii.log",
                encoding="utf-8",
                maxBytes=32 * 1024 * 1024,
                backupCount=5,
            ),
            logging.StreamHandler(),
        ],
    )
