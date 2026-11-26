# ARX CLI Manual for Linux/Windows: Application

## Overview

In the application directory, users can develop and compile the application software source code. Execution of the application must be performed using either RTL simulation or FPGA prototyping.

## Build Mode

|  | debug | release | profile |
| :---: | :---: | :---: | :---: |
| assert\* | O | X | X |
| assert_must\* | O | O | O |
| printf | O | O | X |
| printf_must | O | O | O |
| debug_print\* | O | O | O |

## Functionality

### Creating an Application Directory

- Command:

    ```text
    cd #(platform dir)/app
    make new APP_NAME=#(app name)
    ```

- Result:  
    `#(platform dir)/app/#(app name)` is created,  
    which we refer to as `#(app dir)`.

### Developing an Application

The application software must be written in C,  
and the source code should be stored in `#(app dir)/src`.  
The location of the source code can be changed by modifying `#(app dir)`.

### Building an Application (Including Compiling)

- Prerequisite: `Synthesizing a Platform`

- Command:

    ```text
    cd #(app dir)
    make rtl
    ```

- Result: `#(app dir)/rtl.release` is created.

- Note: `#(app dir)/rtl.release` is automatically managed by the ARX tool.

### Cleaning Build Results

The following files and/or directories are maintained:  
`./Makefile`, `./compile_list`, and `./src`

```text
cd #(app dir)
make clean
```

## Auxiliary Functionality

### Specifying Compile Options Manually

Specify `CFLAGS_RELEASE`, `CFLAGS_DEBUG`, and/or `CFLAGS_PROFILE`  
in `#(app dir)/rvx_each.mh`, depending on your needs.

### Specifying Compile Sources Manually

Edit `#(app dir)/compile_list`.

### Updating `Makefile` after ARX Update

This is not mandatory unless an error occurs.

```text
cd #(app dir)
make update_makefile
```
