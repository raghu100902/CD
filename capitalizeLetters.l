%{
    #include<stdio.h>
%}
%%
[a-z] { printf("%c", yytext[0] - 32); }
\n { printf("\n"); return 0; }
%%

int yywrap() {}

int main() {
    yylex();
    return 0;
}
