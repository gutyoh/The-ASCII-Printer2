import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

# GOPHER = '''|
#
#          ,_---~~~~~----._
#   _,,_,*^____      _____``*g*"*,
#  / __/ /'     ^.  /      \ ^@q   f
# [  @f | @))    |  | @))   l  0 _/
#  \`/   \~____ / __ \_____/    \/
#   |           _l__l_           I
#   }          [______]           I
#   ]            | | |            |
#   ]             ~ ~             |
#   |                            |
#    |                           |
#             GOPHER'''
#
# inputs = [GOPHER]
#
# with open("ascii_art.txt", "w", encoding="utf8") as f:
#     f.write(GOPHER)

inputs = ['''|

         ,_---~~~~~----._
  _,,_,*^____      _____``*g*"*,
 / __/ /'     ^.  /      \ ^@q   f
[  @f | @))    |  | @))   l  0 _/
 \`/   \~____ / __ \_____/    \/
  |           _l__l_           I
  }          [______]           I
  ]            | | |            |
  ]             ~ ~             |
  |                            |
   |                           |
            GOPHER'''
]

inputs = [GOPHER]

with open("ascii_art.txt", "w", encoding="utf8") as f:
    f.write(GOPHER)


FILENAME = "ascii_art.txt"


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in inputs]

    def check(self, reply: str, attach: list):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Cannot find file {FILENAME}")

        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if content != attach[0]:
                raise WrongAnswer(
                    f'Invalid content of {FILENAME} file, got "{content}" want "{attach[0]}"'
                )

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
