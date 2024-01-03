import argparse
import logging

from python_project_example.parsers.basic import parse_str

datefmt="%Y-%m-%d %I:%M:%S"
log_format = "%(asctime)s:%(levelname)s:%(message)s"
logging.basicConfig(format=log_format, datefmt=datefmt, level=logging.INFO)
LOG=logging.getLogger(__name__)


def main():
    
    LOG.info("Starting application")    
    parser = argparse.ArgumentParser(description="Splits sentence into a list of words")
    parser.add_argument("string")
    parser.add_argument("-l", "--lower", action="store_true", help="convert string to lower case")
    args = parser.parse_args()
    
    val = parse_str(args.string, lower_case=args.lower)
    LOG.info(f"Result {val}")
    LOG.info("Done.")
    
if __name__ == '__main__':
    main()