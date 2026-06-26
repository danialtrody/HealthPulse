import logging
from src.logger import setup_logger


def test_logger_has_correct_name():
    logger = setup_logger("TestLogger")
    assert logger.name == "TestLogger"

def test_logger_has_two_handlers():
    logger = setup_logger("TestLogger2")
    assert len(logger.handlers) == 2

def test_logger_level_is_info():
    logger = setup_logger("TestLogger3")
    assert logger.level == logging.INFO

def test_logger_no_duplicate_handlers():
    logger = setup_logger("TestLogger4")
    setup_logger("TestLogger4")  
    assert len(logger.handlers) == 2 