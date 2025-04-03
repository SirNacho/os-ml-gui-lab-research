; declaring global variables
[org 0x7c00]

mov ah, 0x0e

; Attempt 1
mov al, "1"
int 0x10
mov al, the_secret
int 0x10

; Attempt 2
mov al, "2"
int 0x10
mov al, [the_secret]
int 0x10

; Attempt 3

mov al, "3"
int 0x10
mov bx, the_secret
add bx, 0x7c00
mov al, [bx]
int 0x10

; Attempt 4

mov al, "4"
int 0x10
mov al, [0x7c2d]
int 0x10

jmp $

the_secret:
  db "X" ; ASCII code of "X" is 0x58

; padding stuff
times 510-($-$$) db 0
dw 0xaa55
