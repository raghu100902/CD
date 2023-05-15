%{
#include "y.tab.h"
%}
%%
[0-9]+ { yylval = atoi(yytext); return NUM; }
"==" { return EQ; }
"!=" { return NEQ; }
"<" { return LT; }
">" { return GT; }
"<=" { return LTE; }
">=" { return GTE; }
[ \t] ; /* ignore whitespace */
\n ; /* ignore newline */
. { return yytext[0]; } /* catch-all rule for unmatched characters */
%%
int yywrap() {
    return 1;
} 
