from sensor.logger  import logging
from sensor.exception import SensorException
import sys

try:
    logging.info("zero division is not acceptabe")
    a=10
    a/0
except Exception as e:
    raise SensorException(e,sys)