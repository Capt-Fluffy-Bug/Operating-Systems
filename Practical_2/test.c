#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>

int main(){
	int i, fd,op,fw,fr;
	char buff[50] = "I am vengeance! I am the night! I am Batman!";
	
	
	fd = creat("test.txt", 0777);
	
	op = open("test.txt", O_RDWR, 0777);
	
	fw = write(op, buff, sizeof(buff));
	
	fr = read(fw, buff, sizeof(buff));
	
	for(i = 0;i < 50;i++){
		printf("%c\n", fr);
	}
	close(fd);
	
	return 0;
}
