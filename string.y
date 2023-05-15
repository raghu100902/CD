%{
#include<stdio.h>
%}
%token A B
%%
start : S '\n' {return 0;}
S: A S B
|;
%%
main()
{
printf("enter string");
if(yyparse()==0)
printf("valid");
}
yyerror()
{printf("not accepted");
exit(0);
}
yywrap()
{
return 1;
}
