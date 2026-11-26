# ARX Software Development Manual: Caching Region Assignment for Global Variables

## Necessity

- If the software contains many global variables and there is insufficient non-cacheable memory, some variables should be placed in the cacheable region.

- Even when using the CACHING_MOST policy, global variables are not cached by default. To improve performance, they must be explicitly placed in the cacheable region.

- Consistency management is required for these variables.

## How to Specify Allocation

- In C code, global variables can be explicitly assigned to specific data linking sections by using attributes.

    - \#include "ervp_variable_allocation.h"

- NOTCACHED_DATA

    - Forces the variable to be allocated in a non-cacheable memory region.

- CACHED_DATA

    - Forces the variable to be allocated in a cacheable memory region.

    - Data consistency must be maintained manually, regardless of the caching policy.

- BIG_DATA

    - Forces the variable to be allocated in a cacheable memory region.

    - Data consistency must be maintained manually, regardless of the caching policy.

    - The variable is likely to be placed in a large memory region.

- BIG_DATA_BSS

    - Forces the variable to be allocated in a cacheable memory region.

    - Data consistency must be maintained manually, regardless of the caching policy.

    - The variable is likely to be placed in a large memory region.

    - The variable is initialized to zero.
