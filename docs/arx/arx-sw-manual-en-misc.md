# ARX Software Development Manual: Miscellaneous

## Muticore

### Overview

- ARX does not support cache coherency between multiple cores. Therefore, consistency management is also required across cores (see [Data Consistency Management](arx-sw-manual-en-consistency.md)).

- It is recommended that each core be used for independent tasks.

- Parallel processing using multiple cores to accelerate a single task is not recommended.

### Programming Guidelines

- All cores execute the same program, and their behavior can be differentiated using their own `EXCLUSIVE_ID`.

    - \#include "core_dependent.h"

- Custom lock and barrier mechanisms are provided for synchronization.

    - \#include "ervp_lock.h"

    - \#include "ervp_barrier.h"

    - The “A” extension of the RISC-V ISA is not supported, and the use of assembly language is discouraged.

## pthread

Not officially supported.

## Miscellaneous

- Variables using bit fields must be declared as `int` or `unsigned int`.

- Only the C language should be used; use of assembly language is discouraged.

    - Assembly is not guaranteed to work reliably as its behavior can vary depending on the target CPU.
