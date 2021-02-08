row1 = ["🎁️","🎁️","🎁️"]
row2 = ["🎁️","🎁️","🎁️"]
row3 = ["🎁️","🎁️","🎁️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

pozisyon = input("Hangi koordinatı işaretlemek istersin ? \n> ")
pozisyon_ = pozisyon.split(",")
yatay = int(pozisyon_[0])

dikey = int(pozisyon_[1])

map[dikey - 1][yatay - 1] = "💣"

print(f"{row1}\n{row2}\n{row3}")