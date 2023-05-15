%{
#include <stdio.h>
int valid = 1;
%}
%token NUM
%token EQ NEQ LT GT LTE GTE
%left EQ NEQ LT GT LTE GTE
%start expr
%%
expr: NUM { printf("Expression: %d\n", $1); }
    | expr EQ expr { printf("Expression: %d == %d\n", $1, $3); }
    | expr NEQ expr { printf("Expression: %d != %d\n", $1, $3); }
    | expr LT expr { printf("Expression: %d < %d\n", $1, $3); }
    | expr GT expr { printf("Expression: %d > %d\n", $1, $3); }
    | expr LTE expr { printf("Expression: %d <= %d\n", $1, $3); }
    | expr GTE expr { printf("Expression: %d >= %d\n", $1, $3); }
    ;
%%
int main() {
    yyparse();
    if (valid)
	    printf("Success\n");
    return 0;
}
void yyerror(const char *s) {
    valid = 0;
    printf("Error: %s\n", s);
} 
