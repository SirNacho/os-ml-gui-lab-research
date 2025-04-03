//This script was created by Sir Nacho

/*
 *
 *  CREDIT:
 *  https://wiki.osdev.org/Limine_Bare_Bones
 *
 */

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <limine.h>

//Setting the base revision to 3
__attribute__((used, section(".limine_requests")))
static volatile LIMINE_BASE_REVISION(3);

// The limine requests can be placed anywhere, but we should not optimized them away.
__attribute__((used, section(".limine_requests")))
static volatile struct limine_framebuffer_request framebuffer_request = 
{
  
  .id = LIMINE_FRAMEBUFFER_REQUEST,
  .revision = 0

};

//finally, define the start and end of the markers for the Limine requests.
//These can also be moved anywhere, to any .c file, as seen fit.

__attribute__((used, section(".limine_requests_start")))
static volatile LIMINE_REQUESTS_START_MARKER;

__attribute__((used, section(".limine_requests_end")))
static volatile LIMINE_REQUESTS_END_MARKER;

//gcc and clang reserve the right to generate the calls to the following 4 functions
//even if they are not directly called
//Implement them as the C specification mandates.
//DO NOT REMOVED THE FUNCTIONS
//They CAN be moved to a different .c file.




// LAST WARNING

void *memcpy(void *dest, const void *src, size_t n) {
    uint8_t *pdest = (uint8_t *)dest;
    const uint8_t *psrc = (const uint8_t *)src;

    for (size_t i = 0; i < n; i++) {
        pdest[i] = psrc[i];
    }

    return dest;
}

void *memset(void *s, int c, size_t n) {
    uint8_t *p = (uint8_t *)s;

    for (size_t i = 0; i < n; i++) {
        p[i] = (uint8_t)c;
    }

    return s;
}

void *memmove(void *dest, const void *src, size_t n) {
    uint8_t *pdest = (uint8_t *)dest;
    const uint8_t *psrc = (const uint8_t *)src;

    if (src > dest) {
        for (size_t i = 0; i < n; i++) {
            pdest[i] = psrc[i];
        }
    } else if (src < dest) {
        for (size_t i = n; i > 0; i--) {
            pdest[i-1] = psrc[i-1];
        }
    }

    return dest;
}

int memcmp(const void *s1, const void *s2, size_t n) {
    const uint8_t *p1 = (const uint8_t *)s1;
    const uint8_t *p2 = (const uint8_t *)s2;

    for (size_t i = 0; i < n; i++) {
        if (p1[i] != p2[i]) {
            return p1[i] < p2[i] ? -1 : 1;
        }
    }

    return 0;
}

// Halt and catch fire function.
static void hcf(void) {
    for (;;) {
        asm ("hlt");
    }
}

// The following will be our kernel's entry point.
// If renaming kmain() to something else, make sure to change the linker script accordingly.

void kmain(void) 
{
  if (LIMINE_BASE_REVISION_SUPPORTED == false)                        { hcf(); }
  if (framebuffer_request.response == NULL
    || framebuffer_request.response->framebuffer_count < 1)           { hcf(); }

  struct limine_framebuffer * framebuffer = framebuffer_request.response->framebuffers[0];

  for (size_t i = 0; i < 100; i++) {
    volatile uint32_t *fb_ptr = framebuffer->address;
    fb_ptr[i * (framebuffer->pitch / 4) + i] = 0xffffff;
  }

  hcf(); // We're done, so we just hang...
}
