# Nand to Tetris I capstone — K = 82

## Files
- `capstone/CPU.hdl`, `Memory.hdl`, `Computer.hdl`: Part A.
- `capstone/assembler.py`: Part B, two-pass Hack assembler with line-numbered errors.
- `capstone/Box.asm`, `Box.hack`: Part C, screen box program.
- `capstone/invalid_example.asm`: Demonstration of error reporting.
- `REPORT_TEMPLATE.md`: Fill in personal details and attach genuine screenshots.

## Fastest submission procedure
1. Open the official Nand2Tetris Hardware Simulator. Load `capstone/CPU.hdl` and run the official `CPU.tst` (from project 05). Repeat with `Memory.hdl`/`Memory.tst` and `Computer.hdl`/`ComputerAdd.tst`, `ComputerMax.tst`, `ComputerRect.tst`. **Keep official `.tst`, `.cmp`, `.asm`, and `.hack` files in their original project directory** if the tests expect them there. Copy the three HDL files into that project directory when running the tests. Capture real result screenshots.
2. In a terminal, run `python capstone/assembler.py capstone/Box.asm`. This produces `Box.hack`. Run `python capstone/assembler.py capstone/invalid_example.asm` to demonstrate the line-7 error.
3. To test assembler correctness, run it on the official `Add.asm`, `Max.asm`, `Rect.asm`, `Pong.asm`, then compare each `.hack` output with the official assembler's outputs. The official examples are not included in this ZIP.
4. Open the CPU Emulator, load `capstone/Box.hack`, choose `No animation` or fast execution, and run. In the keyboard control, press/hold any key. A 48 x 20 black box should appear starting at screen row 82, x=0; release the key and it should disappear. Capture a genuine screenshot. Depending on the emulator keyboard control, focus may need to be on its keyboard widget.
5. Put the `capstone` folder inside your EXISTING NTT lab Git repository, commit and push. See commands below.
6. Complete `REPORT_TEMPLATE.md` with your name, roll number, test results and screenshots, then export as PDF for ZOSIMA.

## Git commands (run from your existing lab repo root after copying capstone folder there)
```
git add capstone
git commit -m "Add NTT capstone K82 computer assembler and box"
git push
```

## K-specific calculations
K=82; 82 % 3 = 1 => line-numbered assembler errors. 82 % 4 = 2 => width=16*(2+1)=48 pixels (3 screen words). Height=20 rows, rows 82 through 101 inclusive. First screen address=16384 + 32*82 = 19008. Last written screen word is 19008 + 32*19 + 2 = 19618.

## Important
The code was generated and the Python assembler was run to create Box.hack. Official hardware simulator tests, official assembler comparisons, and CPU Emulator output have **not** been run here. Do not claim passing tests without running them. The assignment allows using built-in older chips if needed; disclose that in your report.
