# Description
# BabyEncryption hackthebox.com


import string
# from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)


a = b"asdf"
print(a.hex())

msg = b"ac"
ct = encryption(msg)
f = open('./msg.enc', 'w')
print(ct.hex())
f.write(ct.hex())

f.close()


l = [13, 34, 7]
print(l, "-> ", bytes(l))

b = bytes(l)

h = b.hex()
print(b, "->", h)

def delimit(msg):
    l = []
    n = len(msg)
    i = 0
    while i < n - 1:
        x = msg[i] + msg[i + 1]
        a = int(x, 16)
        l.append(a)
        i += 2
    return l


print(delimit(h))
# int_values = [x for x in b]

# print(int_values)

print("start decrepting")
enc = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
enc_my = "ada3"
def decrypt(msg):
    m = 256
    a = 123
    l = delimit(msg)
    print(l)
    # print(l)
    for i in range(len(l)):
        l[i] = (l[i] - 18) % m
    print(l)
    a_inv = pow(a, -1, m)
    print("a_inv ", a_inv)
    for i in range(len(l)):
        l[i] = (l[i] * a_inv) % m
    print(l)
    print(''.join(chr(i) for i in l))
decrypt(enc)

