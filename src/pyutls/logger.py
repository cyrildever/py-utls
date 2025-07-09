import logging
import os
import sys
from datetime import datetime, timezone


DEFAULT_NOISY_LOGGERS = [
    "asyncio",
    "boto3",
    "botocore",
    "httpcore",
    "httpx",
    "requests",
    "s3transfer",
]


class CustomLogger:
    """
    CustomLogger provides centralized logging setup with optional suppression
    of noisy third-party loggers and a convenience method for timestamped logging.

    Args:
        noisy_loggers (list[str], optional): List of logger names to suppress (set to ERROR level).
        level (int, optional): The global logging level. Defaults to logging.INFO.
        logger_file (str, optional): File name for saving logs. Defaults to 'logger.log'.
                                     In AWS Lambda environments, it is automatically redirected to '/tmp/'.

    Example:
        >>> logger = CustomLogger(
        ...     noisy_loggers=["boto3", "httpx", "requests"],
        ...     level=logging.INFO
        ... )
        >>> logger.with_time("Application started")
        >>> logger.with_time("An error occurred", lvl=logging.ERROR)

    Notes:
        - Only use `logging.ERROR` level in `except:` blocks.
        - Use `logging.CRITICAL` for custom fatal error conditions.
        - The `flush=True` flag can be used to add spacing between log entries in terminal output.
    """

    def __init__(
        self, noisy_loggers=None, level=logging.INFO, logger_file="logger.log"
    ):
        if os.getenv("AWS_EXECUTION_ENV"):
            logger_file = f"/tmp/{logger_file}"

        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=level,
            handlers=[
                logging.FileHandler(logger_file),
                logging.StreamHandler(sys.stdout),
            ],
        )

        # Use ISO-formatted local time
        logging.Formatter.formatTime = (
            lambda self, record, datefmt=None: datetime.fromtimestamp(
                record.created, timezone.utc
            )
            .astimezone()
            .isoformat(" ")
        )

        # Suppress noisy loggers
        if noisy_loggers is None:
            noisy_loggers = DEFAULT_NOISY_LOGGERS
        self.noisy_loggers = noisy_loggers or []
        for logger_name in self.noisy_loggers:
            logging.getLogger(logger_name).setLevel(logging.ERROR)

    def with_time(self, msg, lvl=logging.INFO, flush=False):
        """
        Log message to both stdout and file.

        Args:
            msg (str): Message to log.
            lvl (int): Logging level (e.g., logging.INFO, logging.ERROR). Defaults to logging.INFO.
            flush (bool): If True, adds a newline before the message for better spacing. Defaults to False.

        Usage:
            >>> logger.with_time("Something happened", lvl=logging.WARNING)
            >>> logger.with_time("New section", flush=True)
        """
        if flush:
            print("", end="\n", flush=True)

        if lvl == logging.ERROR:
            logging.exception(msg)
        elif lvl == logging.CRITICAL:
            logging.critical(msg)
        elif lvl == logging.WARNING:
            logging.warning(msg)
        elif lvl == logging.DEBUG:
            logging.debug(msg)
        else:
            logging.info(msg)
