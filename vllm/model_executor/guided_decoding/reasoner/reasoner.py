# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transformers import PreTrainedTokenizer


@dataclass
class Reasoner(ABC):

    @abstractmethod
    def from_tokenizer(cls, tokenizer: PreTrainedTokenizer) -> Reasoner:
        pass

    @abstractmethod
    def is_reasoning_end(self, input_ids: list[int]) -> bool:
        pass

    @abstractmethod
    def extract_content(self, input_ids: list[int]) -> list[int]:
        pass
