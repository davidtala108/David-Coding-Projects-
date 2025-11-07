#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
// struct defiton for the inode
typedef struct{
uint32_t inode;
uint32_t parentInode;
char type;
char name[32];
}Inode;

Inode inodeList[1024]; // an array of inodes where each inode represents a file or a directory
size_t inodeCount = 0; // a count of the number of inodes in the list, initialized to zero
uint32_t currentInode = 0; // a variable to hold and keep track of the current inode

void loadInodeList() {
    FILE *fp = fopen("inodes_list", "rb");
    if (fp == NULL) {
        printf("ERROR 401 : File Failed to Open\n");
        exit(1);
    }

    size_t count = fread(inodeList, sizeof(Inode), 1024, fp);
    if (count == 0) {
        printf("Error 406: Failed to read inodes\n");
        fclose(fp);
        exit(1);
    }

    inodeCount = count;
    fclose(fp);
}	
// read the inodeList from the file path to your inodeList array
// update the inodeCount
// remember that your director`y will have only one inodeList with a given number of inodes in the list 
void saveInodeList() {
	 FILE *fp = fopen("inodes_list", "wb");
    if (fp == NULL) {
        printf("ERROR 401 : File Failed to Open\n");
        exit(1);
    }

    size_t w = fwrite(inodeList, sizeof(Inode), inodeCount, fp);
    if (w < inodeCount) {
        printf("Error 407 : write failed\n");
	fclose(fp);
        exit(1);
    }

// write the content of the inodelist to the file path
	fclose(fp); 
}

void changeDirectory(const char *name) {

	int i;
    for (i = 0; i < inodeCount; i++) {
        if (strcmp(inodeList[i].name, name) == 0) {
	    if (inodeList[i].type == 'd'){
            currentInode = i;
            break;
		}
        }
    }

    if (i == inodeCount) {
        printf("Error 403: Directory not Found\n");
    }
		 
// iterate through the inodeList to search whether a directory with the name already exists
// // if yes, then set the currentInode value to the index of the list with that name
// // otherwise print an error message to indicate that the directory is not found
 }

void listContents() {
// iterate through inodeList and print the members of those elements in the list for which the parentInode is
// the currentInode
        for ( int i = 0; i < inodeCount; i++){
		if (inodeList[i].parentInode == currentInode){
		printf("Inode: %d, type: %c, name: %s\n", inodeList[i].inode, inodeList[i].type, inodeList[i].name); 	
}
}
}                 
void createDirectory(const char *name) {
	if (inodeCount <= 1024){
		for( int i = 0; i <inodeCount; i++){
			if (strcmp(inodeList[i].name, name) == 0){
				exit(1);
			}
			}
			
			Inode inode;
			inode.inode = inodeCount;
			inode.parentInode = currentInode;
			inode.type = 'd';
			strcpy(inode.name, name);
	
			inodeList[inodeCount] = inode;
			
			FILE *fp = fopen(name, "wb");
	       		
			if (fp == NULL){
               	 	printf("ERROR 402: File failed to open");
                	exit(1);
        		}

		        size_t check = fwrite(&inode.inode, sizeof(int), 1, fp);
                        if (check == 0){
                                printf("Error 407 : write failed\n");
				fclose(fp);
                                exit(1);
                        }
			size_t check22 = fwrite(&inode.parentInode, sizeof(int), 1, fp);
                        if (check22 == 0){
                                printf("Error 407 : write failed\n");
				fclose(fp);
                                exit(1);
                        }

			inodeCount++;
			fclose(fp);
		}else{
		printf ("Error 408: inodelist is full\n");
		exit(1);		
 	}
}
// iterate through the inodeList to see if the name of the directory exists; if yes, exit
// // check to see if the inodeCount is 1024; if yes, exit
// // create a new inode with new inodeCount, set its parentInode and type, and also its name
// // create a file with its name as the inode number
// // write into this file its . and .. inode values
 
void createFile(const char *name) {
	if (inodeCount <= 1024){
                
		for( int i = 0; i <inodeCount; i++){
                        if (strcmp(inodeList[i].name, name) == 0){
                                exit(1);
                        }
                        }
                        Inode inode;
			inode.inode= inodeCount;
                        inode.parentInode = currentInode;
                        inode.type = 'f';
                        strcpy(inode.name, name);
		
			inodeList[inodeCount] = inode;

			FILE *fp = fopen(name, "wb");
                
		        if (fp == NULL){
                        printf("ERROR 402: File failed to open");
			exit(1);
                        }
                        size_t check = fwrite(&inode.inode, sizeof(int), 1, fp);
			if (check == 0){
				printf("Error 407 : write failed\n");
				fclose(fp);			
			}
				
			inodeCount++;
			fclose(fp);
		}else{
                printf ("Error 408: inodelist is full\n");
		exit(1);
        }
}
		
                        
// // iterate through inodeList to see if filename exists; if yes, exit
// // check if the inodeCount is 1024; if yes, exit
// // create a new entry for an inode in inodeList
// // create a file with its name as the inode number
// // write into this file its filename
void exit2(){
        saveInodeList();
} 
int main(int argc, char *argv[]){
    	if (argc != 2){
		printf ("Error 409 : Must give 2 comand line agruments\n");
		return 1;
	}

	chdir(argv[1]);
	
	loadInodeList();
	
	char command[64];
	while(1){
	printf(">");
		
	scanf(" %[^\n]", command);
	
	if (strlen(command) == 0){
		continue;
	}
	if (strcmp(command, "exit") == 0){
		break;
	}
	
	if (strcmp(command, "ls") == 0){
		listContents();		
	}else{
		char *token = strtok(command, " ");
		char *name = strtok(NULL, "\n");
	
		if (strcmp(token, "cd") == 0){
			if (name == NULL){
			printf("Error: need directory name\n");
			} else{
			changeDirectory(name);
		}
		}else if (strcmp(token, "mkdir") == 0){
			 if (name == NULL){
                        printf("Error: need name to create directory\n");
                        } else{
			createDirectory(name);
			}
		}else if (strcmp(token, "touch") == 0){
			 if (name == NULL){
                        printf("Error: need name to create file\n");
                        } else{
		
			createFile(name);
		}
		}
		}
	
	}
	exit2();
	return 0;
}
	
	


