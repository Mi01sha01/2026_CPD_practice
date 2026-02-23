name_of_exhibit = input()
min_rotation = 0
current_index = 1
characters = "0abcdefghijklmnopqrstuvwxyz"

for char in name_of_exhibit:
    forward_index = abs(characters.index(char) - current_index)
    backward_index = 26 - forward_index 
    min_rotation += min(forward_index, backward_index)
    current_index = characters.index(char)

print(min_rotation)
