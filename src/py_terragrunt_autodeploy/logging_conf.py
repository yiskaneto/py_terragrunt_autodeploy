#!/usr/bin/env python3
import logging, traceback

# logging.basicConfig(level=logging.DEBUG, filename='iac_deployment.log', format='%(asctime)s %(levelname)s:%(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
