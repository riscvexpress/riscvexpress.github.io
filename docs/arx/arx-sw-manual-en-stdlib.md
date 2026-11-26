# ARX Software Development Manual: Standard Library Porting

## Simple Replacement of Headers

- Availability of standard libraries

    | stddef.h | stdint.h | stdio.h | stdlib.h |
    | :---: | :---: | :---: | :---: |
    | O | O | X | X |

- Available variables and functions

    | Variable/Function | Original Header | Modified Header |
    | :---: | :---: | :---: |
    | u?intXX_t | stdint.h | - |
    | size_t | stddef.h | - |
    | NULL | stddef.h | - |
    | assert | assert.h | ervp_assert.h |
    | EOF | stdio.h | ervp_fakefile.h |
    | printf | stdio.h | ervp_printf.h |
    | malloc | stdlib.h | ervp_malloc.h |
    | calloc | stdlib.h | ervp_malloc.h |
    | free | stdlib.h | ervp_malloc.h |
    | realloc | stdlib.h | ervp_malloc.h |
    | atoi | stdlib.h | ervp_stdlib.h |
    | atof | stdlib.h | ervp_stdlib.h |
    | exit | stdlib.h | ervp_platform_api.h |

- When replacing header files:

    - You do not need to change how the functions are used in the code.

    - Original functions are redefined using macros and automatically mapped to the provided alternatives.

    - The replacement function names follow the format: `#(original function)_rvx`.

    - Therefore, the original functions must not be included in the compiled ELF file.

## File I/O Porting

### Overview

- Standard file I/O is not supported in ARX. Instead, ARX provides a feature called `fakefile` to simplify porting.

- `Fakefile` is not a general-purpose file I/O mechanism. Instead, it converts input files into header files that can be accessed through the provided functions.

- Because this method relies on compile-time file conversion, only predefined files can be used.

- It is suitable for data sizes under a few megabytes. For larger files, ARX is not appropriate due to limitations in functionality and performance.

- Output files are stored in the SoC’s main memory and can be retrieved to a PC using the ocd program.

- The `fakefile` feature is supported only on hardware implementations such as FPGA prototypes and is not available in RTL simulation.

### Converting Input Files to Headers

```text
cd #(platform dir)
make user
make util
cd #(platform dir)/util
make fakefile
cd #(platform dir)/util/fakefile
mkdir target
```

Copy the input files into the 'target' directory.

```text
make all
```

### Modifying C Code

| Original |  | Modified |  |
| :---: | :---: | :---: | :---: |
| Variable/Function | Header | Variable/Function | Header |
| SEEK_SET | stdio.h | - | ervp_fakefile.h |
| SEEK_CUR | stdio.h | - | ervp_fakefile.h |
| SEEK_END | stdio.h | - | ervp_fakefile.h |
| FILE | stdio.h | FAKEFILE | ervp_fakefile.h |
| fopen | stdio.h | ffopen | ervp_fakefile.h |
| fputc | stdio.h | ffputc | ervp_fakefile.h |
| fgetc | stdio.h | ffgetc | ervp_fakefile.h |
| feof | stdio.h | ffeof | ervp_fakefile.h |
| fclose | stdio.h | ffclose | ervp_fakefile.h |
| fgetline | stdio.h | ffgetline | ervp_fakefile.h |
| fread | stdio.h | ffread | ervp_fakefile.h |
| ftell | stdio.h | fftell | ervp_fakefile.h |
| fseek | stdio.h | ffseek | ervp_fakefile.h |

### Setting Up Compilation Environment

```text
cd #(app dir)
make rvx_each
```

Uncomment 'USE_FAKEFILE=true' in rvx_each.mh

