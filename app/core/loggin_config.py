import logging
import os

def setup_basic_logging():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(log_dir, "bot.log"), mode="w"),
            logging.StreamHandler()
        ]
    )
    
    logging.info("Logging inicializado en app/core/logs/")