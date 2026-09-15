import zlib
import struct

def get_1x1_png_color(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    idat_start = data.find(b'IDAT')
    if idat_start == -1: return None
    
    # Read chunk length
    length = struct.unpack('>I', data[idat_start-4:idat_start])[0]
    idat_data = data[idat_start+4:idat_start+4+length]
    
    decompressed = zlib.decompress(idat_data)
    # The first byte is the filter type (usually 0).
    # Then follows the pixel data. For RGBA it's 4 bytes.
    if len(decompressed) >= 5:
        r, g, b, a = decompressed[1:5]
        return f"#{r:02x}{g:02x}{b:02x} (alpha {a})"
    elif len(decompressed) >= 4:
        r, g, b = decompressed[1:4]
        return f"#{r:02x}{g:02x}{b:02x}"
    return decompressed

print(get_1x1_png_color('test.bmp'))
