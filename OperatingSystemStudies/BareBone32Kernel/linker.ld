/* This script is created by Sir Nacho 
 *
 * CREDIT: https://wiki.osdev.org/User:Zesterer/Bare_Bones
 *
 * */

/* The bootloader will start execution at the symbol designated as the entry point 
 * which is start from start.s*/
ENTRY(start)

/* Tell the linker part of the compiler where the sections of the kernel will be put*/
SECTIONS
{
    /* We will start with putting the section at 1 MB for the kernel to be loaded by the bootloader
     * This also because of how below 1 MB is where other x86-related things were reserved.
     * */
    . = 1M;

    /* This is where we align all sections in the executable to the multiple of 4 Kilobytes.
     * This will be useful for later in development when adding paging*/

    /* We need to start putting the multiboot header as it's required to be near the start of the executable
     * or else the bootloader like GRUB can't find it*/
    /* The multiboot header is read only, so we put it in the .rodata section*/

    .rodata BLOCK(4K) : ALIGN(4K) 
    {
      *(.multiboot)
    }

    .text BLOCK(4K) : ALIGN(4K)
    {
      *(.text)
    }

    .rodata BLOCK(4K) : ALIGN(4K)
    {
      *(.rodata)
    }

    .data BLOCK(4K) : ALIGN(4K)
    {
      *(.data)
    }

    /* This is where the stack and unintialized read-write data goes*/
    .bss BLOCK(4K) : ALIGN (4K)
    {
      *(COMMON)
      *(.bss)
    }
}

