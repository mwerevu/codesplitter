options obs=0;
data test0;
set _NULL_;
run;
data temp;
do i=1 to 10;
output;
end;
run;
proc print data=temp;
run;
;
data temp1;
do i=1 to 1;
output;
end;
run;
proc print data=temp1(where=(i gt 3));
run;
data temp2;
do i=1 to 2;
output;
end;
run;
proc print data=temp2(where=(i gt 3));
run;
data temp3;
do i=1 to 3;
output;
end;
run;
proc print data=temp3(where=(i gt 3));
run;
data temp4;
do i=1 to 4;
output;
end;
run;
proc print data=temp4(where=(i gt 3));
run;
data temp5;
do i=1 to 5;
output;
end;
run;
proc print data=temp5(where=(i gt 3));
run;
;
data OUTPUTS.manual1;
set INPUTS.manual0;
run;
