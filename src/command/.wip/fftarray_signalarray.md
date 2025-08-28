## FFTarray!(), signalarray!()

"FFTarray" must be floating point and have dimension 2*N where N must be apower of 2 (eg, f(1,1023) assuming OPTION BASE is zero) with the real partin f(0,n) and the imaginary part in f(1,n)."signalarray" must be floating point and the single dimension must be the sameas the FFT array.The command will return the real part of the inverse transform in "signalarray".