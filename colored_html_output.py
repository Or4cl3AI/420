import coloredlogs
import logging

def generate_colored_html_output():
    # Set up logging
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)

    # Generate colored HTML output
    logger.debug('Generating colored HTML output...')
    # Your code for generating colored HTML output goes here

    logger.debug('Colored HTML output generated successfully.')

if __name__ == '__main__':
    generate_colored_html_output()