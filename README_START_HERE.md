# Nand to Tetris I capstone — K = 82

## Files
- `capstone/CPU.hdl`, `Memory.hdl`, `Computer.hdl`: Part A.
- `capstone/assembler.py`: Part B, two-pass Hack assembler with line-numbered errors.
- `capstone/Box.asm`, `Box.hack`: Part C, screen box program.
- `capstone/invalid_example.asm`: Demonstration of error reporting.
- `REPORT_TEMPLATE.md`: Fill in personal details and attach genuine screenshots.

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
