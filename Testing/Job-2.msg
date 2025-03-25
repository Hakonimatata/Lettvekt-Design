1

   Abaqus 2022                                  Date 25-mar-2025   Time 11:09:09
   For use by NORGES TEKNISK NATURVITENSKAPELIGE UNIVERSITET under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                0.100    
          AND A TOTAL TIME PERIOD OF                            1.00    
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-05
          THE MAXIMUM TIME INCREMENT ALLOWED IS                0.100    

     LINEAR EQUATION SOLVER TYPE         DIRECT SPARSE

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

 CONVERGENCE TOLERANCE PARAMETERS FOR MOMENT   
     CRITERION FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR ROTATION CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE MOMENT                              1.000E-02
     AVERAGE MOMENT    IS TIME AVERAGE MOMENT   
     ALTERNATE CRIT. FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO MOMENT    RELATIVE TO TIME AVRG. MOMENT        1.000E-05
     CRITERION FOR RESIDUAL MOMENT    WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR ROTATION CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL MOMENT    FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO MOMENT    REL. TO TIME AVRG. MAX. MOMENT       1.000E-05

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 TIME INCREMENTATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AT WHICH LOG. CONVERGENCE RATE CHECK BEGINS         8
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     EQUILIBRIUM ITERATION COUNT FOR CUT-BACK IN NEXT INCREMENT               10
     MAXIMUM EQUILIB. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      4
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            50
     MAXIMUM ATTEMPTS ALLOWED IN AN INCREMENT                                  5
     MAXIMUM DISCON. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      50
     MAXIMUM CONTACT AUGMENTATIONS FOR *SURFACE BEHAVIOR,AUGMENTED LAGRANGE   50
     CUT-BACK FACTOR AFTER DIVERGENCE                                 0.2500    
     CUT-BACK FACTOR FOR TOO SLOW CONVERGENCE                         0.5000    
     CUT-BACK FACTOR AFTER TOO MANY EQUILIBRIUM ITERATIONS            0.7500    
     CUT-BACK FACTOR AFTER TOO MANY SEVERE DISCONTINUITY ITERATIONS   0.2500    
     CUT-BACK FACTOR AFTER PROBLEMS IN ELEMENT ASSEMBLY               0.2500    
     INCREASE FACTOR AFTER TWO INCREMENTS THAT CONVERGE QUICKLY        1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED                       1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DYNAMICS)            1.250    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DIFFUSION)           2.000    
     MINIMUM TIME INCREMENT RATIO FOR EXTRAPOLATION TO OCCUR          0.1000    
     MAX. RATIO OF TIME INCREMENT TO STABILITY LIMIT                   1.000    
     FRACTION OF STABILITY LIMIT FOR NEW TIME INCREMENT               0.9500    
     TIME INCREMENT INCREASE FACTOR BEFORE A TIME POINT                1.000    
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                     100

          LARGE DISPLACEMENT THEORY WILL BE USED

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH      1.94    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       4.81       TIME AVG. FORCE        4.81    
 LARGEST RESIDUAL FORCE             -27.6       AT NODE         16   DOF  1
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      44.7       TIME AVG. MOMENT       44.7    
 LARGEST RESIDUAL MOMENT           -4.782E-02   AT NODE        740   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.979E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -2.979E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                      0.895       TIME AVG. FORCE       0.895    
 LARGEST RESIDUAL FORCE            -2.685E-03   AT NODE        345   DOF  1
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        5.082E-03   AT NODE         13   DOF  1
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      44.7       TIME AVG. MOMENT       44.7    
 LARGEST RESIDUAL MOMENT            4.145E-02   AT NODE         78   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.980E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     1.895E-04   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3


 AVERAGE FORCE                      0.895       TIME AVG. FORCE       0.895    
 LARGEST RESIDUAL FORCE             3.506E-05   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        5.962E-06   AT NODE        100   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      44.7       TIME AVG. MOMENT       44.7    
 LARGEST RESIDUAL MOMENT           -5.764E-05   AT NODE        740   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.979E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -6.030E-07   AT NODE        182   DOF  6
   INSTANCE: SPECIMEN                                                                        
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   3 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  3 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.100    
 STEP TIME COMPLETED       0.100    ,  TOTAL TIME COMPLETED        0.100    


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       1.83       TIME AVG. FORCE        1.36    
 LARGEST RESIDUAL FORCE            -3.572E-03   AT NODE        246   DOF  1
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.       -1.016E-02   AT NODE         14   DOF  1
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF DISP.    CORRECTION    6.584E-07
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      95.7       TIME AVG. MOMENT       70.2    
 LARGEST RESIDUAL MOMENT           -8.239E-02   AT NODE        184   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.980E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     3.795E-04   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          1

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       1.83       TIME AVG. FORCE        1.36    
 LARGEST RESIDUAL FORCE             1.372E-04   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        1.874E-05   AT NODE        317   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      95.7       TIME AVG. MOMENT       70.2    
 LARGEST RESIDUAL MOMENT            1.170E-03   AT NODE       1082   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.979E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -4.886E-06   AT NODE        182   DOF  6
   INSTANCE: SPECIMEN                                                                        
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       2.73       TIME AVG. FORCE        1.82    
 LARGEST RESIDUAL FORCE             3.566E-03   AT NODE        134   DOF  1
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.       -1.017E-02   AT NODE         11   DOF  1
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF DISP.    CORRECTION   -6.578E-07
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      141.       TIME AVG. MOMENT       93.9    
 LARGEST RESIDUAL MOMENT           -0.175       AT NODE        184   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.980E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     3.827E-04   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       2.72       TIME AVG. FORCE        1.82    
 LARGEST RESIDUAL FORCE            -4.326E-04   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        2.514E-05   AT NODE        162   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      141.       TIME AVG. MOMENT       93.8    
 LARGEST RESIDUAL MOMENT            4.067E-03   AT NODE       1446   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.978E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -1.099E-05   AT NODE        294   DOF  6
   INSTANCE: SPECIMEN                                                                        
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.300    
 STEP TIME COMPLETED       0.300    ,  TOTAL TIME COMPLETED        0.300    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       3.63       TIME AVG. FORCE        2.27    
 LARGEST RESIDUAL FORCE            -6.043E-03   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.       -1.018E-02   AT NODE         14   DOF  1
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF DISP.    CORRECTION   -1.116E-06
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      186.       TIME AVG. MOMENT       117.    
 LARGEST RESIDUAL MOMENT           -0.272       AT NODE        184   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.979E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     3.886E-04   AT NODE        183   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       3.63       TIME AVG. FORCE        2.27    
 LARGEST RESIDUAL FORCE            -8.899E-04   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        3.154E-05   AT NODE        317   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      186.       TIME AVG. MOMENT       117.    
 LARGEST RESIDUAL MOMENT            9.345E-03   AT NODE       1446   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.977E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -1.935E-05   AT NODE        182   DOF  6
   INSTANCE: SPECIMEN                                                                        
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.400    
 STEP TIME COMPLETED       0.400    ,  TOTAL TIME COMPLETED        0.400    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       4.53       TIME AVG. FORCE        2.72    
 LARGEST RESIDUAL FORCE             1.136E-02   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        1.019E-02   AT NODE         15   DOF  1
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF DISP.    CORRECTION    2.101E-06
 FORCE     EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 AVERAGE MOMENT                      231.       TIME AVG. MOMENT       140.    
 LARGEST RESIDUAL MOMENT            0.376       AT NODE         78   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.978E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -3.953E-04   AT NODE         79   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       4.54       TIME AVG. FORCE        2.72    
 LARGEST RESIDUAL FORCE            -1.525E-03   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        3.792E-05   AT NODE        274   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      231.       TIME AVG. MOMENT       140.    
 LARGEST RESIDUAL MOMENT            1.709E-02   AT NODE       1082   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.976E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -3.021E-05   AT NODE        294   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION   -1.374E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.500    
 STEP TIME COMPLETED       0.500    ,  TOTAL TIME COMPLETED        0.500    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       5.44       TIME AVG. FORCE        3.18    
 LARGEST RESIDUAL FORCE             1.849E-02   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        1.020E-02   AT NODE         13   DOF  1
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      276.       TIME AVG. MOMENT       162.    
 LARGEST RESIDUAL MOMENT            0.485       AT NODE         78   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.977E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -4.011E-04   AT NODE         79   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       5.44       TIME AVG. FORCE        3.18    
 LARGEST RESIDUAL FORCE            -2.362E-03   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        4.429E-05   AT NODE        100   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      276.       TIME AVG. MOMENT       162.    
 LARGEST RESIDUAL MOMENT            2.654E-02   AT NODE       1082   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.974E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -4.347E-05   AT NODE        294   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION   -2.378E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.600    
 STEP TIME COMPLETED       0.600    ,  TOTAL TIME COMPLETED        0.600    


  INCREMENT     7 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       6.35       TIME AVG. FORCE        3.63    
 LARGEST RESIDUAL FORCE             2.754E-02   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.       -1.022E-02   AT NODE         14   DOF  1
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      321.       TIME AVG. MOMENT       185.    
 LARGEST RESIDUAL MOMENT           -0.600       AT NODE        184   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      2.975E-03   AT NODE          7   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     4.036E-04   AT NODE        183   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          1

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       6.36       TIME AVG. FORCE        3.63    
 LARGEST RESIDUAL FORCE            -3.426E-03   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        5.065E-05   AT NODE        162   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      321.       TIME AVG. MOMENT       185.    
 LARGEST RESIDUAL MOMENT           -3.575E-02   AT NODE        733   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -2.972E-03   AT NODE          2   DOF  5
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     5.828E-05   AT NODE        297   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION    3.473E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.700    
 STEP TIME COMPLETED       0.700    ,  TOTAL TIME COMPLETED        0.700    


  INCREMENT     8 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       7.27       TIME AVG. FORCE        4.09    
 LARGEST RESIDUAL FORCE            -3.859E-02   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        1.023E-02   AT NODE         13   DOF  1
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      367.       TIME AVG. MOMENT       208.    
 LARGEST RESIDUAL MOMENT            0.716       AT NODE         78   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -3.009E-03   AT NODE        296   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -4.000E-04   AT NODE         79   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       7.27       TIME AVG. FORCE        4.09    
 LARGEST RESIDUAL FORCE             4.741E-03   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        5.697E-05   AT NODE        274   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      366.       TIME AVG. MOMENT       208.    
 LARGEST RESIDUAL MOMENT            4.148E-02   AT NODE       1082   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      3.023E-03   AT NODE        183   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     7.257E-05   AT NODE         80   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION    4.206E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.800    
 STEP TIME COMPLETED       0.800    ,  TOTAL TIME COMPLETED        0.800    


  INCREMENT     9 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       8.18       TIME AVG. FORCE        4.54    
 LARGEST RESIDUAL FORCE             5.166E-02   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.       -1.026E-02   AT NODE         14   DOF  1
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      411.       TIME AVG. MOMENT       230.    
 LARGEST RESIDUAL MOMENT            0.828       AT NODE         78   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      3.411E-03   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     3.880E-04   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       8.18       TIME AVG. FORCE        4.54    
 LARGEST RESIDUAL FORCE            -6.318E-03   AT NODE        184   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        6.327E-05   AT NODE        100   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      411.       TIME AVG. MOMENT       230.    
 LARGEST RESIDUAL MOMENT           -5.099E-02   AT NODE       1106   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION     -3.418E-03   AT NODE        296   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION    -8.305E-05   AT NODE        182   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION    5.115E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.900    
 STEP TIME COMPLETED       0.900    ,  TOTAL TIME COMPLETED        0.900    


  INCREMENT    10 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       9.10       TIME AVG. FORCE        5.00    
 LARGEST RESIDUAL FORCE            -6.670E-02   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        1.028E-02   AT NODE         15   DOF  1
   INSTANCE: SPECIMEN                                                                        
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      456.       TIME AVG. MOMENT       253.    
 LARGEST RESIDUAL MOMENT           -0.931       AT NODE        184   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      3.785E-03   AT NODE        295   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     3.709E-04   AT NODE       1089   DOF  6
   INSTANCE: SPECIMEN                                                                        
          ROTATION CORRECTION TOO LARGE COMPARED TO ROTATION INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     11322
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         2.042e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2


 AVERAGE FORCE                       9.09       TIME AVG. FORCE        5.00    
 LARGEST RESIDUAL FORCE             8.156E-03   AT NODE         78   DOF  2
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF DISP.         -1.00       AT NODE          3   DOF  3
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO DISP.        6.954E-05   AT NODE        274   DOF  3
   INSTANCE: SPECIMEN                                                                        
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                      456.       TIME AVG. MOMENT       253.    
 LARGEST RESIDUAL MOMENT           -6.846E-02   AT NODE        728   DOF  4
   INSTANCE: SPECIMEN                                                                        
 LARGEST INCREMENT OF ROTATION      3.780E-03   AT NODE        183   DOF  6
   INSTANCE: SPECIMEN                                                                        
 LARGEST CORRECTION TO ROTATION     8.602E-05   AT NODE         80   DOF  6
   INSTANCE: SPECIMEN                                                                        
 ESTIMATE OF ROTATION CORRECTION    6.324E-06
 MOMENT    EQUILIB. ACCEPTED BASED ON SMALL RESIDUAL AND ESTIMATED CORRECTION

 ITERATION SUMMARY FOR THE INCREMENT:   2 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  2 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF         10  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      21  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      21  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      21  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       0  WARNING MESSAGES DURING USER INPUT PROCESSING
                       0  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   4.1000    
       SYSTEM TIME (SEC)    =  0.50000    
       TOTAL CPU TIME (SEC) =   4.6000    
       WALLCLOCK TIME (SEC) =          5
