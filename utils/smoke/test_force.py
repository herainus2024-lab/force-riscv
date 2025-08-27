#
# Copyright (C) [2020] Futurewei Technologies, Inc.
#
# FORCE-RISCV is licensed under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES
# OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence


class MainSequence(Sequence):
    def generate(self, **kargs):
        i_rec_id1 = self.genInstruction("ADD##RISCV")
        i_rec_id2 = self.genInstruction("SRA##RISCV")
        record1 = self.queryInstructionRecord(i_rec_id1)
        record2 = self.queryInstructionRecord(i_rec_id2)

        self.notice("record1内容: {}".format(record1))
        self.notice("record2内容: {}".format(record2))
        self.verifyInstruction("ADD##RISCV", record1)
        self.verifyInstruction("SRA##RISCV", record2)


#  Points to the MainSequence defined in this file
MainSequenceClass = MainSequence

#  Using GenThreadRISCV by default, can be overriden with extended classes
GenThreadClass = GenThreadRISCV

#  Using EnvRISCV by default, can be overriden with extended classes
EnvClass = EnvRISCV
