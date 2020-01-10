import logging
import re

from bs4 import BeautifulSoup
from ..const import EMAIL_ATTR_FROM, EMAIL_ATTR_BODY


_LOGGER = logging.getLogger(__name__)
EMAIL_DOMAIN_AMAZONFR = 'amazon.fr'
ATTR_AMAZONFR = 'amazonfr'


def parse_amazonfr(email):
    """Parse Amazon FR tracking numbers."""
    tracking_numbers = []

    matches = re.findall(r'ie=(.*?)=&addressID=(.*?)&latestArrivalDate=(.*?)&orderID=(.*?)&shipmentDate=(.*?)&orderingShipmentId=(.*?)&packageId=(.*?)', email[EMAIL_ATTR_BODY])
    for tracking_number in matches:
        if tracking_number not in tracking_numbers:
            tracking_numbers.append(tracking_number)
                
    return tracking_numbers
    
