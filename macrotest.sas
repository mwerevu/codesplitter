options mfile mprint;
filename mprint 'debug.sas';
%macro runall;
options obs=0;

%macro test1;

    data temp;
        do i=1 to 10;
            output;
        end;
    run;
    proc print data=temp;
    run;
    
%mend test1;


%macro test2(cnt);
    %do ii=1 %to &cnt.;
        data temp&ii.;
            do i=1 to &ii.;
                output;
            end;
        run;
        proc print data=temp&ii.(where=(i gt 3));
        run;
    %end;
%mend;
            
data test0;
    set _NULL_;
run;
%test1;
%test2(5);
%mend;
%runall;
