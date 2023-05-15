%{
	#include<stdio.h>
	#include "y.tab.h"
	extern YYSTYPE yylval;
	
%}

%%
[0-9]+	{yylval=atoi(yytext);return NUMBER;}
[a-zA-Z]+ {return ID;}	
[\t]+	;
\n	;
.	{return yytext[0];}
%%
int yywrap()
{
	return 1;
}

