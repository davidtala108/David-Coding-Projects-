#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//defines helper function
void helper_function(FILE *fp);
//program reads a file and returns the line if the line is not the same as the pervious line
int main (int argc, char * argv[]){
	FILE *fp;
	
	//checks to see if file was given
	if(argc > 1){
		fp = fopen(argv[1], "r");
	//checks to see if file open, if not program ends
	if (fp == NULL){
		printf("Could not open file\n");
		return 1;
	
		}
	
	//if file was not given, user writes file
	}else{
		fp = stdin;
	
	 //checks to see if stdin work, if not program ends
	 if (fp == NULL){
                printf("stdin failed \n");
        	return 1;
                }
	}
	
	//helpr function called
	helper_function(fp);        
        return 0;
}

//helper function reads through the file and prints the line only if it is not the same as the pervious line
void helper_function(FILE *fp){
	
	char *buffer = NULL;
	size_t buffer_size = 0;
	size_t characters = 0;
	
	
	characters = getline(&buffer, &buffer_size, fp);
	
	//checks to see if getline failed, if so program ends
	if (buffer == NULL){
		printf("getline failed");
	
	//prints the first line if getline deos not fail	
	}else{
		printf("%s",buffer);
	
	/*loops through the file and save the line in varible call buffer2
	  Buffer2 then is compared with the pervious line to see if they are the same
	  if its not the same, the it prints buffer2, else it skips printing buffer2	 
	*/    
	while (characters != -1 ){

	char *buffer2 = NULL;
        size_t buffer_size2 = 0;
        size_t characters2 = 0;	
	
	characters2 = getline(&buffer2,&buffer_size2,fp);
	//checks to see if get line failed, if so program ends
	if (buffer2 == NULL){
                printf("getline failed");
		break;
                }
	//comapres the current line with the perious line to see if they are the same
	//if so it does not print the line, else it prints the line
	if (strcmp(buffer, buffer2) != 0){
	
		printf("%s", buffer2);
	
		//buffer is free before changing to aviod memory leaks	
		free(buffer);
        	buffer = buffer2;
		buffer_size = buffer_size2;

	}else{
		free(buffer2);
	}		
	characters = characters2;	
		}
	//buffer is free to avoid memory leaks
	free(buffer);
	}
        fclose(fp); 	
}
