c123456789012345678901234567890
       program input

       integer i,j,k,l,m,n,clock, iseed
       real*4 r
       real*8 x1,y1 

       open(10,file='sample.in')
       write(10,*) ' x   ', '   y'
        
       x1 = -30
       
        call random_seed()
 
       do i = 1, 50000
        call random_number(r)

        x1 = x1 + dx
        dx = 0.0012
        
        y1 = x1*x1 + 15 + 15*(r-0.5)
        print*, r,x1,y1- x1*x1 - 15
        if(x1 .ge. 15 .and. x1 .le. 23) then
c         if(r .ge. 0.5 .and. r .le. 0.6) then
          y1 = y1 + 150*r
c         endif
        endif

        if(x1 .ge. -18 .and. x1 .le. -13) then
c         if(r .ge. 0.5 .and. r .le. 0.6) then
          y1 = y1 - 150*r
c         endif
        endif

c        pause

       write(10,101) x1,',',y1
 101    format(f6.2,A1,f7.3)
       enddo
 
 
       stop
       end 
