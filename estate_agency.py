from Pyro5.api import expose, behavior, serve, Daemon
# Test comments
@expose
@behavior(instance_mode="single")
class estate_agency(object):

  def __init__(self):
    self.properties= []
  
  def search_for_property(self, postcode, number):
    for property in self.properties:
      if property['Postcode'] == postcode and property['Number'] == number:
        return True

  def return_properties(self):
    if len(self.properties) > 0:
      return(f"\nThere are a total of {len(self.properties)} properties in the system:\n\n {self.properties}")

    else:
      return(f"\n There are currently no properties listed in the system to display.\n")

  def add_property(self, owner, postcode, number, year):
    id_counter = len(self.properties) +1
    new_property = {"Number":number,
                    "Postcode":postcode, 
                    "ID":id_counter, 
                    "Owner":owner, 
                    "Year":year,
                    "For Sale":"Yes"}
    self.properties.append(new_property)
    return (f"The property {number}, {postcode} has been added to the system with the ID {new_property['ID']}.")

  def select_by_year(self, start_year, end_year):
    properties_in_range = []
    for property in self.properties:
      if property['Year'] >= start_year and property['Year'] <= end_year:
        properties_in_range.append(property)
    
    if len(properties_in_range) > 0:
      return (f"\n No. of properties built within the years {start_year} and {end_year} inclusively: {len(properties_in_range)}\n\n {properties_in_range}")

    else:
          return(f"\n There are no properties in the system that were built within the years {start_year} and {end_year}.\n \n")

  def select_by_postcode(self, postcode):
    properties_in_range = []
    for property in self.properties:
      if property['Postcode'] == postcode:
        properties_in_range.append(property)
    if len(properties_in_range) > 0:
      return(f"\nNo. of properties located within postcode {postcode}: {len(properties_in_range)}\n \n {properties_in_range}")

    else:
      return(f"\n There are no properties in the system with the postcode {postcode}.\n \n")

  def set_for_sale(self, postcode, number):
    if self.search_for_property(postcode, number) == True:
      for property in self.properties:
        if (property['Postcode'] == postcode) and (property['Number'] == number): 
          property['For Sale'] = "Yes"
      return(f"\nThe property at {number}, {postcode} was listed as for sale.\n")

    else:
      return(f"\n The property {number} {postcode} does not exist in the system so its sale status cannot be changed to 'for sale'.\n \n")   

  # # To see a return output in the console, this method needs to be printed.
  def set_not_sale(self, postcode, number):
    if self.search_for_property(postcode, number) == True:
      for property in self.properties:
        if (property['Postcode'] == postcode) and (property['Number'] == number): 
          property['For Sale'] = "No"
      return(f"\nThe property at {number}, {postcode} was listed as sold (no longer for sale).\n")

    else:
      return(f"\n The property {number}, {postcode} does not exist in the system so its sale status cannot be changed to sold.\n \n")   


  def display_properties_sorted(self):
    if len(self.properties) > 0:
      return (f"These are {len(self.properties)} properties in the system, listed in descending order by construction year:\n\n {sorted(self.properties, key=lambda x: x['Year'], reverse=True)}")
 
    else:
      return("\nThere are currently no properties in the system to sort.")
  

if __name__ == "__main__":
  daemon = Daemon()
  serve({estate_agency:"example.estate_agency"}, daemon=daemon, use_ns=True)




