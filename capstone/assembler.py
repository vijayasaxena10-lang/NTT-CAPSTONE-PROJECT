#!/usr/bin/env python3
"""Two-pass Hack assembler with K=82 feature: line-numbered errors."""
import argparse
import re
from pathlib import Path

COMP = {
    '0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000',
    '!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011',
    'D+1':'0011111','A+1':'0110111','D-1':'0001110','A-1':'0110010',
    'D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101',
    'M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010',
    'D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101',
}
DEST = {'':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
JUMP = {'':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
SYMBOLS = {'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
           **{f'R{i}':i for i in range(16)}}
VALID = re.compile(r'^[A-Za-z_.$:][A-Za-z0-9_.$:]*$')

class AssemblyError(Exception):
    pass

def fail(line, message):
    raise AssemblyError(f'Line {line}: {message}')

def assemble(source):
    symbols = SYMBOLS.copy()
    instructions = []
    for lineno, raw in enumerate(source.splitlines(), 1):
        line = re.sub(r'\s+', '', raw.split('//',1)[0])
        if not line:
            continue
        if line.startswith('('):
            if not line.endswith(')') or not VALID.fullmatch(line[1:-1]):
                fail(lineno, 'invalid label declaration')
            label = line[1:-1]
            if label in symbols:
                fail(lineno, f'duplicate or reserved label: {label}')
            symbols[label] = len(instructions)
        else:
            instructions.append((lineno, line))
    next_ram = 16
    output = []
    for lineno, line in instructions:
        if line.startswith('@'):
            token = line[1:]
            if token.isdecimal():
                number = int(token)
                if number > 32767:
                    fail(lineno, 'A-instruction value must be 0..32767')
            elif VALID.fullmatch(token):
                if token not in symbols:
                    symbols[token] = next_ram
                    next_ram += 1
                number = symbols[token]
            else:
                fail(lineno, f'invalid A-instruction: {line}')
            output.append('0' + format(number,'015b'))
            continue
        if line.count('=') > 1 or line.count(';') > 1:
            fail(lineno, f'invalid C-instruction: {line}')
        before_jump, sep, jump = line.partition(';')
        dest, eq, comp = before_jump.partition('=')
        if not eq:
            comp, dest = dest, ''
        if not comp or comp not in COMP or dest not in DEST or (sep and jump not in JUMP):
            fail(lineno, f'invalid C-instruction: {line}')
        output.append('111'+COMP[comp]+DEST[dest]+JUMP[jump if sep else ''])
    return '\n'.join(output)+'\n'

def main():
    parser=argparse.ArgumentParser(description='Hack assembler; K=82 error reporting')
    parser.add_argument('input', help='Input .asm file')
    parser.add_argument('-o','--output',help='Output .hack file')
    args=parser.parse_args()
    inp=Path(args.input)
    out=Path(args.output) if args.output else inp.with_suffix('.hack')
    try:
        out.write_text(assemble(inp.read_text(encoding='utf-8')), encoding='utf-8')
    except (AssemblyError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')
    print(f'Assembled {inp} -> {out}')

if __name__=='__main__':
    main()
