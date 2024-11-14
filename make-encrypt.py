import struct

def xcrypt(content, length):
    encrypted = bytearray()  # Sử dụng bytearray để lưu trữ dữ liệu mã hóa

    key = 0xea1ab19f  # Khóa mã hóa ban đầu (giống như var_C trong mã giả)

    for word in range(length // 4):  # Thay thế 'xrange' bằng 'range' trong Python 3 và sử dụng phép chia nguyên '//' 
        # Lấy 4 byte mỗi lần
        byte_data = content[word*4:((word*4)+4)]

        # Chuyển đổi 4 byte thành một số nguyên (32-bit) theo định dạng little-endian
        long_to_xor = struct.unpack('<L', byte_data)[0]

        # Mã hóa bằng cách áp dụng XOR với khóa
        encrypted_bytes = long_to_xor ^ key

        # Thêm kết quả đã mã hóa vào dữ liệu đầu ra
        encrypted.extend(struct.pack('<L', encrypted_bytes))

        # Thực hiện biến đổi khóa cho mỗi vòng lặp
        for mutation in range(8):
            if (key & 1) != 0:
                key = key >> 1
                key = key ^ 0x6daa1cf4
            else:
                key = key >> 1

    return bytes(encrypted)  # Trả về dữ liệu mã hóa dưới dạng bytes

if __name__ == '__main__':
    # Đọc nội dung từ tệp in.tfc
    with open('in.tfc', 'rb') as file:
        content = file.read()

    # Đặt chiều dài của nội dung tệp
    length = len(content)

    # Mã hóa nội dung
    encrypted_content = xcrypt(content, length)

    # Lưu kết quả vào tệp out.tfc
    with open('out.tfc', 'wb') as file:
        file.write(encrypted_content)

    print("File đã được mã hóa và lưu vào out.tfc.")
