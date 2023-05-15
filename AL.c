#include<stdio.h>
#include<conio.h>
#include<string.h>
struct three
{
	char data[10],temp[7];
}s[30];
void main()
{
    char *d1,*d2;
    int i=0,len=0;
    FILE *f1,*f2;
    f1=fopen("exe.txt","r");
    f2=fopen("exe1.txt","w");
    while(fscanf(f1,"%s",s[len].data)!=EOF)
    	len++;
    for(i=0;i<=len;i++)
    {
    	if(!strcmp(s[i].data,"="))
        {
        	fprintf(f2,"\nLDA\t%s",s[i+1].data);
            if(!strcmp(s[i+2].data,"+"))
            	fprintf(f2,"\nADD\t%s",s[i+3].data);
            if(!strcmp(s[i+2].data,"-"))
            	fprintf(f2,"\nSUB\t%s",s[i+3].data);
            fprintf(f2,"\nSTA\t%s",s[i-1].data);
        }
    }
    fclose(f1);
    fclose(f2);
    getch();
}
