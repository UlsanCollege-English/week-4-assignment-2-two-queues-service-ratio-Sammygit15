import pytest
from src.gate import Gate

# --- Basic functionality ---
def test_ratio_and_skips():
    g = Gate()
    g.arrive("regular","r1")
    g.arrive("regular","r2")
    g.arrive("regular","r3")
    g.arrive("fastpass","f1")
    # Pattern F,R,R,R
    assert g.serve() == "f1"
    assert g.serve() == "r1"
    assert g.serve() == "r2"
    assert g.serve() == "r3"
    with pytest.raises(IndexError):
        g.serve()

def test_peek_next_line():
    g = Gate()
    assert g.peek_next_line() is None
    g.arrive("regular","r1")
    assert g.peek_next_line() == "regular"
    g.arrive("fastpass","f1")
    assert g.peek_next_line() == "fastpass"

# --- Edge Cases ---
def test_edge_serve_when_both_empty():
    g = Gate()
    with pytest.raises(IndexError):
        g.serve()
    assert g.peek_next_line() is None

def test_edge_pattern_wrap_with_sparse_lines():
    g = Gate()
    # Only fastpass riders arrive; pattern should skip empty regular line
    g.arrive("fastpass", "f1")
    g.arrive("fastpass", "f2")
    assert g.peek_next_line() == "fastpass"
    assert g.serve() == "f1"  # consume F slot
    # pattern would point to R, but it's empty; skip to F
    assert g.serve() == "f2"
    with pytest.raises(IndexError):
        g.serve()

# --- Longer scenario with mixed arrivals ---
def test_long_mixed_arrivals_and_service():
    g = Gate()
    # Seed queues
    for i in range(1, 6):
        g.arrive("regular", f"r{i}")  # r1..r5
    g.arrive("fastpass", "f1")
    g.arrive("fastpass", "f2")       # f1..f2

    served = []
    total_people = 7  # 5 regular + 2 fastpass
    for _ in range(total_people):
        served.append(g.serve())

    # Expected F,R,R,R pattern with skips handled
    expected_order = ["f1", "r1", "r2", "r3", "f2", "r4", "r5"]
    assert served == expected_order, f"Served order {served} != expected {expected_order}"

    # After all served, next serve raises IndexError
    with pytest.raises(IndexError):
        g.serve()
