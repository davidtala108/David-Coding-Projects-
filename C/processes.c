#define _GNU_SOURCE
#include <stdio.h>      // printf, FILE, fopen, getline
#include <stdlib.h>     // atoi, exit, malloc/free (if used)
#include <unistd.h>     // fork, execlp
#include <sys/types.h>  // pid_t
#include <sys/wait.h>   // wait, waitpid
#include <string.h>

int main( int argc, char * argv[]){
	//checks to see if we where given the right amount of arguments
	if (argc != 3){
		printf("Error: Need 2 agruments\n");
		return 1;
	}
	//Open files
	FILE *fp = fopen(argv[1], "r");
	if ( fp == NULL){
		printf("Error: File faild to open\n");
		return 1;
	}
	//change the string to read as an int
	int n = atoi(argv[2]);
	if (n == 0){
		printf("Error: atoi failed\n");
		return 1;
}

	//the varible list that I used 
	int count= 0;
	int line_count = 0;
	char *buffer = NULL;
	size_t buffer_size = 0;
	ssize_t charactor_count = 0;
	
	//Loop throgh each line of the file and makes a child process to process the line at the same time	
	while((charactor_count = getline(&buffer, &buffer_size, fp)) != -1){
	
		strtok(buffer, " ");
                char *URL = strtok(NULL, " ");

		size_t len = strlen(URL);
	
		//this is to get rid of the new line character so the url is read correctly by URL
		if (URL[len-1] == '\n'){
			URL[len-1] = '\0';
		}
		pid_t pid = fork();
		
		//This keeps track if the number of process that can run at once has been reach
		//wait if the max number of process allowed has been reach
		if (count == n){
			wait(NULL);
			count--;
			}
	
		//fail check for fork
		if (pid < 0){
			printf("Error: fork failed\n");
			return 1;
		}
		//Makes it to where the child process is the one processing the lines
		//Makes the parent print the line to tells us that the line has been printed
		if (pid == 0){
			execlp("curl", "curl", "-s", "-o", URL, URL, NULL);
			perror("Execl failed\n");
			exit(1);
		}else{
			line_count++;
			printf("Process 3287 processing line #%d\n", line_count);
			count++;
		}
			
	}

	//this does a last check to make sure all child process are terminated
	for (int i = 0; i < n; i++){
		wait(NULL);
	}
	free(buffer);
	fclose(fp);
	return 0;
	 


}
