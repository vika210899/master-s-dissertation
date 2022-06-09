#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


class Constants:
    # Params
    COUNT_OF_MOST_COMMON_WORDS = 10
    COUNT_OF_TRAINING_REPEAT = 10000
    RANDOM_SEED = 17  # Just a number for start Random
    CATEGORY_BORDER_LINE_COUNT = 2

    # Filenames
    LEARN_FILE_NAME = 'popisyat.xls'
    TEST_FILE_NAME = 'popisyat.xls'
    STOPLIST_FILE_NAME = 'SmartStoplist.txt'
    # Position triggers
    START_POSITION_WORKSHEET = 0
    DATA_COLUMN_WORKSHEET = 0
    RESULT_COLUMN_WORKSHEET = 3

    EXCEL_RANGE = 150  # RANGE FOR LEARNER FILE
    TEST_EXCEL_RANGE = 150  # RANGE FOR MASSTEST FILE

    @staticmethod
    def getTestFileName():
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        return ("masstest_result_" + dt_string + ".xls")

    # Triggers for Testing
    IS_CHECK_TIME_TEST_MODE = True  # or write False here
    IS_WRITE_TO_CONSOLE = False
    IS_VKLUCHIT_BRAIN_COUNTER = False
    IS_BORDERLINE_TESTIN_FOR_SINGLE_REQUEST = True

    CONSOLE_WRITER_FILE_NAME = "console_output_" + \
        str(COUNT_OF_TRAINING_REPEAT) + "_" + \
        str(COUNT_OF_MOST_COMMON_WORDS) + "_" + str(EXCEL_RANGE) + ".txt"
    SAVE_FILE = "trainready_" + str(COUNT_OF_TRAINING_REPEAT) + "_" + str(
        COUNT_OF_MOST_COMMON_WORDS) + "_" + str(EXCEL_RANGE) + ".antondahann"
