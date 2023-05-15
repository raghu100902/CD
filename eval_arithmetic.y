%{
	#include<stdio.h>
	int yylex(void);
	int yyerror(char* s);
%}
%token NUMBER ID
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%
S:E{
	printf("result = %d\n",$$);
	return 0;
	}
E:E'+'E { $$=$1 + $3; }
 |E'-'E { $$=$1 - $3; }
 |E'*'E { $$=$1 * $3; }
 |E'/'E { $$=$1 / $3; }
 |E'%'E { $$=$1 % $3; }
 |'-'NUMBER { $$ = -$2; }
 |'-'ID { $$ = -$2; }
 |'('E')' { $$ = $2; }
 |NUMBER { $$ = $1; }
 |ID { $$ = $1; }
 ;
%%

void main()
{
	printf("enter any arithmetic expression\n");
	yyparse();
}
int yyerror(char* s)
{
	printf("invalid arithmetic expression\n");
}
