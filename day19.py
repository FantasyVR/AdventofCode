# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:29:04 2018

@author: RV
"""
from collections import defaultdict
opType = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
          'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']


def compute(registers,instruction):
    register = [x for x in registers]
    # operation sourceData1 sourceData2, destination
    opT = instruction[0]
    [s1, s2, d] = list(map(int,instruction[1:]))

    if opT == 'addr':
        register[d] = register[s1] + register[s2]
    elif opT == 'addi':
        register[d] = register[s1] + s2
    elif opT == 'mulr':
        register[d] = register[s1] * register[s2]
    elif opT == 'muli':
        register[d] = register[s1] * s2
    elif opT == 'banr':
        register[d] = register[s1] & register[s2]
    elif opT == 'bani':
        register[d] = register[s1] & s2
    elif opT == 'borr':
        register[d] = register[s1] | register[s2]
    elif opT == 'bori':
        register[d] = register[s1] | s2
    elif opT == 'setr':
        register[d] = register[s1]
    elif opT == 'seti':
        register[d] = s1
    elif opT == 'gtir':
        register[d] = 1 if s1 > register[s2] else 0
    elif opT == 'gtri':
        register[d] = 1 if register[s1] > s2 else 0
    elif opT == 'gtrr':
        register[d] = 1 if register[s1] > register[s2] else 0
    elif opT == 'eqir':
        register[d] = 1 if s1 == register[s2] else 0
    elif opT == 'eqri':
        register[d] = 1 if register[s1] == s2 else 0
    elif opT == 'eqrr':
        register[d] = 1 if register[s1] == register[s2] else 0
    return register


def main():
    lines = open("day19.txt").read().split('\n')
    boundReg = int(lines[0].split(' ')[1])
    program = defaultdict(str)
    for i in range(1, len(lines)):
        program[i - 1] = lines[i]
    programlen = len(program)

    registers = [0] * 6
	# part 2 :set register[0] = 1 然后得到大数
	# 之后获取sum(factors of big number)
    # registers[0]  = 1
    ip = registers[boundReg]
    while ip < programlen:
        registers[boundReg] = ip
        instr = program[ip].split(' ')  # 从IP地址取出指令
        print("ip = %2d" % ip, registers, program[ip], end=' ')  # IP 地址， 寄存器内容， 程序中的指令
        registers = compute(registers, instr)  # 执行指令，并返回寄存器的内容
        print(registers)
        ip = registers[boundReg]  # IP 地址加 1
        ip += 1  # 把IP地址放进 绑定的寄存器中

if __name__ == "__main__":
    main()