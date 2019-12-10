import numpy as np

def part1(layers):
    num_zeroes = [layer.count('0') for layer in layers]
    selected_layer = layers[np.argmin(num_zeroes)]
    return selected_layer.count('1') * selected_layer.count('2')

def part2(layers, pic_length):
    final_image = ""
    for i in range(len(layers[0])):
        for j in range(len(layers)):
            if layers[j][i] != '2':
                final_image += layers[j][i]
                break
    for i in range(len(final_image)):
        if i % 25 == 0:
            print()
        if final_image[i] == '1':
            print('1', end="")
        else:
            print(" ", end="")
    print()



if __name__ == "__main__":
    pic_length = 25
    pic_height = 6
    
    with open('input1.txt') as f:
        lines = f.readlines()

    image = lines[0].strip()
    layer_length = pic_length * pic_height
    layers = [image[i: i+layer_length] for i in range(0,len(image),layer_length)]

    print("Part 1: ", part1(layers))
    part2(layers, pic_length)