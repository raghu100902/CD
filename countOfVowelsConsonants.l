%{
    int vowel = 0, cons = 0;
%}

%%
[aeiouAEIOU] { vowel++; }
[A-z] { cons++; }
\n { return 0; }
. {}
%%

int yywrap() {}

int main() {
    yylex();
    printf("Count of Vowels: %d\n", vowel);
    printf("Count of Consonants: %d\n", cons);
    return 0;
}
