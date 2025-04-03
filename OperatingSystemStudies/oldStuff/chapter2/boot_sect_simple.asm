;This is a boot sector created by Sir Nacho


mov ah, 0x0e ; tty mode
mov al, 'H'
int 0x10
mov al, 'e'
int 0x10
mov al, 'l'
int 0x10
int 0x10 ; l is already on al registry
mov al, 'o'
int 0x10
mov al, ' '
int 0x10
mov al, 'f'
int 0x10
mov al, 'r'
int 0x10
mov al, 'o'
int 0x10
mov al, 'm'
int 0x10
mov al, ' '
int 0x10
mov al, 'D'
int 0x10
mov al, 'e'
int 0x10
mov al, 'P'
int 0x10
mov al, 'a'
int 0x10
mov al, 'u'
int 0x10
mov al, 'l'
int 0x10
mov al, ' '
int 0x10
mov al, 'U'
int 0x10
mov al, 'n'
int 0x10
mov al, 'i'
int 0x10
mov al, 'v'
int 0x10
mov al, 'e'
int 0x10
mov al, 'r'
int 0x10
mov al, 's'
int 0x10
mov al, 'i'
int 0x10
mov al, 't'
int 0x10
mov al, 'y'
int 0x10
mov al, '!'
int 0x10
int 0x10
int 0x10
mov al, ' '
int 0x10
mov al, ':'
int 0x10
mov al, ')'
int 0x10

jmp $ ; jump to current address which puts it into a infinite loop

;Padding stuff
times 510 - ($-$$) db 0 
dw 0xaa55

  ;loop:
  ;jmp loop

;times 510-($-$$) db 0
;dw 0xaa55
