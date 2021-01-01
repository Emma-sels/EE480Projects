/** Simple On-board LED flashing program - written in C by Derek Molloy
*    simple functional struture for the Exploring Raspberry Pi book
*
*    This program uses GPIO4 with a connected LED and can be executed:
*         makeLED setup
*         makeLED on
*         makeLED off
*         makeLED status
*         makeLED close
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define GPIO_NUMBER "4"
#define GPIO4_PATH "/sys/class/gpio/gpio4/"
#define GPIO_SYSFS "/sys/class/gpio/"

void writeGPIO(char filename[], char value[]){
   FILE* fp;                           // create a file pointer fp
   fp = fopen(filename, "w+");         // open file for writing
   fprintf(fp, "%s", value);           // send the value to the file
   fclose(fp);                         // close the file using fp
}

int main(int argc, char* argv[]){

   printf("Starting the flashing LED program\n");
   while(1) {
      writeGPIO(GPIO_SYSFS "export", GPIO_NUMBER);
      usleep(500000);                  // sleep for 500ms
      writeGPIO(GPIO4_PATH "direction", "out");
      
      writeGPIO(GPIO_SYSFS "export", GPIO_NUMBER);
      usleep(500000);                  // sleep for 500ms
      writeGPIO(GPIO4_PATH "direction", "in");
   }
   
   return 0;
}
