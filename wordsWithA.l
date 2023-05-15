%{
    #include<stdio.h>
    int c = 0;
%}
%%
^[aA][a-zA-Z]+ { c++; }
\n { return 0; }
. {}
%%
int yywrap() {}
int main() {
    yylex();
    if (c > 0) {
        printf("Accepted!\n");
    } else {
        printf("Not Accepted!\n");
    }
    return 0;
}
