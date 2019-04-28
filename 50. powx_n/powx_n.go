package powxn

func myPow(x float64, n int) float64 {
	if n > 0 {
		return slon(x, n)
	} else if n < 0 {
		return 1.0 / slon(x, -n)
	}
	return 1.0
}

func slon(x float64, n int) float64 {
	if n == 1 {
		return x
	}
	res := slon(x, n/2)
	if n&1 == 0 {
		return res * res
	}
	return res * res * x
}
