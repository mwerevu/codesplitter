/* DATA block with single SET */
data temp1;
    set temp2;
run;
data 
    temp1;
    set 
        temp2;
run;

data OUTPUTS.temp1(drop=a);
    set INPUTS.temp2(keep=c d);
    b=2;
run;
