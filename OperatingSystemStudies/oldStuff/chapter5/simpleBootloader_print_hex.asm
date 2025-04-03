; recieving the data in 'dx'
; for the example, let's assume we called dx=0x1234
print_hex:
  pusha

  mov cx, 0 ; the index var, i for example

hex_loop:
  cmp cx, 4 ; loops 4 times
  je end

  ; 1. convert last char of 'dx' to ascii
  mov ax, dx ; use ax as the working register
  and ax, 0x000f ; 0x1234 -> 0x0004 by masking first three to zeros
  add al, 0x30 ; add 0x30 to N to convert it to ASCII "N"
  cmp al, 0x39 ; if > 9, add 8 to change 'A' to 'F'
  jle step2
  add al, 7 ; 'A' is ASCII 65 instead of 58, so 65 - 58 = 7

step2:
  ; 2. get the correct position of the string to place our ASCII char
  ; bx <- base address + string length - index of char)
  mov bx, HEX_OUT + 5 ; base + length
  sub bx, cx ; our index variable
  mov [bx], al ; copy the char of 'al' to the position pointed by 'bx'
  ror dx, 4 ; this is complicated but 0x1234 would loop to 0x4123, then 0x3412, 0x2341, and finally back to 0x1234
  
  add cx, 1
  jmp hex_loop

end:
  ; prepare the parameter and call the funct
  mov bx, HEX_OUT
  call print
  
  popa
  ret

HEX_OUT:
  db '0x0000', 0 ; reserve the memory for the new string

