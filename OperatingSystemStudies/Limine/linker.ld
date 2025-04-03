/* This linker script was created by Sir Nacho*/
/* CREDIT: https://wiki.osdev.org/Limine_Bare_Bones */

/* Tell the linker that we want an x86_64 ELF64 output file */
OUTPUT_FORMAT(elf64-x86-64)

/* We want the symbol of kmain to be the entry point */
ENTRY(kmain)

/* Define the program headers we want so the bootloadeer gives us the right */
/* MMU permissions; this also allows us to exert more control over the linking process. */
PHDRS
{
  limine_requests PT_LOAD;
  text PT_LOAD;
  rodata PT_LOAD;
  data PT_LOAD;
}

SECTIONS
{

  /* We want to be placed in the topmost 2GiB of the address space, for optimisations */
    /* and because that is what the Limine spec mandates. */
    /* Any address in this region will do, but often 0xffffffff80000000 is chosen as */
    /* that is the beginning of the region. */
  . = 0xffffffff80000000;

  .limine_requests : {
    KEEP(*(.limine_requests_start))
    KEEP(*(.limine_requests))
    KEEP(*(.limine_requests_end))
  } :limine_requests

  /* Move to the next page for .text*/
  . = ALIGN(CONSTANT(MAXPAGESIZE));

  .text : {
    *(.text .text.*)
  } :text

  /* Same thing, but with .rodata */
  . = ALIGN(CONSTANT(MAXPAGESIZE));
  
  .rodata : {
    *(.rodata .rodata.*)
  } : data

  /* again, but with .data */
  . = ALIGN(CONSTANT(MAXPAGESIZE));

  .data : {
    *(.data .data.*)
  } : data

  /* .bss needs to be the last thing to be mapped to :data or else lots of zeros would be written to the binary*/
  .bss : {
    *(.bss .bss.*)
    *(COMMON)
  } : data

  /* Discard .note.* and .eh_frame* since they causes issues to some hosts */

  /DISCARD/ : {
    *(.eh_frame*)
    *(.note .note.*)
  }
}

