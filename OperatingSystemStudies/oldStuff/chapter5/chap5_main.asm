[org 0x7c00]

mov bx, HELLO
call print
call print_nl

mov bx, BELOW
call print
call print_nl
call print_nl

mov bx, HEX_SPACE
call print
call print_nl
call print_nl

mov dx, 0x12fe
call print_hex
call print_nl
call print_nl

mov bx, HEX_SPACE
call print
call print_nl
call print_nl

mov bx, GOODBYE
call print
call print_nl

jmp $

%include "chap5_print.asm"
%include "chap5_print_hex.asm"

HELLO:
  db 'Hello From DePaul University :)', 0

BELOW:
  db 'Below is the hex value of the above message:', 0

GOODBYE:
  db 'Goodbye from Sir Nacho (adios)', 0

HEX_SPACE:
  db '----------HEX VALUE----------', 0

times 510-($-$$) db 0
dw 0xaa55
