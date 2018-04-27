C Fortran implementation of https://github.com/omarestrella/simplify.py
C It uses a combination of Douglas-Peucker and Radial Distance algorithms

C FILE: DPSIMPLIFY.F
      REAL*4 FUNCTION SSD(PX,PY,X0,Y0,XF,YF)
C
C     Return the squared distance from a point to a line segment
C
      REAL*4 PX,PY !Point to calculate distance from 
      REAL*4 X0,Y0 !Start of segment to calculate distance from   
      REAL*4 XF,YF !End of segment

      REAL*4 X, Y, DX, DY, T !Temporary variables for function
      INTEGER T_GT_0,T_GT_1,INTX,INTY !Use bitwise ops to avoid branching

      X = X0
      Y = Y0
      DX = XF - X
      DY = YF - Y

      IF ((DX.NE.0).AND.(DY.NE.0)) THEN
          T = (((PX - X) * DX) + ((PY - Y) * DY))/((DX*DX)+(DY*DY))
          
          T_GT_0 = -TRANSFER((T.GT.0),1)
          T_GT_1 = -TRANSFER((T.GT.1),1)


          !if T > 0: X = X + DX*T
          INTX = TRANSFER(DX*T,1)
          INTY = TRANSFER(DY*T,1)
          X = X + TRANSFER(IAND(T_GT_0,INTX),1.0)
          Y = Y + TRANSFER(IAND(T_GT_0,INTY),1.0)

          !if T > 1: X = XF
          INTX = TRANSFER(X-XF,1)
          INTY = TRANSFER(Y-YF,1)
          X = XF+TRANSFER(IAND(NOT(T_GT_1),INTX),1.0)
          Y = YF+TRANSFER(IAND(NOT(T_GT_1),INTY),1.0)
      END IF
        
      DX = PX - X
      DY = PY - Y

      SSD = (DX*DX)+(DY*DY)
      RETURN 
      END FUNCTION SSD

      SUBROUTINE SIMPLIFY(X,Y,THRESH,MARKS,N)
C
C     Simplify a set of x,y coordinates using Douglas-Peuker
C
      INTEGER N
      REAL*4 X(N),Y(N),THRESH
      LOGICAL MARKS(N)
Cf2py intent(in) x
Cf2py intent(in) y
Cf2py intent(in) thresh
Cf2py intent(hide),depend(x) :: n = len(x)
Cf2py intent(out) marks
      INTEGER FSTACK(N),LSTACK(N),SI !stacks of first/last ranges
      INTEGER FIRST,LAST !indices of current interval
      REAL MAX_SQDIST,SQDIST!keep track of maximum square distance
      INTEGER SQDIST_I 
      REAL SQTHRESH

      !set up temporary variables
      SQDIST_I = 1
      SQTHRESH = THRESH * THRESH
      MARKS(1) = .TRUE.
      MARKS(N) = .TRUE.
      FIRST = 1
      LAST = N
      SI = 1
        
      !main loop
      DO WHILE (SI .NE. 0)
          MAX_SQDIST = 0
          !inner loop: find the largest square segment difference
          DO I=FIRST,LAST-1
            SQDIST = SSD(X(I),Y(I),X(FIRST),Y(FIRST), X(LAST),Y(LAST))

            IF(SQDIST.GT.MAX_SQDIST)THEN
                SQDIST_I = I
                MAX_SQDIST = SQDIST
            ENDIF
          ENDDO
          
          !If the max squared distance is large enough, add to markers
          !and push new first,last bounds to stacks
          IF(MAX_SQDIST.GT.SQTHRESH)THEN
              MARKS(SQDIST_I) = .TRUE.
              FSTACK(SI) = FIRST
              FSTACK(SI+1) = SQDIST_I
              LSTACK(SI) = SQDIST_I
              LSTACK(SI+1) = LAST
              SI = SI + 2
          END IF

          !Pop new first,last bounds from stack
          SI = SI - 1
          FIRST = FSTACK(SI)
          LAST = LSTACK(SI)
      END DO
      END SUBROUTINE SIMPLIFY
C END FILE DPSIMPLIFY.F
