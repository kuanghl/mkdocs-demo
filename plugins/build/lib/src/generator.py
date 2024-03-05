import logging
import os

class Generator(object):
    
    def test_log(self, val):
        os.chdir("./")
        logging.basicConfig(filename='mkdocs-pdf.log', level=logging.DEBUG) 
        self.val = val
        logging.error('error {} !', self.val)
        logging.warning('waning {} !', self.val)
        logging.info('info {} !', self.val)
        logging.debug('debug {} !', self.val)
        logging.critical('critical {} !', self.val)

