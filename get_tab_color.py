import struct

with open('test.bmp', 'rb') as f:
    header = f.read(54)
    pixel_offset = struct.unpack_from('<I', header, 10)[0]
    width = struct.unpack_from('<i', header, 18)[0]
    height = abs(struct.unpack_from('<i', header, 22)[0])
    bpp = struct.unpack_from('<H', header, 28)[0]
    
    bytes_per_pixel = bpp // 8
    row_size = (width * bytes_per_pixel + 3) & ~3
    
    for x_test in [150, 200, 300]:
        for y_test in [30, 50, 70]:
            f.seek(pixel_offset + y_test * row_size + x_test * bytes_per_pixel)
            pixel = f.read(bytes_per_pixel)
            b, g, r = pixel[0], pixel[1], pixel[2]
            print(f"({x_test}, {y_test}): #{r:02x}{g:02x}{b:02x}")
