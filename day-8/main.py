
class Operations:

    @classmethod
    def acc(cls, input_data, registers):
        registers.acc += input_data
        registers.pc += 1

    @classmethod
    def jmp(cls, input_data, registers):
        """
        Change the pc register to a new value by <input_data> amount
        """
        registers.pc += input_data

    @classmethod
    def nop(cls, input_data, registers):
        """
        Well, this literally does.. nothing
        """
        registers.pc +=1


class VM:

    class Registers:
        pc = 0
        acc = 0

    def __init__(self, program):
        self._registers = self.Registers()

        self._program = program
        self._pc_last_index = len(program)-1
        self._seen_pc = set()
        self._termination_state = -1

    def _dump_regs(self):
        return f"Register dump:\n" \
               f"\tPC: {self._registers.pc}\n" \
               f"\tACC: {self._registers.acc}"

    def _panic(self):
        msg = f">> PANIC: Loop in the program detected!!!\n"
        msg += self._dump_regs()
        raise RuntimeError(msg)

    @staticmethod
    def parse_instruction(instruction):
        return instruction[:3], int(instruction[3:].strip())

    def run_program(self):
        while True:
            if self._registers.pc > self._pc_last_index:
                # We're at the end of the program, quit
                break

            if self._registers.pc in self._seen_pc:
                self._panic()

            # Push current PC onto the seen set
            self._seen_pc.add(self._registers.pc)

            # Find the instruction to execute
            instruction, args = self.parse_instruction(
                self._program[self._registers.pc]
            )
            execute = getattr(Operations, instruction, None)

            if execute is None:
                msg = f"Unknown instruction {instruction} at address " \
                      f"{self._registers.pc}."
                raise RuntimeError(msg)

            # Run the instruction
            curr_pc = self._registers.pc
            execute(args, self._registers)

        self._termination_state = 0
        print(">>> Program finished")
        print(self._dump_regs())


def run():
    with open('input.txt', 'r') as f:
        original_program = f.readlines()

    # Run in loop to find the "bug"
    # Better strategy would be to basically just branch the code and register
    # state and run it from there as opposed to always rerunning the program
    # in it's entirety, but I am a little lazy to implement that. Not that it
    # changes complexity directly, but is really a nicer strategy. Leaving for
    # my future non-lazy self.
    for pc, raw_instruction in enumerate(original_program):
        prog_copy = original_program.copy()

        instruction, args = VM.parse_instruction(raw_instruction)
        if instruction == 'acc':
            # No point dealing with acc instruction
            continue

        try:
            vm = VM(prog_copy)
            vm.run_program()
        except RuntimeError:
            # Flip the instruction and try again
            instruction = 'jmp' if instruction == 'nop' else 'nop'
            prog_copy[pc] = f"{instruction} {args}"
            try:
                vm = VM(prog_copy)
                vm.run_program()
            except RuntimeError:
                continue

        break


if __name__ == '__main__':
    run()
