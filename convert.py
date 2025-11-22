import binascii

with open("model.tflite", "rb") as f:
    data = f.read()

hex_data = binascii.hexlify(data).decode('utf-8')

with open("model.h", "w") as f:
    f.write("const unsigned char model_tflite[] = {\n")

    for i in range(0, len(hex_data), 2):
        byte = "0x" + hex_data[i:i+2]
        if i < len(hex_data) - 2:
            byte += ","
        f.write(byte)
        if (i//2 + 1) % 12 == 0:  # 12 bytes per line
            f.write("\n")

    f.write("\n};\n")
    f.write("unsigned int model_tflite_len = {};\n".format(len(data)))
