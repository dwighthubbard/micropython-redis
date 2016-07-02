# Usage

The micropython-redis module provides 3 different redis client interfaces.  
Each of which has different benefits and tradeoffs.

In the following section, the resource estimates are based on usage
using the micropython unix port.  The numbers will be different on
other platforms, although the relative amounts used will remain
roughly the same.

## The uredis.Redis()/uredis.StrictRedis() classes.
This class is mostly compatible with the redis-py 
redis.Redis()/redis.StrictRedis() classes.  Which allows a lot of 
existing code to work with little or no modifications.

The tradeoff is this requires the most resources.  Currently
importing this module uses currently ~20kb of memory.

## The uredis_modular.* classes
The uredis_modular python module contains python modules that
each implement a subset of the redis server functionality.  Each
of these modules can be used individully or they can be combined
as mixins to create a Redis class with the desired functionality.
The more functionality used, the more resources the resulting class
will use.

All of these modules share a common redis.client which currently
uses about ~6.5kb.  Then each functionality module increases the
resource usage by 1kb to 6kb depending on the compexity of 
the functinality submodule.

For example using the uredis_modular.list.List() submodule provides
all of the redis server List functionality but uses 10kb to import.

## Low level access using the uredis_modular.client.Client() class
The uredis.modular.client.Client() implements the redis protocol
and can be used to communicate to the redis server direcctly without
pulling in any of the funtionality submodules. 
This method uses the least resources, requiring ~6.5kb to import.

This method is not compatible with the redis-py bindings in any way.  
Also all communications will need to be encoded/decode to from byte
strings prior to sending.
