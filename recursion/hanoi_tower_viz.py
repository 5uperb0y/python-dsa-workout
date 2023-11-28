"""
Implement a solution to the Tower of Hanoi and keep track of the disks.
This Tower of Hanoi algorithm is enhanced by incorporating a dictionary to track disk positions across poles,
and modifying the disk movement functions to update this dictionary, thereby maintaining the game's state
throughout the recursive solution process.
"""
def show_piles(piles):
	for k, p in piles.items():
		print(f"{k}| {p}")
	print("-----")
def move_disk(source, target, piles):
	disk = piles[source].pop()
	piles[target].append(disk)
	print(f"move disk {disk} from {source} to {target}")
def move_tower(height, source, temp, target, piles):
	if height > 0:
		move_tower(height - 1, source, target, temp, piles)
		move_disk(source, target, piles)
		show_piles(piles)
		move_tower(height - 1, temp, source, target, piles)
	else:
		pass
def main(height):
	p = {
		"a": list(range(height, 0, -1)),
		"b": [],
		"c": []
		}
	print("Initial Piles:")
	show_piles(p)
	move_tower(height, "a", "b", "c", p)
main(3)
