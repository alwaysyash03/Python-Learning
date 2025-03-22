# Modules are files with some code that can be imported into other files
# We can import modules using the import keyword
import converters
# We can also import specific module from our modules
from converters import kg_to_lbs

#we can directly call it if we import it
kg_to_lbs(5)

# we can also call it if we import it from the module but we use the module name
print(converters.kg_to_lbs(7.5))