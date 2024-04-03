
//Extracting the nth bit:
num=4
n=2
print(bin(4))
extracted_bit = (num>>n-1)&1
print(extracted_bit)

//Setting the nth bit:
num=4
n=2
print(bin(4))
num = num | (1<<n-1)
print(bin(num))


//Extract a range/group of bits in number:
num=122
l=2
r=4
print(bin(num))
mask1 = (1<<(l-1))-1
mask2 = (1<<(r))-1
mask3 = mask1 ^mask2
print(bin(mask3))
extracted_bits = (num & mask3)
extracted_bits >>=l-1
print(bin(extracted_bits))


//Set a group/range of bits in a number:
num=160
l=3
r=6
print(bin(num))
mask1 = (1<<(l-1))-1
mask2 = (1<<(r))-1
mask3 = mask1 ^mask2

print(bin(mask3))
set_num = num | mask3
print(bin(set_num))
