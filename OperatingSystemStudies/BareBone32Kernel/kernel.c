//This script is created by Sir Nacho at 4/3/2025

//CREDIT: https://wiki.osdev.org/User:Zesterer/Bare_Bones

//Nice that GCC provides these headers
#include <stddef.h>
#include <stdint.h>

#if defined(__linux__)
  #error "This code must be compiled with a cross-compiler. Try again!"
#elif !defined(__i386__)
  #error "This code must be compiled with an x86-elf compiler. Try again!"
#endif

//This here is the VGA textmode buffer. To display the text, we must write 
//data to this memory location.

volatile uint16_t* vga_buffer = (uint16_t*)0xB8000;

//Btw, the VGA buffer has a default size of 80x25 chars.
const int VGA_COLS = 80;
const int VGA_ROWS = 25;

//Starting text position.
int term_col = 0;
int term_row = 0;
uint8_t term_color = 0x0F; // <---- Feel free to change the color. By Default,
                           // Default: Black background and White Foreground

//This funct initiates the terminal by clearing it.
void term_init()
{
  for (int col = 0; col < VGA_COLS; col++)
  {
    for (int row = 0; row < VGA_ROWS; row++)
    {
      //The VGA textmode buffer has size (VGA_COLS * VGA_ROWS),
      //We could use this to find the index of the buffer for our char
      const size_t index = (VGA_COLS * row) + col;
      
      //NOTES: Entries in the VGA buffer take the binary form of: BBBBFFFFCCCCCCCC
      // - B is the background color
      // - F is the foreground color
      // - C is the ASCII char 
      
      vga_buffer[index] = ((uint16_t) term_color << 8) | ' '; //Set the char to blank (space) char.
    }
  }
}

//This funct places a single char to the screen
void term_putc(char c)
{
  switch (c) //NOTE: you don't want to display all char.
  {
    case '\n': // New line char should return the column to 0, and increment the row
        {
          term_col = 0;
          term_row++;
          break;
        }
    default: //Normal char just get display and increment the column
        {
            const size_t index = (VGA_COLS * term_row) + term_col;
            vga_buffer[index] = ((uint16_t)term_color << 8) | c;
            term_col++;
        }
  }
  
  //If the char gets passed the last row, we reset both column and row to 0 to loop back to the top of the screen
  if (term_col >= VGA_COLS) 
  {
    term_col = 0;
    term_row = 0;
  }
}

//This funct is to print the whole string to the screen
void term_print(const char* str) 
{
  for (size_t i = 0; str[i] != '\0'; i++) // keep placing char until the null-terminating char '\0'
  {
    term_putc(str[i]);
  }
}

//The main function of the kernel!!!
void kernel_main() 
{
  //Initiate the terminal
  term_init();
  
  //Print the messages
  term_print("Hello from DePaul University!!!\n");
  term_print("This is a message from Sir Nacho!\n");
}
