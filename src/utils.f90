module utils_module

    !> The effective value of \f$ log(0) \f$
    double precision, parameter :: logzero = -1d20


    contains












    !> How to actually calculate sums from logs.
    !!
    !! i.e. if one has a set of logarithms \f$\{\log(L_i)\}\f$, how should one
    !! calculate \f$ \log(\sum_i L_i)\f$ without underflow?
    !!
    !! One does it with the 'log-sum-exp' trick, by subtracting off the maximum
    !! value so that at least the maxmimum value doesn't underflow, and then add
    !! it back on at the end:
    function logsumexp(vector)
        implicit none
        !> vector of log(w
        double precision, dimension(:),intent(in) :: vector

        double precision :: logsumexp
        double precision :: maximumlog

        maximumlog = maxval(vector)

        logsumexp =  maximumlog + log(sum(exp(vector - maximumlog)))

    end function logsumexp







end module utils_module
