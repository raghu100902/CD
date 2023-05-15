%{
#include<stdio.h>
int l = 1;
%}
delim [ \t\b]
ws {delim}*
ident [A-Za-z][A-Za-z0-9]*
op [\+\-\*/%=]
special [;\{\}\[\]\(\)<>]
%%
{ws}(int|return|include) { printf("%d\t\"%s\"\t\t\tKeyword\n", l, yytext); }
{ident} { printf("%d\t\"%s\"\t\t\tIdentifier\n", l, yytext); }
{op} { printf("%d\t\"%s\"\t\t\tOperator\n", l, yytext); }
{special} { printf("%d\t\"%s\"\t\t\tSpecial\n", l, yytext); }
\n { l++; }
. {}
%%

int main() {
    extern FILE *yyin;
    printf("LineNumber\tLexme\t\tToken\n");
    yyin = fopen("hello.c", "r");
    yylex();
    return 0;
}
