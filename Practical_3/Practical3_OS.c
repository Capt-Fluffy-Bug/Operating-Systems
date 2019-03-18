#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>

int main(){
	int f, a = 10, b = 20, c;
	printf("Parent process: %d\n", getppid());
	printf("Child process: %d\n", getpid());
	
	f = fork();
	printf("After fork\n");
	printf("Process ID: %d\n", getpid());
	wait();
	
	if(f > 0){
		c = b - a;
		printf("Difference = %d\n", c);
		sleep(5);
		printf("Parent and Child PID: %d, %d\n", getppid(), getpid());
	}
	
	if(f == 0){
		c = b / a;
		printf("Quotient: %d\n", c);
		printf("Parent and Child PID: %d, %d\n", getppid(), getpid());
	}
	return 0;
}
