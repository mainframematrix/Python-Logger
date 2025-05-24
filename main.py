
from pyLog import Logger  # assuming your Logger instance is imported like this


def run_tests():

    Logger.select_format("us")  # Set US datetime format
    Logger.warning("Memory usage is high.")

    Logger.set_loglevel("INFO")# set_loglevel will work from where it is placed it will not affect the previous logs
    
    Logger.debug("This is a debug message.")

    Logger.info("System started successfully.")
    Logger.warning("Memory usage is high.")

    Logger.select_format("europe")  # Set European datetime format
    Logger.error("File not found.")
    Logger.error("Failed to connect to the database.")
   # Logger.critical("System crash! Immediate action required.")

    print("\nSelected logs:")
    # Assuming this method filters logs by level
    Logger._select_log("INFO", "WARNING", "error")


if __name__ == "__main__":
    run_tests()
