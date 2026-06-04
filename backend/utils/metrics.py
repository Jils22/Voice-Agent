import time
from dataclasses import dataclass, field

@dataclass
class TurnMetrics:
    turn_id: str
    stt_finalization_ms: int = 0      # time from speech_end to on_final
    retrieval_ms: int = 0             # time for hybrid_retrieve()
    filler_ms: int = 0                # time to first filler audio
    llm_first_token_ms: int = 0       # time to first LLM token
    tts_first_audio_ms: int = 0       # time from on_final to first PCM sent
    total_turn_ms: int = 0            # on_final → tts_end
    interrupted: bool = False
    stale_response: bool = False      # turn_id mismatch caught
    correction_detected: bool = False

def log_turn(m: TurnMetrics):
    print(
        f"[TURN {m.turn_id[:8]}] "
        f"stt={m.stt_finalization_ms}ms | "
        f"retrieval={m.retrieval_ms}ms | "
        f"filler={m.filler_ms}ms | "
        f"llm_first={m.llm_first_token_ms}ms | "
        f"tts_first={m.tts_first_audio_ms}ms | "
        f"total={m.total_turn_ms}ms | "
        f"interrupted={m.interrupted} | "
        f"stale={m.stale_response}"
    )
