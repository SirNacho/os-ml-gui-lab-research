mov ah, 0x0e ; tty mode

mov bp, 0x8000 ; away from 0x7c00 to not get overwrited
mov sp, bp ; in a nutshell, if (stack == isEmpty()) then {sp = bp;} 

push 'A'
push 'B' ;    <---- Pushing some stuff to the stack
push 'C'

mov al, [0x7ffe] ; 0x8000 -2
int 0x10


mov al, [0x8000] ; Due to growing the stack, we can't access 0x8000, The only way to access the top of the stack is to go to 0x7ffe from above
int 0x10


; printing section:
pop bx
mov al, bl ; "C"
int 0x10 

pop bx
mov al, bl ; "B"
int 0x10

pop bx
mov al, bl ; "A"
int 0x10 


; Data that has been pop'd from the stack is garbage
mov al, [0x8000]
int 0x10

jmp $
times 510-($-$$) db 0
dw 0xaa55
