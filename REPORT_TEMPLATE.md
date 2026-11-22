# Nand to Tetris I — Capstone Project Report
## Make the Computer Draw a Box

**Name:** [VIJAYA SAXENA]  
**Roll number:** [2501010182]  
**Personal number K:** 82  
**Course:** Nand to Tetris – I (ETCCNT301)

## 1. Objective and personalized requirements
The aim is to integrate the Hack computer using HDL, build a two-pass assembler in Python, and write a keyboard-controlled screen drawing program in Hack assembly. My personal number is K=82. The box starts at row 82, is 20 rows tall, and has a width of 16*((82 mod 4)+1) = 48 pixels. Because 82 mod 3 = 1, the assembler includes clear error messages with source line numbers.

## 2. Part A — Computer construction
The CPU combines an A register, D register, ALU and program counter to execute Hack instructions. Memory maps RAM16K, Screen and Keyboard to the Hack address space. Computer connects ROM32K, CPU and Memory. The HDL source files are CPU.hdl, Memory.hdl and Computer.hdl.

**Test evidence (insert your actual screenshots and record actual status):**
- CPU.tst: [PASS / FAIL / NOT RUN] — [screenshot]
- Memory.tst: [PASS / FAIL / NOT RUN] — [screenshot]
- ComputerAdd.tst: [PASS / FAIL / NOT RUN] — [screenshot]
- ComputerMax.tst: [PASS / FAIL / NOT RUN] — [screenshot]
- ComputerRect.tst: [PASS / FAIL / NOT RUN] — [screenshot]

**Built-in chips used, if any:** [List actual substitutions, or 'None' if none]

## 3. Part B — Python assembler
The first pass removes comments and blank lines and records labels with their ROM instruction addresses. The second pass converts A-instructions and C-instructions into 16-bit binary. Variables are allocated starting at RAM address 16. The assembler uses translation tables for computation, destination and jump fields. My K-specific extension reports invalid instructions with their original source line number, for example `Line 7: invalid C-instruction: THIS_IS_NOT_A_HACK_INSTRUCTION`.

**Official assembler comparison (record actual results):**
- Add.asm: [MATCH / MISMATCH / NOT TESTED]
- Max.asm: [MATCH / MISMATCH / NOT TESTED]
- Rect.asm: [MATCH / MISMATCH / NOT TESTED]
- Pong.asm: [MATCH / MISMATCH / NOT TESTED]

[Insert assembler run screenshot and error demonstration screenshot]

## 4. Part C — Keyboard-controlled box
Box.asm reads KBD. When a key is pressed, the color is -1 (all 16 pixels in a screen word are black); when released, the color is 0 (white). The program starts at address SCREEN + 32*82 = 19008. Each row writes 3 words, representing 48 pixels, and skips 29 words to reach the next row. The outer loop processes 20 rows and repeats the keyboard check continuously. The provided Python assembler generates Box.hack from Box.asm.

**CPU Emulator screenshot showing the black box:** [Insert actual screenshot]

## 5. One mistake fixed
[Replace this placeholder with ONE genuine mistake you personally observed and fixed while testing. Explain the symptom, what you changed, and how you verified the fix. Do not invent a debugging experience.]

## 6. Conclusion
The project demonstrates the connection between Hack hardware, binary instruction encoding and memory-mapped screen/keyboard I/O. [Add your actual test outcomes here.]
