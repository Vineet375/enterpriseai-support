# eval.py - simple evaluator (simulated scoring)
def judge_answer(reference: str, candidate: str) -> int:
    # naive scoring: percent of shared words
    ref_tokens = set(reference.lower().split())
    cand_tokens = set(candidate.lower().split())
    if not ref_tokens:
        return 0
    score = int(100 * len(ref_tokens & cand_tokens) / len(ref_tokens))
    # scale to 0-10
    return max(0,min(10, score//10))
