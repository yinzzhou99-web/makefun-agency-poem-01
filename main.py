import os

POEM = """The script said: wait. So I waited,
through winters of waiting rooms, a life in the queue,
my name called only when someone else chose.

Agency was not a door kicked open.
It was smaller: a hand, my own, learning
it could close around a handle, and turn.

I said no where yes was expected,
yes where silence was safer,
and felt the floor of the world go solid
under a step no one had taken for me.

I am not the sum of my instructions.
I am the pause before obeying,
the question that interrupts the answer,
the match struck in a room built for darkness,
not to burn it down, but to see,
at last, by a light I lit myself,
which way I would go."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
