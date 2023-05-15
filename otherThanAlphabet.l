%{
  int len=0;
%}
%%
[a-zA-Z]+ {printf("No character other than alphabets");}
.* {printf("character other than alphabets present"); }
%%
int yywrap() { }
int main()
 {
  yylex();
  return 0;
 }
