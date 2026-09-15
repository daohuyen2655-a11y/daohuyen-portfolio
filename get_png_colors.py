import zlib
import struct

def parse_png(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    idat_chunks = []
    idx = 8
    while idx < len(data):
        length = struct.unpack('>I', data[idx:idx+4])[0]
        chunk_type = data[idx+4:idx+8]
        if chunk_type == b'IDAT':
            idat_chunks.append(data[idx+8:idx+8+length])
        elif chunk_type == b'IEND':
            break
        idx += 12 + length
        
    decompressed = zlib.decompress(b''.join(idat_chunks))
    
    # 4x4 image, RGBA (8 bit) => width=4. 
    # Each row has 1 filter byte + 4 * 4 bytes = 17 bytes.
    # Total 4 rows = 68 bytes.
    colors = set()
    for row in range(4):
        offset = row * 17 + 1
        for col in range(4):
            pixel_offset = offset + col * 4
            r, g, b, a = decompressed[pixel_offset:pixel_offset+4]
            if a > 50:
                colors.add(f"#{r:02x}{g:02x}{b:02x}")
    return colors

print(parse_png('test4x4_3.png'))
