1

   Abaqus 2022                                  Date 30-apr-2025   Time 10:48:48
   For use by NORGES TEKNISK NATURVITENSKAPELIGE UNIVERSITET under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                 1.00    
          AND A TOTAL TIME PERIOD OF                            1.00    
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-05
          THE MAXIMUM TIME INCREMENT ALLOWED IS                 1.00    

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

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH      5.04    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

 ***WARNING: The 3-direction at one or more points in one or more layers in 
             1992 elements as defined in *ORIENTATION are in the opposite 
             direction to the element normals. Either the 1 or 2 and the 
             3-direction defined in *ORIENTATION will be reversed. The elements 
             have been identified in element set 
             WarnElem3DirOppElemNormalStep1Inc1.


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   1.00    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13261
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.559e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =  0.10000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             PLATE.147 D.O.F. 6 RATIO = 11.6192E+09 .

                    3 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    3 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     1

   MAX. PENETRATION ERROR -8.21756     AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -31.5755E+03  AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          PENETRATION ERROR TOO LARGE COMPARED TO DISPLACEMENT INCREMENT.

 AVERAGE FORCE                       819.       TIME AVG. FORCE        819.    
 LARGEST RESIDUAL FORCE             2.632E+04   AT NODE         11   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.        -1.421E+03   AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.       -1.421E+03   AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      5.19       TIME AVG. MOMENT       5.19    
 LARGEST RESIDUAL MOMENT            3.525E-08   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION      -1.51       AT NODE          2   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION     -1.51       AT NODE          2   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13258
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.559e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

                    2 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    2 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     2

   MAX. PENETRATION ERROR -1.37905     AT NODE PLATE.26 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -25.1136E+03  AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE ESTIMATED CONTACT FORCE ERROR IS OUTSIDE OF CONVERGENCE TOLERANCES.

 AVERAGE FORCE                       838.       TIME AVG. FORCE        838.    
 LARGEST RESIDUAL FORCE             2.160E+04   AT NODE          6   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.         -526.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.         895.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      7.83       TIME AVG. MOMENT       7.83    
 LARGEST RESIDUAL MOMENT           -2.219E-08   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -0.575       AT NODE         46   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION     0.975       AT NODE        628   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13256
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.556e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.

     NEGATIVE EIGENVALUES MEAN THAT THE SYSTEM MATRIX IS NOT 
     POSITIVE DEFINITE:
     FOR EXAMPLE, A BIFURCATION (BUCKLING) LOAD MAY HAVE BEEN EXCEEDED.

                    3 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    2 POINTS CHANGED FROM OPEN TO CLOSED
                    1 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     3

   MAX. PENETRATION ERROR -9.66781     AT NODE PLATE.3 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -37.1480E+03  AT NODE PLATE.3 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          PENETRATION ERROR TOO LARGE COMPARED TO DISPLACEMENT INCREMENT.

 AVERAGE FORCE                       877.       TIME AVG. FORCE        877.    
 LARGEST RESIDUAL FORCE            -4.583E+04   AT NODE          3   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.         1.025E+03   AT NODE          9   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.        1.551E+03   AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      15.6       TIME AVG. MOMENT       15.6    
 LARGEST RESIDUAL MOMENT           -3.850E-08   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION       1.12       AT NODE         45   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION      1.68       AT NODE          6   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13257
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.558e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

                    4 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    3 POINTS CHANGED FROM OPEN TO CLOSED
                    1 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     4

   MAX. PENETRATION ERROR -2.19029     AT NODE PLATE.57 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -31.9215E+03  AT NODE PLATE.58 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          PENETRATION ERROR TOO LARGE COMPARED TO DISPLACEMENT INCREMENT.

 AVERAGE FORCE                       861.       TIME AVG. FORCE        861.    
 LARGEST RESIDUAL FORCE             3.062E+04   AT NODE         58   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.          358.       AT NODE          9   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.        -667.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      14.2       TIME AVG. MOMENT       14.2    
 LARGEST RESIDUAL MOMENT            1.659E-08   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION      0.411       AT NODE         27   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION    -0.755       AT NODE          3   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13259
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.571e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          1

                    4 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    2 POINTS CHANGED FROM OPEN TO CLOSED
                    2 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     5

   MAX. PENETRATION ERROR 205.774E-03   AT NODE PLATE.41 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -15.0993E+03  AT NODE PLATE.57 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE ESTIMATED CONTACT FORCE ERROR IS OUTSIDE OF CONVERGENCE TOLERANCES.

 AVERAGE FORCE                       821.       TIME AVG. FORCE        821.    
 LARGEST RESIDUAL FORCE             1.516E+04   AT NODE         57   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.          184.       AT NODE          9   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.        -173.       AT NODE        632   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      3.98       TIME AVG. MOMENT       3.98    
 LARGEST RESIDUAL MOMENT            4.296E-09   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION      0.207       AT NODE         26   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION    -0.226       AT NODE         60   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13259
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.582e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.
             EXPLANATIONS ARE SUGGESTED AFTER THE FIRST OCCURRENCE OF THIS MESSAGE.

                    8 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    6 POINTS CHANGED FROM OPEN TO CLOSED
                    2 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     6

   MAX. PENETRATION ERROR -1.02429     AT NODE PLATE.27 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -4.34955E+03 AT NODE PLATE.41 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          PENETRATION ERROR TOO LARGE COMPARED TO DISPLACEMENT INCREMENT.

 AVERAGE FORCE                       850.       TIME AVG. FORCE        850.    
 LARGEST RESIDUAL FORCE             1.273E+04   AT NODE         27   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.         -198.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.        -382.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      5.25       TIME AVG. MOMENT       5.25    
 LARGEST RESIDUAL MOMENT            9.472E-09   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -0.232       AT NODE         40   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION    -0.426       AT NODE         27   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13263
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.584e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0

                    6 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    3 POINTS CHANGED FROM OPEN TO CLOSED
                    3 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     7

   MAX. PENETRATION ERROR -242.142E-03   AT NODE PLATE.2 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -9.60992E+03 AT NODE PLATE.11 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE ESTIMATED CONTACT FORCE ERROR IS OUTSIDE OF CONVERGENCE TOLERANCES.

 AVERAGE FORCE                       830.       TIME AVG. FORCE        830.    
 LARGEST RESIDUAL FORCE             9.456E+03   AT NODE         11   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.         -51.3       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.         147.       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      2.49       TIME AVG. MOMENT       2.49    
 LARGEST RESIDUAL MOMENT           -3.634E-09   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -6.883E-02   AT NODE         40   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION     0.170       AT NODE         27   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13263
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.598e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.
             EXPLANATIONS ARE SUGGESTED AFTER THE FIRST OCCURRENCE OF THIS MESSAGE.

                    5 SEVERE DISCONTINUITIES OCCURRED DURING THIS ITERATION.
                    2 POINTS CHANGED FROM OPEN TO CLOSED
                    3 POINTS CHANGED FROM CLOSED TO OPEN

               CONVERGENCE CHECKS FOR SEVERE DISCONTINUITY ITERATION     8

   MAX. PENETRATION ERROR 106.464E-03   AT NODE PLATE.26 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -7.78901E+03 AT NODE PLATE.629 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          PENETRATION ERROR TOO LARGE COMPARED TO DISPLACEMENT INCREMENT.

 AVERAGE FORCE                       824.       TIME AVG. FORCE        824.    
 LARGEST RESIDUAL FORCE             6.030E+03   AT NODE        629   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.         -19.0       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.         32.3       AT NODE        632   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                      1.07       TIME AVG. MOMENT       1.07    
 LARGEST RESIDUAL MOMENT           -7.987E-10   AT NODE        252   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -3.073E-02   AT NODE          6   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION     5.046E-02   AT NODE        630   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13262
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.579e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.
             EXPLANATIONS ARE SUGGESTED AFTER THE FIRST OCCURRENCE OF THIS MESSAGE.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1

   MAX. PENETRATION ERROR -4.46210E-03 AT NODE PLATE.27 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -17.1454      AT NODE PLATE.27 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE CONTACT CONSTRAINTS HAVE CONVERGED.

 AVERAGE FORCE                       822.       TIME AVG. FORCE        822.    
 LARGEST RESIDUAL FORCE              163.       AT NODE         26   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.          3.66       AT NODE          9   DOF  2
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.         22.6       AT NODE        249   DOF  2
   INSTANCE: PLATE                                                                           
          FORCE     EQUILIBRIUM NOT ACHIEVED WITHIN TOLERANCE.

 AVERAGE MOMENT                     0.403       TIME AVG. MOMENT      0.403    
 LARGEST RESIDUAL MOMENT           -5.624E-10   AT NODE        251   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION      1.102E-02   AT NODE         25   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION     3.189E-02   AT NODE          2   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13262
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.579e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   0.0000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =   0.0000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.
             EXPLANATIONS ARE SUGGESTED AFTER THE FIRST OCCURRENCE OF THIS MESSAGE.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     2

   MAX. PENETRATION ERROR -101.119E-06   AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -388.545E-03   AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE CONTACT CONSTRAINTS HAVE CONVERGED.

 AVERAGE FORCE                       823.       TIME AVG. FORCE        823.    
 LARGEST RESIDUAL FORCE            -0.613       AT NODE          6   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.          1.42       AT NODE         12   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.        -3.83       AT NODE         12   DOF  2
   INSTANCE: PLATE                                                                           
          DISP.    CORRECTION TOO LARGE COMPARED TO DISP.    INCREMENT

 AVERAGE MOMENT                     0.400       TIME AVG. MOMENT      0.400    
 LARGEST RESIDUAL MOMENT            9.614E-11   AT NODE        253   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -7.678E-03   AT NODE         41   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION    -4.308E-03   AT NODE         40   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST:        1 MPI RANK  x 1 THREAD
 	NUMBER OF EQUATIONS:     13262
 	NUMBER OF RHS:           1
 	NUMBER OF FLOPS:         1.579e+08

     CHECK POINT   START OF SOLVER    

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =  0.10000    
       ELAPSED SYSTEM TIME (SEC)    =   0.0000    
       ELAPSED TOTAL CPU TIME (SEC) =  0.10000    
       ELAPSED WALLCLOCK TIME (SEC) =          0
 

 ***WARNING: THE SYSTEM MATRIX HAS 1 NEGATIVE EIGENVALUES.
             EXPLANATIONS ARE SUGGESTED AFTER THE FIRST OCCURRENCE OF THIS MESSAGE.

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     3

   MAX. PENETRATION ERROR -612.239E-12   AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
   MAX. CONTACT FORCE ERROR -2.35249E-06 AT NODE PLATE.6 OF CONTACT PAIR 
   (ASSEMBLY_EDGES-HOLE-BOLT-1_CNS_,ASSEMBLY_BOLT-1_SURFACE-BOLT-1)
          THE CONTACT CONSTRAINTS HAVE CONVERGED.

 AVERAGE FORCE                       823.       TIME AVG. FORCE        823.    
 LARGEST RESIDUAL FORCE            -4.816E-05   AT NODE          6   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF DISP.          1.42       AT NODE         12   DOF  1
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO DISP.       -1.365E-03   AT NODE        247   DOF  2
   INSTANCE: PLATE                                                                           
          THE FORCE     EQUILIBRIUM EQUATIONS HAVE CONVERGED

 AVERAGE MOMENT                     0.400       TIME AVG. MOMENT      0.400    
 LARGEST RESIDUAL MOMENT           -6.122E-12   AT NODE          3   DOF  5
   INSTANCE: PLATE                                                                           
 LARGEST INCREMENT OF ROTATION     -7.683E-03   AT NODE         41   DOF  6
   INSTANCE: PLATE                                                                           
 LARGEST CORRECTION TO ROTATION    -5.856E-06   AT NODE          2   DOF  6
   INSTANCE: PLATE                                                                           
          THE MOMENT    EQUILIBRIUM EQUATIONS HAVE CONVERGED

 ITERATION SUMMARY FOR THE INCREMENT:  11 TOTAL ITERATIONS, OF WHICH
   8 ARE SEVERE DISCONTINUITY ITERATIONS AND  3 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   1.00    ,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          1  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      11  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      11  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      11  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       4  WARNING MESSAGES DURING USER INPUT PROCESSING
                       8  WARNING MESSAGES DURING ANALYSIS
                       1  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       6  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   3.0000    
       SYSTEM TIME (SEC)    =  0.10000    
       TOTAL CPU TIME (SEC) =   3.1000    
       WALLCLOCK TIME (SEC) =          3
