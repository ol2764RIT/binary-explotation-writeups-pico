object dissasembly binary

clutter is at 
  4006cb:       48 81 ec 10 01 00 00    sub    $0x110,%rsp

  this means we have a buffer of 0x100 bytes

rbp-0x8    → code   (8 bytes)
rbp-0x10   → padding (alignment / unused)

is our stack most likely


we want to overwrite rbp-0x8 which we found from the cmp instruction against 0xdeadbeef (eax)

so we have to buffer overwrite the gets() since it does 0 bounds checking with enough x's to append 0xdeadbeef for flag!

