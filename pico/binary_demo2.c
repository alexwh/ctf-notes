#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  setbuf(stdin, NULL); // Don't worry about this.
                       // Unless you're a C-pro, in which case, trivia question:
                       // why might the program break without this? :P

  // Three "line" buffers, all initialized to be filled with null bytes.
  char line1[20];
  bzero(line1, 20);

  char line2[20];
  memset(line2, 0, 20);

  // This might look like just the first byte is set to a null byte,
  // but no, the full buffer gets zeroed.
  char line3[20] = {0};



  // All different ways of reading from the terminal. Although they all do
  // the same thing, they all have slightly different behavior. Use the
  // terminal manual pages to learn more! In all cases, up to 19 characters
  // are read, so line1, line2, and line3 will always be null terminated.

  // This reads up to a newline, or up to 19 chars, whichever comes first.
  fgets(line1, 19, stdin);

  // This does NOT stop at a newline, and keeps reading a full 19 chars (including
  // newlines). (It might read less than 19 chars if the input ends, though.)
  fread(line2, 1, 19, stdin);

  // This MAY OR MAY NOT stop reading at newlines, depending on the circumstances.
  // (Usually, it will stop and newlines when entering stuff live at the terminal,
  // but not when piping input in from a file).
  read(STDIN_FILENO, line3, 19); // STDIN_FILENO is just 0



  // line1X is a string that starts at the second half of the line1 buffer.
  // This string now "overlaps" with the "line1" string, since both line1 and
  // line1X point to the same buffer space.
  char *line1X = &amp;line1[10];


  // This next line overwrites the 10th character of the line1 buffer with a null
  // byte. Strings in C end at null bytes, so now "line1" is like a string that
  // is up to 9 characters long (if the first line entered was shorter than 9
  // characters, then the line1 buffer already has an earlier null byte and
  // thus "line1" continues to represent a string shorter than 9 characters).
  // After these lines, line1X and line1 still point to the same buffer space,
  // but will act like independent strings since the "line1" string certainly
  // ends before the "line1X" string starts.
  line1X[-1] = 0;
  line1[9] = 0; // This line is useless: it "changes" exactly the same byte as
                // the previous line, we already just set that byte to zero!
                // (It does make more sense than the previous line though,
                // because negative indexing is kinda confusing.)



  if(strcmp(line1, line1X) != 0) {
    puts("fail!");
    return 1;
  }



  int i;
  for(i = 0; i < strlen(line2); i++) {
    // Modify line2 by XORing it's bytes.
    line2[i] ^= "banannabanannabanannabananna"[i];
  }

  for(i = 0; i < strlen(line3); i++)
    line3[i] += 0x80; // Modify line3 by incremeting its bytes.
                      // Note that chars are 8 bit, so this is likely to wrap.

  if(strcmp(line2, line3) == 0) {
    // If they match, run the lines as a command. In a CTF problem,
    // you'll want a line that says "sh" or something.
    system(line3);
  } else {
    puts("NOOOOOOOOOOOOOOOOOOO");
    return 1;
  }

  return 0;
}
