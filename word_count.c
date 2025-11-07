#include<stdio.h>

//defining helper_function
void helper_function(FILE *fp);

//programs is meant to take in a file and return back the number of lines, words, and characters in the file
//if no file is presented, than the user types in a file
int main(int argc,char* argv[]){
	FILE *fp;
	
	//checks to see if a file was presented
	if (argc > 1){
	fp = fopen(argv[1], "r");
	
	//check to see if file was able to open, if not program ends
	if (fp == NULL){	
		printf("Could not open file for reading\n");
		return 1;
		}
	//if file was not presented, user types file
	}else{
	
		fp = stdin;
	//checks to see if stdin worked, if not program ends
         	if (fp == NULL){
                	printf("stdin failed \n");
        		return 1;
                	}	
	}
	//call for helper function	
	helper_function(fp);
	
	//prints the file name if it exist
	if (argc > 1){
		printf("%s",argv[1]);
	}
	printf("\n");
	return 0;
}

//helper function counts and prints the number of lines, words, and characters in the provided file, return nothing
void helper_function(FILE *fp){
	int count_line = 0;
	int count_word = 0;
	int count_characters = 0;
	int ch = fgetc(fp);
	int prev= ch;
	
	//loops through the entrie file by looking through every character until it reaches EOF
	//always adds 1 to character count and keeps track of the previous character
	while (ch != EOF){
	
		//checks to see if line ended, if so adds 1 to count line
		if (ch == '\n'){
			count_line++;
			
			//checks to see if there was no space or tab before the line ended, if so adds 1 to word count
			if (prev != ' ' && prev != '	'){
				count_word++;
		}
		}
	
		//checks to see if the characters is a space or tab and then checks to see if the previous charcher is not a sapce or tab. if all is true, it add 1 to word count
		else if (ch == ' '|| ch == '	'){
			
			if (prev != ' ' && prev != '	'){
				count_word ++;
		}
		}

		count_characters ++;
		prev = ch;
		ch = fgetc(fp);
		
	}
	printf("%d    ", count_line);
	printf("%d    ", count_word);
	printf("%d ",count_characters );
  }	

