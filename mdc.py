class MDC():
    def calcMDC(self, *numbers):
        for n in numbers:
            if n == 1:
                return 1
            if n < 1:
                return None
        lmax = max(numbers)
        lmin = 2
        sel = None
        for divisor in range(lmin,lmax):
            n = 0
            while (n < len(numbers)) :
                check = False
                if numbers[n] % divisor == 0:
                    sel = divisor
                else:
                    check = True
                n += 1
                