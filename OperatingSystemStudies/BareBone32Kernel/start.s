//This script is made by Sir Nacho on 4/3/2025

//CREDIT: https://wiki.osdev.org/User:Zesterer/Bare_Bones

//Declaring the main funct of kernel.c

.extern kernel_main

//declaring 'start' as a global var since the linker need to know about it later on
.global start

//This is the "magic' constant that GRUB will use to detect our kernel's location.
.set MB_MAGIC, 0x1BADB002 

//Loads the modules on to the page boundaries while providing a memory map.
.set MB_FLAGS, (1 << 0) | (1 << 1)

//Calculating the checksum of all previous values
.set MB_CHECKSUM, (0 - (MB_MAGIC + MB_FLAGS))

//starting the section of the executable that will contain our multiboot header
.section .multiboot
    .align 4 // make sure the following data is aligned on a multiple of 4 bytes.
    .long MB_MAGIC
    .long MB_CHECKSUM

//Intialzing the zeroes when kernel is loaded
.section .bss
    .align 16
    stack_bottom:
      .skip 4096 // Reserving 4096 bytes for the stack 
    stack_top:

//This section contains our actual assembly code to be run when our kernel Loads
.section .text
  //Hey look, the start label that we globalized earlier, this is where we Loads
  //The first code that gets run in our kernel.
 
  //NOTE: This kernel is x86, so the stack goes DOWNWARD.
  
  start:
    mov $stack_top, %esp //   <---- setting pointer to the top of the stack
    call kernel_main // <---- Calling main funct of kernel.c since it's the 
                            //environment is read to run.
      

    hang:
      cli           // <---- Disable CPU interrupts
      hlt           // <---- Halt the CPU
      jmp hang           // <---- If somehow doesn't work, it'll loop back to hang
    


