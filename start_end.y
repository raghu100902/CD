%{
#include <stdio.h>
%}
%token ZERO ONE
%start input
%%
input: ZERO_OR_ONE expression ZERO_OR_ONE { printf("Valid input\n"); }
     ;
expression: ZERO
          | ONE
          | expression ZERO
          | expression ONE
          ;
ZERO_OR_ONE: ZERO | ONE;
%%
int main() {
    yyparse();
    return 0;
}
int yyerror(const char *s) {
    printf("Error: %s\n", s);
    return 0;
}
int yylex() {
    int c = getchar();
    if (c == '0') return ZERO;
    else if (c == '1') return ONE;
    else if (c == '\n') return 0;
    else return c;
}
