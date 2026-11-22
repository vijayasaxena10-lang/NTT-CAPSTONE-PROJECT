# Hack Computer Architecture

**Nand to Tetris – I | ETCCNT301**

A capstone project implementing the Hack computer architecture using Hardware Description Language (HDL), Hack Assembly Language, and Python.

---

## Overview

This repository contains the capstone project **"Make the Computer Draw a Box"**, developed as part of the Nand to Tetris – I course at K.R. Mangalam University.

The project demonstrates the working of a computer system through three main components:

1. **Hardware Implementation:** Building the Hack CPU, Memory, and Computer using HDL.
2. **Assembler Development:** Developing a two-pass assembler in Python to convert Hack assembly instructions into binary machine code.
3. **Assembly Programming:** Creating a keyboard-controlled black rectangle on the Hack computer screen.

## Student Details

| Field | Details |
|---|---|
| Name | Vijaya Saxena |
| Roll Number | 25010182 |
| Personal Number (K) | 82 |
| Course | Nand to Tetris – I |
| Course Code | ETCCNT301 |
| University | K.R. Mangalam University |
| School | School of Engineering & Technology |

---

## Personalized Project Specifications

The rectangle dimensions and assembler feature are calculated using the personal number **K = 82**.

| Calculation | Result |
|---|---|
| K | 82 |
| K mod 3 | 1 |
| K mod 4 | 2 |
| Rectangle Width | 48 pixels |
| Rectangle Height | 20 rows |
| Starting Row | 82 |
| Ending Row | 101 |
| Starting Screen Address | 19008 |
| Assembler Extra Feature | Line-numbered error messages |

### Rectangle Width Calculation

Width = 16 × ((K mod 4) + 1)

Width = 16 × (2 + 1)

**Width = 48 pixels**

### Starting Screen Address

Screen Address = 16384 + (32 × K)

= 16384 + (32 × 82)

**Starting Address = 19008**

The rectangle occupies 3 consecutive 16-bit words per row and extends across 20 rows.

---

## Part A: Hack Computer Hardware Implementation

The hardware implementation consists of three main HDL components.

### 1. CPU.hdl
Implements the central processing unit responsible for executing Hack machine instructions, performing ALU operations, and controlling program execution.

### 2. Memory.hdl
Implements the memory system, integrating RAM, screen memory, and keyboard input.

### 3. Computer.hdl
Connects the CPU, Memory, and ROM32K to form the complete Hack computer architecture.

### Official Test Files

The following test scripts are used to verify the hardware implementation:

- CPU.tst
- Memory.tst
- ComputerAdd.tst
- ComputerMax.tst
- ComputerRect.tst

---

## Part B: Python-Based Hack Assembler

A two-pass assembler is implemented using Python.

The assembler converts Hack assembly language (`.asm`) into 16-bit binary machine code (`.hack`).

### First Pass
- Removes comments and empty lines.
- Identifies labels.
- Stores label addresses in the symbol table.

### Second Pass
- Converts A-instructions into binary.
- Converts C-instructions into binary.
- Resolves predefined symbols and labels.
- Allocates new variables beginning at RAM address 16.
- Generates the `.hack` output file.

### Personalized Extra Feature

Since **82 mod 3 = 1**, the assembler includes line-numbered error handling.

Example:

```text
Error: Line 7: invalid C-instruction: THIS_IS_NOT_A_HACK_INSTRUCTION
```

This helps identify invalid assembly instructions without displaying an unhandled Python exception.

### Run the Assembler

From the project root:

```bash
python capstone/assembler.py capstone/Box.asm
```

Expected output:

```text
Assembled capstone\Box.asm -> capstone\Box.hack
```

---

## Part C: Keyboard-Controlled Rectangle

The assembly program `Box.asm` displays a black rectangle on the Hack computer screen.

### Working Principle

1. The program continuously checks the keyboard memory address.
2. When a key is pressed, the rectangle is drawn.
3. When the key is released, the rectangle is cleared.
4. The program repeats the process using a continuous loop.

### Rectangle Specifications

- Starting Row: 82
- Height: 20 rows
- Width: 48 pixels
- Starting Address: 19008
- Position: Left edge of the screen

The program is assembled into `Box.hack` using the Python assembler and can be executed in the Nand2Tetris CPU Emulator.

---

## Project Structure

```text
NTT_Capstone_K82/
│
├── capstone/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   ├── Computer.hdl
│   ├── assembler.py
│   ├── Box.asm
│   ├── Box.hack
│   └── invalid_example.asm
│
├── README.md
└── REPORT_TEMPLATE.md
```

*The structure above shows the main project files. Additional test files and supporting documents may be included.*

---

## Technologies Used

| Technology | Purpose |
|---|---|
| HDL | Hardware chip implementation |
| Python | Two-pass assembler development |
| Hack Assembly | Keyboard-controlled rectangle program |
| Nand2Tetris Hardware Simulator | Testing HDL components |
| Nand2Tetris CPU Emulator | Running machine code |
| Visual Studio Code | Code development |
| Git and GitHub | Version control and project submission |

---

## Testing and Verification

### Assembler Verification

The Python assembler was executed successfully to generate `Box.hack`.

The personalized error-handling feature was also tested using an invalid instruction, producing a clear line-numbered error message.

### Hardware Verification

The project includes HDL implementations intended to be tested using the official Nand2Tetris test scripts.

### Rectangle Verification

The `Box.hack` program can be loaded into the CPU Emulator to check the rectangle's appearance and keyboard interaction.

**Verification Note:** Official HDL test results and the final rectangle output require successful simulator execution before they can be reported as passed.

---

## Learning Outcomes

Through this capstone project, the following concepts were explored:

- Understanding the internal architecture of a computer.
- Connecting hardware components using HDL.
- Understanding CPU, memory, and instruction execution.
- Converting assembly instructions into binary machine code.
- Implementing symbol tables and error handling in Python.
- Understanding memory-mapped screen and keyboard input.
- Using GitHub for source-code management.

---

## Conclusion

The Nand to Tetris capstone project demonstrates how hardware and software work together in a computer system.

The project combines HDL-based computer architecture, Python assembler development, and Hack assembly programming to demonstrate instruction execution and memory-mapped input/output.

It provides practical experience with the fundamental concepts of computer organization and low-level programming.

---

## References

- [Official Nand2Tetris Website](https://www.nand2tetris.org/)
- [Nand2Tetris Web IDE](https://nand2tetris.github.io/web-ide/)
- [Official Nand2Tetris Project Files](https://github.com/nand2tetris/projects)

---

**Submitted By:** Vijaya Saxena  
**Roll Number:** 25010182  
**Course:** Nand to Tetris – I (ETCCNT301)  
**University:** K.R. Mangalam University  
**School of Engineering & Technology**
