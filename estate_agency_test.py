import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file estate_agency.py exists.
import os.path
if(os.path.isfile("estate_agency.py")==False):
	print("Error you need to call the Python file estate_agency.py!")

# Check that the class is called estate_agency. That is, the file estate_agency.py contains the expression "estate_agency(object):"
file_text = open('estate_agency.py', 'r').read()
if("estate_agency(object):" not in file_text):
	print("Error you need to call the Python class estate_agency!")

sys.excepthook = Pyro5.errors.excepthook
estate_agency = Proxy("PYRONAME:example.estate_agency")

print(estate_agency.return_properties())
print(estate_agency.add_property("James Joyce", "CF24 3AA", 12, 1991))
print(estate_agency.select_by_year(2000, 2010))
print(estate_agency.select_by_postcode("CF24 3AA"))
estate_agency.set_for_sale("CF24 3AA", 12)
print(estate_agency.set_not_sale("CF24 3AA", 12))
print(estate_agency.display_properties_sorted()) 




