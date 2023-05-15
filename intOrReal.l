%{
    #include<stdio.h>
%}
%%
[0-9]*(\.|\.e|e)[0-9]+ { printf("\"%s\" is a Real Number\n", yytext); }
[0-9]+ { printf("\"%s\" is an Integer\n", yytext); }
\n { return 0; }
. {}
%%

int yywrap() {}

int main() {
    yylex();
    return 0;
}
