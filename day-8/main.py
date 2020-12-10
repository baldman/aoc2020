
class Operations:

    @classmethod
    def acc(cls, input_data, registers):
        registers.acc += input_data

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
        ...


class VM:

    class Registers:
        pc = 0
        acc = 0

    def __init__(self, program):
        self._registers = self.Registers()

        self._program = program
        self._pc_last_index = len(program)-1
        self._seen_pc = set()

    @staticmethod
    def _parse_instruction(instruction):
        return instruction[:3], int(instruction[3:].strip())

    def run_program(self):
        while True:
            if self._registers.pc > self._pc_last_index:
                # We're at the end of the program, quit
                break

            if self._registers.pc in self._seen_pc:
                msg = f">> PANIC: Loop in the program detected!!!\n " \
                      f"Register dump:\n" \
                      f"\tPC: {self._registers.pc}\n" \
                      f"\tACC: {self._registers.acc}"
                raise RuntimeError(msg)

            # Push current PC onto the seen set
            self._seen_pc.add(self._registers.pc)

            # Find the instruction to execute
            instruction, args = self._parse_instruction(self._program[self._registers.pc])
            execute = getattr(Operations, instruction, None)

            if execute is None:
                raise RuntimeError(f"Unknown instruction {instruction} at address {self._registers.pc}.")

            print(f">>> DEBUG: {instruction} {args} at address {self._registers.pc}")
            # Run the instruction
            curr_pc = self._registers.pc
            execute(args, self._registers)

            # Advance the program counter register if it was not modified
            if self._registers.pc == curr_pc:
                self._registers.pc += 1

        print(">>> Program finished")


def run():
    vm = None
    with open('input.txt', 'r') as f:
        vm = VM(f.readlines())

    vm.run_program()


if __name__ == '__main__':
    run()
