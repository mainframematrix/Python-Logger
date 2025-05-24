
import sys
from datetime import datetime

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Logger:
    def __init__(self, level="DEBUG"):
        self.date_format = "%Y-%m-%d"
        self.time_format = "%H:%M:%S"
        self.loglevel = level.upper()
        self.logs = []

    def set_loglevel(self, level: str):
        """
        Set the default log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
        Only messages at or above this level will be printed.
        """
        level = level.upper()
        if level not in LOG_LEVELS:
            raise ValueError(
                f"Invalid log level '{level}'. Choose from: {', '.join(LOG_LEVELS)}")
        self.loglevel = level

    def select_format(self, style: str):
        """
        Select preset date and time formats.

        style options:
            - "default":  YYYY-MM-DD and 24h time
            - "europe":   DD-MM-YYYY and 24h time
            - "us":       MM/DD/YYYY and 12h time with AM/PM
        """
        style = style.lower()
        if style == "default":
            self.date_format = "%Y-%m-%d"
            self.time_format = "%H:%M:%S"
        elif style == "europe":
            self.date_format = "%d-%m-%Y"
            self.time_format = "%H:%M:%S"
        elif style == "us":
            self.date_format = "%m/%d/%Y"
            self.time_format = "%I:%M:%S %p"
        else:
            raise ValueError("Choose from: 'default', 'europe', or 'us'")

    def _should_log(self, level):
        return LOG_LEVELS.index(level) >= LOG_LEVELS.index(self.loglevel)

    def _log(self, level, message):
        timestamp = datetime.now()  # store datetime object, not formatted string
        self.logs.append((timestamp, level, message))
        if self._should_log(level):
            formatted_time = timestamp.strftime(
                f"{self.date_format} {self.time_format}".strip())
            print(f"{formatted_time} [{level}]: {message}")
            if level == "CRITICAL":
                sys.exit(1)

    def debug(self, message): self._log("DEBUG", message)
    def info(self, message): self._log("INFO", message)
    def warning(self, message): self._log("WARNING", message)
    def error(self, message): self._log("ERROR", message)
    def critical(self, message): self._log("CRITICAL", message)

    def _select_log(self, *levels):
        selected_levels = set(level.upper() for level in levels)
        grouped_logs = {level: [] for level in selected_levels}
        for timestamp, level, message in self.logs:
            if level in selected_levels:
                grouped_logs[level].append((timestamp, message))

        for level in sorted(grouped_logs.keys(), key=lambda l: LOG_LEVELS.index(l)):
            print(f"\n=== {level} LOGS ===")
            for timestamp, message in grouped_logs[level]:
                formatted_time = timestamp.strftime(
                    f"{self.date_format} {self.time_format}".strip())
                print(f"{formatted_time} [{level}]: {message}")
