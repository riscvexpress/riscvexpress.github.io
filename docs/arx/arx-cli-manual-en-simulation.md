# ARX CLI Manual for Linux/Windows: RTL Simulation

## Overview

This manual is intended for simulating applications on an RTL-based hardware platform. Applications developed in `#(app dir)` are converted into RISC-V binary files through the build process, and are then loaded into the main memory of the RTL platform at the start of simulation. The simulation automatically terminates when the application's `main` function returns.  
Note that this process requires a license for the mixed-language RTL simulator, which must be obtained separately.

## Simulation Functionality

### Creating an RTL Simulation Directory

- Prerequisite: `Synthesizing a Platform`

- Command:

    ```text
    cd #(platform dir)
    make sim_rtl
    ```

- Result:  
    `#(platform dir)/sim_rtl` is created,  
    which we refer to as `#(sim dir)`.

- Note: `#(sim dir)` is automatically managed by the ARX tool.

### Cleaning All Simulation Results

```text
cd #(sim dir)
make clean
```

### Compiling the Platform RTL Code

```text
cd #(sim dir)
make compile_test
```

### Displaying the Compilation Log of the Platform RTL Code

```text
cd #(sim dir)
make compile_check
```

### Simulating the RTL Platform Using an Application

#### Common

- Prerequisite: `Developing an Application`

- Build Mode:

    - The default value is `debug` for all simulation commands.

    - You can explicitly specify `BUILD_MODE` when invoking `make`.

    - Or, can be defined in `#(sim dir)/rvx_each.mh`.

    - Or, can be defined in `#(platform dir)/user/sim/env/set_sim_env.mh`.

- Note:

    - `Build` compiles only the parts that have changed.

#### Simulating the Platform with an Application

- Included Process:

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).sim
```

#### Simulating the Platform Including an Application Rebuild

- Included Process:

    - `Cleaning Build Results`

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).resim
```

#### Simulating the Platform from Scratch

- Included Process:

    - `Cleaning All Simulation Results`

    - `Cleaning Build Results`

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).all // make clean #(app name).resim
```

#### Simulating with RTL Waveform Recording (with Rebuild)

- Included Process:

    - `Cleaning Build Results`

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).debug
```

#### Simulating with Recording but without Rebuild

- Included Process:

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).debug_hw
```

#### Simulating with RTL Waveform Recording from Boot

- Included Process:

    - `Building an Application`

    - `Compiling the Platform RTL Code`

```text
cd #(sim dir)
make #(app name).debug_init
```

### Opening the Waveform Viewer for Debugging

```text
cd #(sim dir)
make view
```

## Auxiliary Functionality

### Displaying Applications List

```text
cd #(sim dir)
make app_list
```

### Compiling the Platform RTL Code One by One

This command helps identify missing include files.

```text
cd #(sim dir)
make compile_test_all
```

### Identifying RTL Compilation Failures

```text
cd #(sim dir)
make compile_check
```
