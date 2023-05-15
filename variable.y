%{
	#include<stdio.h>
	int yylex();
	int yyerror();
	int valid=1;
%}

%token letter digit
%%
start:letter s
s:letter s
 |digit s
 |
 ;
%%

int main()
{
	printf("enter identifier to be tested\n");
	yyparse();
	if(valid)
	{
		printf("identifieris valid\n");
	}
	return 0;
}
int yyerror()
{
	printf("Identifier is invalid\n");
	valid=0;
	return 0;
}
